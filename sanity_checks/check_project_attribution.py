#!/usr/bin/env python3
"""
Simple script to check if all YAML project attributions in content files have corresponding folders in /content/research/
"""

import re
import yaml
from pathlib import Path

# Base directory configuration
BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / 'content'
RESEARCH_DIR = CONTENT_DIR / 'research'

def get_research_projects():
    """Get list of all project folders in /content/research/"""
    if not RESEARCH_DIR.exists():
        print(f"Research directory {RESEARCH_DIR.absolute()} does not exist!")
        return set()
    
    return {item.name for item in RESEARCH_DIR.iterdir() 
            if item.is_dir() and not item.name.startswith('_')}

def extract_projects_simple(content):
    """Extract projects using simple pattern matching."""
    projects = None
    has_projects_field = False
    
    # Remove commented lines first
    lines = [line for line in content.split('\n') if not line.strip().startswith('#')]
    clean_content = '\n'.join(lines)
    
    # Pattern 1: Single line with value (projects: value or projects: [item1, item2])
    single_match = re.search(r'^\s*projects:\s*(.+?)\s*$', clean_content, re.MULTILINE)
    if single_match:
        has_projects_field = True
        value = single_match.group(1).strip()
        if value.startswith('[') and value.endswith(']'):
            # Inline list format
            inner = value[1:-1].strip()
            if inner == '':
                # Empty list [] is valid
                projects = []
            elif inner in ["''", '""']:
                # List with empty strings -> NoneType (needs fixing)
                projects = None
            else:
                projects = [p.strip().strip('"\'') for p in inner.split(',')]
        elif value and not value.startswith('#') and value != '---':
            # Single value (but not the YAML separator)
            projects = [value.strip().strip('"\'')]
        else:
            # Empty, comment only, or YAML separator
            projects = None
    
    # Pattern 2: Multi-line format (projects:\n  - item1\n  - item2)
    elif re.search(r'^\s*projects:\s*$', clean_content, re.MULTILINE):
        has_projects_field = True
        # Look for list items after projects line
        lines = clean_content.split('\n')
        projects_line_idx = None
        
        for i, line in enumerate(lines):
            if re.match(r'^\s*projects:\s*$', line):
                projects_line_idx = i
                break
        
        if projects_line_idx is not None:
            # Look for list items in following lines
            projects = []
            for line in lines[projects_line_idx + 1:]:
                stripped = line.strip()
                # Stop when we hit a non-list item, empty line, or YAML separator
                if stripped and not stripped.startswith('- ') and stripped != '---':
                    break
                if stripped.startswith('- '):
                    projects.append(stripped[2:].strip().strip('"\''))
                elif stripped == '---':
                    break  # Stop at YAML separator
            
            projects = projects if projects else None
    
    return projects, has_projects_field

def check_projects_in_content(fix_none_type=False):
    """Check all content files for project attributions."""
    research_projects = get_research_projects()
    
    print(f"Found {len(research_projects)} research projects: {sorted(research_projects)}")
    print("=" * 60)
    
    issues = []
    files_checked = 0
    files_with_projects = 0
    none_type_files = []
    
    for md_file in CONTENT_DIR.rglob('*.md'):
        if 'research/' in str(md_file):
            continue
        
        files_checked += 1
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
        
        projects, has_projects_field = extract_projects_simple(content)
        
        if has_projects_field:
            # Only count as having projects if it was actually found (not commented out)
            files_with_projects += 1
            
            if projects is None:
                # projects field exists but is NoneType
                none_type_files.append(str(md_file))
                if fix_none_type:
                    if fix_projects_field(md_file):
                        print(f"🔧 Fixed NoneType in: {md_file}")
            elif isinstance(projects, str):
                projects = [projects]
            
            if projects:  # Only check for missing projects if we have a valid list
                for project in projects:
                    if project not in research_projects:
                        issues.append({
                            'file': str(md_file),
                            'missing_project': project,
                            'existing_projects': projects
                        })
    
    # Report results
    print(f"\nChecked {files_checked} markdown files")
    print(f"Found {files_with_projects} files with valid 'projects' attribute")
    
    if none_type_files:
        print(f"Found {len(none_type_files)} files with NoneType 'projects' field:")
        for file_path in none_type_files:
            print(f"  📄 {file_path}")
        
        if fix_none_type:
            print(f"\n🔧 Attempted to fix {len(none_type_files)} NoneType files")
        else:
            print(f"\n💡 Run with --fix to automatically fix NoneType fields")
    
    if issues:
        print(f"\n❌ Found {len(issues)} missing project references:")
        print("=" * 60)
        
        for issue in issues:
            print(f"📄 {issue['file']}")
            print(f"   Missing project: '{issue['missing_project']}'")
            print(f"   All projects in file: {issue['existing_projects']}")
            print()
    else:
        print("\n✅ All project references are valid!")
    
    return len(issues) == 0 and (not none_type_files or fix_none_type)

def fix_projects_field(file_path):
    """Fix empty projects field by adding []"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix 1: Replace empty projects: with projects: []
        new_content = re.sub(r'^(\s*)projects:\s*$', r'\1projects: []', content, flags=re.MULTILINE)
        
        # Fix 2: Replace projects: [''] with projects: []
        new_content = re.sub(r'^(\s*)projects:\s*\[\'\'\]\s*$', r'\1projects: []', new_content, flags=re.MULTILINE)
        new_content = re.sub(r'^(\s*)projects:\s*\[""\]\s*$', r'\1projects: []', new_content, flags=re.MULTILINE)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
    
    return False

if __name__ == "__main__":
    import sys
    
    fix_none_type = "--fix" in sys.argv
    
    print("Checking project attributions in content files...")
    if fix_none_type:
        print("🔧 Auto-fix mode enabled for NoneType fields")
    print("=" * 60)
    
    success = check_projects_in_content(fix_none_type=fix_none_type)
    
    if success:
        print("\n🎉 All checks passed!")
        exit(0)
    else:
        print("\n💥 Some checks failed!")
        exit(1)
