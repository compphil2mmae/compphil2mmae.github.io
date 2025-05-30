#!/usr/bin/env python3
# filepath: migrate_content.py
"""
Migration Script for Hugo Multilingual Content Structure

This script reorganizes a Hugo site's content from language-based folders
(content/en/, content/) to a unified structure with language identifiers in filenames.

Usage:
    python3 migrate_content.py [--dry-run] [--path /path/to/site]

Options:
    --dry-run   Show what would be done without making actual changes
    --path      Path to the Hugo site root (defaults to current directory)
"""

import os
import shutil
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Migrate Hugo multilingual content structure")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be done without making changes")
    parser.add_argument('--path', default='.', help="Path to the Hugo site root")
    return parser.parse_args()

def process_files(site_path, dry_run=False):
    content_dir = os.path.join(site_path, 'content')
    en_content_dir = os.path.join(content_dir, 'en')
    
    if not os.path.exists(en_content_dir):
        print(f"Error: English content directory not found at {en_content_dir}")
        return
    
    print(f"Processing English content in {en_content_dir}...")
    
    # Track statistics
    stats = {
        'files_processed': 0,
        'moved': 0,
        'renamed': 0,
        'conflicts': 0
    }
    
    # Process English content
    for root, dirs, files in os.walk(en_content_dir):
        # Calculate relative path to maintain directory structure
        rel_path = os.path.relpath(root, en_content_dir)
        if rel_path == '.':
            rel_path = ''
        
        # Create target directory if it doesn't exist
        target_dir = os.path.join(content_dir, rel_path)
        if not os.path.exists(target_dir) and not dry_run:
            os.makedirs(target_dir, exist_ok=True)
        
        for file in files:
            stats['files_processed'] += 1
            src_file = os.path.join(root, file)
            
            # Split filename and extension for renaming
            filename, extension = os.path.splitext(file)
            
            # Skip language code if already present
            if filename.endswith('.en'):
                new_filename = file
            else:
                new_filename = f"{filename}.en{extension}"
            
            dst_file = os.path.join(target_dir, new_filename)
            
            # Check for conflicts
            if os.path.exists(dst_file):
                print(f"CONFLICT: {dst_file} already exists")
                stats['conflicts'] += 1
                continue
                
            # Handle German counterpart naming
            de_counterpart = os.path.join(target_dir, file)
            has_de_counterpart = os.path.exists(de_counterpart)
            
            # Report actions
            if dry_run:
                print(f"Would move: {src_file} -> {dst_file}")
                if has_de_counterpart:
                    print(f"  Note: German version exists at {de_counterpart}")
            else:
                # Move and rename the file
                shutil.copy2(src_file, dst_file)
                print(f"Moved: {src_file} -> {dst_file}")
                stats['moved'] += 1
                stats['renamed'] += (new_filename != file)
    
    # Process German content (optional)
    print("\nChecking German content...")
    for root, dirs, files in os.walk(content_dir):
        # Skip the English content directory during processing
        if root.startswith(en_content_dir):
            continue
            
        for file in files:
            # Skip files that already have language codes
            if '.en.' in file or '.de.' in file:
                continue
                
            file_path = os.path.join(root, file)
            filename, extension = os.path.splitext(file)
            
            # Check if this might need a .de suffix
            en_counterpart = os.path.join(root, f"{filename}.en{extension}")
            if os.path.exists(en_counterpart):
                de_filename = f"{filename}.de{extension}"
                de_path = os.path.join(root, de_filename)
                
                if dry_run:
                    print(f"Would rename: {file_path} -> {de_path} (German version)")
                else:
                    # Rename to add .de suffix
                    shutil.copy2(file_path, de_path)
                    os.remove(file_path)
                    print(f"Renamed: {file_path} -> {de_path} (German version)")
                    stats['renamed'] += 1
    
    # Remove the original English content directory if not dry run
    if not dry_run and stats['conflicts'] == 0:
        print(f"\nRemoving original English content directory: {en_content_dir}")
        shutil.rmtree(en_content_dir)
    
    # Display summary
    print("\nMigration Summary:")
    print(f"  Files processed: {stats['files_processed']}")
    print(f"  Files moved: {stats['moved']}")
    print(f"  Files renamed: {stats['renamed']}")
    print(f"  Conflicts detected: {stats['conflicts']}")
    
    if dry_run:
        print("\nThis was a dry run. No files were actually modified.")
    else:
        print("\nMigration complete!")
        print("\nNext steps:")
        print("1. Update your config.toml to use the same contentDir for both languages")
        print("2. Test your site to ensure all links work correctly")
        print("3. Update your language selector to handle the new URL structure")

def main():
    args = parse_args()
    site_path = os.path.abspath(args.path)
    
    print(f"Hugo Site Migration Tool")
    print(f"Site path: {site_path}")
    print(f"Mode: {'Dry run' if args.dry_run else 'Live run'}\n")
    
    process_files(site_path, args.dry_run)

if __name__ == "__main__":
    main()