#!/usr/bin/env python3
"""
Publication validation script for Hugo academic website.
Checks all publications under /content/publication/ for required parameters and coherence.
"""

import re
from datetime import date

import unicodedata
import yaml
from pathlib import Path
from typing import Dict, Set

# Valid publication types from archetype
VALID_PUBLICATION_TYPES = {
    'inproceedings': 'conference-paper',
    'article': 'article-journal',
    'unpublished': 'preprint',
    'report': 'report',
    'techreport': 'report',
    'book': 'book',
    'proceedings': 'book',
    'booklet': 'book',
    'manual': 'book',
    'inbook': 'chapter',
    'incollection': 'chapter',
    'thesis': 'thesis',
    'phdthesis': 'thesis',
    'masterthesis': 'thesis',
    'patent': 'patent',
    'review': 'review',
}


class PublicationValidator:
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
        self.errors = []
        self.warnings = []
        self.notifications = []
        self.ignored_proper_translation: set[str] = set()

        # Cache existing author directories for reuse across multiple validation runs
        self.existing_author_dirs = self._load_author_directories()

    def _load_author_directories(self) -> Set[str]:
        """Load existing author directories once and cache them."""
        authors_dir = self.work_dir / 'content' / 'authors'
        if authors_dir.exists():
            return {d.name for d in authors_dir.iterdir() if d.is_dir()}
        return set()

    def _convert_ints_to_strings(self, data):
        """Recursively convert all integers to strings while preserving other types."""
        if isinstance(data, dict):
            return {k: self._convert_ints_to_strings(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._convert_ints_to_strings(item) for item in data]
        elif isinstance(data, int):
            return str(data)
        elif isinstance(data, date):
            return data.isoformat()
        else:
            return data

    def load_yaml_frontmatter(self, file_path: Path) -> Dict:
        """Load YAML frontmatter from markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML frontmatter between --- markers
            match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                self.errors.append(f"{file_path}: No YAML frontmatter found")
                return {}

            return self._convert_ints_to_strings(yaml.safe_load(match.group(1)) or {})
        except Exception as e:
            self.errors.append(f"{file_path}: Error parsing YAML: {e}")
            return {}

    def load_bib_file(self, bib_path: Path) -> Dict:
        """Load and parse .bib file."""
        if not bib_path.exists():
            return {}

        try:
            with open(bib_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple BibTeX parsing
            entry = {}
            match = re.search(r'@(\w+)\{([^,]+),\s*(.*)\}', content, re.DOTALL)
            if match:
                entry['bib_type'] = match.group(1)
                entry['bib_key'] = match.group(2)

                # Parse fields
                fields = match.group(3)
                for field_match in re.finditer(r'(\w+)\s*=\s*\{(.*)\}', fields):
                    entry[field_match.group(1)] = field_match.group(2).strip()

            return self._convert_ints_to_strings(entry)
        except Exception as e:
            self.errors.append(f"{bib_path}: Error parsing BibTeX: {e}")
            return {}

    @staticmethod
    def normalize(text: str, pattern = r'[^a-zß\s]', repl = '') -> str:
        """Clean text/string by removing special characters and converting to lowercase."""
        text = text or ''
        text = text.replace('ä', 'ae').replace('ü', 'ue').replace('ö', 'oe')
        text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
        text = re.sub(pattern, repl, text.lower())
        return re.sub(r'\s+', ' ', text).strip()

    def check_null_values(self, pub_data: Dict, pub_path: Path) -> None:
        """Check for None values in publication data."""
        for field in pub_data:
            if pub_data[field] is None:
                self.errors.append(f"{pub_path}: Field '{field}' has None value (initialized but not declared)")

    def check_publication_types(self, pub_data: Dict, pub_path: Path) -> None:
        """Check publication type is exactly one of valid types."""
        pub_types = pub_data.get('publication_types', [])

        if not pub_types:
            self.errors.append(f"{pub_path}: Missing publication_types")
            return

        if len(pub_types) != 1:
            self.errors.append(f"{pub_path}: Must have exactly one publication type, found {len(pub_types)}")
            return

        pub_type = pub_types[0]
        if pub_type not in VALID_PUBLICATION_TYPES.values():
            self.errors.append(f"{pub_path}: Invalid publication type '{pub_type}'. Must be one of: {', '.join(sorted(VALID_PUBLICATION_TYPES.values()))}")

    def check_type_specific_requirements(self, pub_data: Dict, pub_path: Path) -> None:
        """Check requirements specific to publication types."""
        pub_types = pub_data.get('publication_types', [])
        if not pub_types:
            return

        pub_type = pub_types[0]

        if pub_type == 'chapter':
            # Chapters require booktitle, pages & publisher
            for field in ['booktitle', 'pages', 'publisher']:
                if field not in pub_data or not pub_data[field]:
                    self.errors.append(f"{pub_path}: Chapter type requires {field}")

        elif pub_type == 'thesis':
            # Thesis requires type & school
            for field in ['sub_type', 'school']:
                if field not in pub_data or not pub_data[field]:
                    self.errors.append(f"{pub_path}: Thesis type requires {field}")

        elif pub_type == 'report':
            # Reports need a link named "Report"
            links = pub_data.get('links', [])
            report_link_found = any(link.get('name') == 'Report' for link in links)
            if not report_link_found:
                self.errors.append(f"{pub_path}: Report type requires a link named 'Report'")

        elif pub_type in ['book', 'chapter']:
            # Books and chapters require publisher
            if 'publisher' not in pub_data or not pub_data['publisher']:
                self.errors.append(f"{pub_path}: {pub_type} type requires publisher")

        elif pub_type == 'article-journal':
            # Articles require journal attribute
            if 'journal' not in pub_data or not pub_data['journal']:
                self.errors.append(f"{pub_path}: Article-journal type requires journal attribute")

        elif pub_type == 'conference-paper':
            # Conference-papers need eventtitle
            if 'eventtitle' not in pub_data or not pub_data['eventtitle']:
                self.errors.append(f"{pub_path}: Conference-paper type requires eventtitle")

    def check_author_exists(self, pub_data: Dict, pub_path: Path) -> None:
        """Check if author exists and has proper formatting."""
        authors = pub_data.get('authors', [])
        if not authors:
            self.errors.append(f"{pub_path}: Missing author")
            return

        for author in authors:
            if not author or not author.strip():
                self.errors.append(f"{pub_path}: Empty author entry")
                continue

            author = author.strip()

            # Check if author is in prename.surname format (folder reference)
            if '.' in author and not ' ' in author:
                # This should be a folder reference
                if author not in self.existing_author_dirs:
                    self.errors.append(f"{pub_path}: Author '{author}' references non-existent folder /content/authors/{author}/")
            else:
                # This is a formatted name, check if there's a corresponding author page
                # Normalize author name: remove titles and special chars, allow German umlaute
                normalized_author = self.normalize(author, repl=' ')
                # Remove titles using word boundaries to prevent partial name matches
                for title in ['dr', 'prof', 'professor']:
                    normalized_author = re.sub(rf'\b{title}\b', '', normalized_author).strip()
                normalized_author = re.sub(r'\s+', ' ', normalized_author).strip()
                author_split = normalized_author.split()
                if len(author_split) != 2:
                    self.errors.append(f"{pub_path}: Author '{author}' is has unrecognized format")
                else:
                    if f"{author_split[0]}.{author_split[1]}" in self.existing_author_dirs:
                        self.warnings.append(f"{pub_path}: Author '{author}' should be referenced as '{author_split[0]}.{author_split[1]}' instead of formatted name")
                    elif f"{author_split[1]},{author_split[0]}" in self.existing_author_dirs:
                        self.warnings.append(f"{pub_path}: Author '{author}' should be referenced as '{author_split[1]}.{author_split[0]}' instead of formatted name")
                    elif not f"{author_split[0]} {author_split[1]}".title() == author.replace('ä', 'ae').replace('ü', 'ue').replace('ö', 'oe').strip():
                        self.errors.append(f"{pub_path}: Author '{author}' is has unrecognized format")

    def check_publication_parameter(self, pub_data: Dict, pub_path: Path) -> None:
        """Check publication & publication_short attributes."""
        publication = pub_data.get('publication', '')

        # Check if publication can be replaced by more specific fields
        pub_types = pub_data.get('publication_types', [])
        if pub_types and len(pub_types) == 1 and publication:
            pub_type = pub_types[0]

            if pub_type == 'article-journal' and not pub_data.get('journal'):
                self.errors.append(f"{pub_path}: Publishing medium should be moved 'publication' to 'journal' field")
            elif pub_type == 'book' and not pub_data.get('publisher'):
                self.errors.append(f"{pub_path}: The Books publisher should be moved from 'publication' and stated in 'publisher' field")
            elif pub_type == 'chapter' and not pub_data.get('publisher'):
                self.errors.append(f"{pub_path}: The chapter containing book should be stated in 'booktitle' instead of 'publication' field")
        if "publication" in pub_data or "publication_short" in pub_data:
            self.warnings.append(f"{pub_path}: Deprecated autogenerated 'publication' and 'publication_short' attributes should be removed ('journal', 'booktitle' & 'publisher' used instead)")

    def check_short_parameters(self, pub_data: Dict, pub_path: Path) -> None:
        """Check short attributes."""
        abbreviated_fields = ['publication', 'journal', 'publisher']

        for field in abbreviated_fields:
          field_short = f"{field}_short"
          value = pub_data.get(field, '-1') or ''
          value_short = pub_data.get(field_short, '-1') or ''

          # Check if short version exists but base version doesn't
          if value_short != '-1' and value_short.strip('*').strip() and (value == '-1' or not value.strip('*').strip()):
            self.errors.append(f"{pub_path}: '{field_short}' exists but corresponding '{field}' not")

          # Check for empty fields with asterisks
          for f, v in [(field, value)]:
            if v != '-1' and not v.strip('*').strip():
              self.warnings.append(f"{pub_path}: Empty '{f}' field should be removed")

    def check_date_parameter(self, pub_data: Dict, pub_path: Path) -> None:
        """Check date parameter is always set."""
        if ('date' not in pub_data or not pub_data['date']) and ('pubstate' not in pub_data or not pub_data['pubstate'] or pub_data['pubstate'] == 'published'):
            self.errors.append(f"{pub_path}: Missing date parameter")

    def check_address_location_consistency(self, pub_data: Dict, pub_path: Path) -> None:
        """Check address/location parameter consistency."""
        has_address = 'address' in pub_data and pub_data['address']
        has_location = 'location' in pub_data and pub_data['location']

        if has_address and has_location:
            if pub_data['address'] == pub_data['location']:
              self.errors.append(f"{pub_path}: Address is duplication of location")
            elif not pub_data['location'] in pub_data['address']:
              self.errors.append(f"{pub_path}: There is a mismatch between address and location, {pub_data['location']} is not part of the address:{pub_data['address']}")

        if has_address and not has_location:
            # If address contains only one word, suggest changing to location
            address = pub_data['address'].strip()
            if len(address.split()) == 1:
                self.warnings.append(f"{pub_path}: Single-word address '{address}' should be moved to location field")
            else:
                self.errors.append(f"{pub_path}: Has address but no location. Add location field")

    def check_author_notes_parameter(self, pub_data: Dict, pub_path: Path) -> None:
        """Check author notes parameter."""
        if 'author_notes' in pub_data and pub_data.get('author_notes') and len(pub_data.get('author_notes')) != len(pub_data.get('authors', [])):
            self.errors.append(f"{pub_path}: The number of author notes does not match the number of authors. Add (empty) notes for each author")

    def check_links(self, pub_data: Dict, pub_path: Path) -> None:
        """Check links."""
        for link in pub_data.get('links', []):
            if "philpapers.org" in link.get('url') and (link.get('name') != "PhilPapers" or link.get('icon') != "philpapers" or link.get('icon_pack') != "ai"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a PhilPapers link")
            elif "springer.com" in link.get('url') and link.get('name') == "URL" and (link.get('icon') != "springer" or link.get('icon_pack') != "ai"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a Springer URL link")
            elif "publikationen.bibliothek.kit.edu" in link.get('url') and (link.get('name') != "URL" or link.get('icon') != "open-access" or link.get('icon_pack') != "ai"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a open-access URL link")
            elif (link.get('name') in ["Book", "Buch"] and (link.get('icon') != "book" or link.get('icon_pack', 'fas') != "fas")) or (link.get('name') not in ["Book", "Buch"] and link.get('icon') == "book"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a book link")
            elif (any(domain in link.get('url') for domain in ['github.com', 'gitlab.com']) and (link.get('name') != "Code" or link.get('icon') != "file-code" or link.get('icon_pack', 'fas') != "fas")) or (link.get('name') == "Code" and link.get('icon') != "file-code"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a code link")
            elif ".pdf" in link.get('url') and (link.get('name') != "PDF" or link.get('icon') != "file-pdf" or link.get('icon_pack', 'fas') != "fas"):
                self.warnings.append(f"{pub_path}: Link {link.get('name')} ({link.get('url')}) is incorrectly visualized, should be a PDF link")
            if ".pdf" in link.get('url') and "/" not in link.get('url') and not (pub_path / link.get('url')).exists():
                self.errors.append(f"{pub_path}: Referenced PDF {link.get('url')} deosn't exists at {pub_path / link.get('url')}")
            elif ".pdf" in link.get('url') and "http" not in link.get('url') and "/" in link.get('url') and not (self.work_dir / 'static' / link.get('url')).exists():
                self.errors.append(f"{pub_path}: Referenced PDF {link.get('url')} deosn't exists at {self.work_dir / 'static' / link.get('url')}")

        pdf_files = {f.name for f in pub_path.glob("*.pdf")}
        linked = {link.get('url') for link in pub_data.get('links', []) if link.get('url').endswith(".pdf") and '/' not in link.get('url')}
        unlinked = pdf_files - linked - {pub_path.name+".pdf"}
        if unlinked:
            self.warnings.append(f"{pub_path}: contains [{", ".join(unlinked)}], that are not linked")

    def check_pubstate_parameter(self, pub_data: Dict, pub_path: Path) -> None:
        """Check pubstate parameter."""
        date = re.match(r'\d{4}-\d{2}-\d{2}', pub_data.get('date', ''))
        if date and pub_data.get('pubstate'):
            if pub_data.get('pubstate') != 'published':
                self.errors.append(f"{pub_path}: {pub_data['pubstate']} 'pubstate' doesn't fit published state of the paper (date is fully set: {pub_data['date']}) and should be removed or at least set to 'published'.")
            else:
                self.warnings.append(f"{pub_path}: 'pubstate' field should be removed after publication (date fully set: {pub_data['date']}).")
        if not date:
            if pub_data.get('pubstate') == 'published':
                self.errors.append(f"{pub_path}: add missing publication date and remove 'pubstate' field if paper is really published")
            elif not pub_data.get('pubstate'):
                self.notifications.append(f"{pub_path}: consider adding 'pubstate' field for unpublished paper (date is not set)")

    def check_coherence_between_files(self, en_data: Dict, de_data: Dict, bib_data: Dict, pub_path: Path) -> None:
        """Check coherence between English, German, and BibTeX files."""
        # Valid BibTeX fields from archetype
        valid_bib_fields = {
            'author', 'title', 'subtitle', 'year', 'journal', 'booktitle', 'editor', 'translator', 'series',
            'volume', 'number', 'pages', 'chapter', 'edition', 'eventtitle', 'date', 'type', 'pubstate', 'publisher',
            'location', 'institution', 'school', 'doi', 'isbn', 'issn', 'url', 'abstract', 'keywords',
            'pagetotal', 'language', 'note'
        }
        unchecked_bib_fields = valid_bib_fields

        if not bib_data:
            self.errors.append(f"{pub_path}: BibTeX file is empty!")
        else:
            if self.normalize(bib_data.get('bib_key')) != self.normalize(pub_path.name):
                self.notifications.append(f"{pub_path}: BibTeX key ({bib_data.get('bib_key')}) does not match publications abbreviation ({pub_path.name})")
            if VALID_PUBLICATION_TYPES.get(bib_data.get('bib_type').lower()) != en_data.get('publication_types')[0] and en_data.get('publication_types')[0] != 'review':
                self.errors.append(f"{pub_path}: BibTeX publication type ({bib_data.get('bib_type')} --> {VALID_PUBLICATION_TYPES.get(bib_data.get('bib_type').lower())}) does not match publications type ({en_data.get('publication_types')[0]})")

            # Check that BibTeX only contains valid fields
            invalid_bib_fields = set(bib_data.keys()) - {'bib_type', 'bib_key'} - valid_bib_fields
            if invalid_bib_fields:
                self.warnings.append(f"{pub_path}: BibTeX contains ignored fields: {', '.join(sorted(invalid_bib_fields))}")

        # Fields that must be exactly the same between EN and DE
        exact_match_fields: set[str] = {'authors', 'editors', 'translators', 'publishDate', 'publication_types', 'volume', 'number', 'pages', 'chapter', 'pubstate', 'database', 'defenseDate', 'language', 'pagetotal', 'doi', 'isbn', 'issn', 'featured', 'projects'
                              } | {'url_pdf', 'url_code', 'url_dataset', 'url_poster', 'url_project', 'url_slides', 'url_source', 'url_video'
                              } | {'publication_short', 'journal_short', 'publisher_short'}
        # Fields that are compared with custom rules
        individual_fields: set[str] = {'authors', 'author', 'editors', 'editor', 'translators', 'translator', 'tags', 'keywords', 'sub_type', 'type', 'year', 'date', 'links', 'url', 'image'}
        # Fields that are expected to be translated
        expected_translation_fields: set[str] = {'title', 'subtitle', 'summary', 'author_notes', 'booktitle', 'edition', 'type', 'note', 'abstract', 'tags'}
        # Fields that are expected to be translated and the original shall be contained (in brackets)
        original_translation: set[str] = {'title', 'subtitle', 'booktitle', 'series', 'eventtitle'}

        # Check that both English and German versions contain the same parameters (keys)
        en_keys = set(en_data.keys())
        de_keys = set(de_data.keys())
        # Check if all bib fields are present in MD files
        missing_md_keys = set(bib_data.keys()) - (en_keys | de_keys) - {'bib_type', 'bib_key'} - individual_fields

        if en_keys != de_keys:
            if missing_in_en := de_keys - en_keys:
                self.errors.append(f"{pub_path}: Parameters missing in English version: \'{'\', \''.join(sorted(missing_in_en))}\'")
            if missing_in_de := en_keys - de_keys:
                self.errors.append(f"{pub_path}: Parameters missing in German version: \'{'\', \''.join(sorted(missing_in_de))}\'")
        if missing_md_keys:
            self.errors.append(f"{pub_path}: Parameters from BibTeX missing in MD files: \'{'\', \''.join(sorted(missing_md_keys))}\'")

        # Check exact match fields
        for field in exact_match_fields:
            if field in en_data and field in de_data:
                if en_data[field] != de_data[field]:
                    self.errors.append(f"{pub_path}: Field '{field}' differs between EN and DE versions ({en_data[field]} != {de_data[field]})")
                if field in valid_bib_fields and en_data[field] != bib_data.get(field, ''):
                    self.errors.append(f"{pub_path}: Field '{field}' differs between MD and BibTeX versions ({en_data[field]} != {bib_data.get(field)})")
                elif en_data[field] is None:
                    self.warnings.append(f"{pub_path}: Field '{field}' has None value (initialized but not declared)")
            elif bib_data.get(field):
                self.errors.append(f"{pub_path}: Field '{field}' is missing from EN MD file ({bib_data.get(field)} in BibTeX)")
        unchecked_bib_fields -= exact_match_fields

        # Check individual fields
        for list_type in ['authors', 'editors', 'translators']:
            list = en_data.get(list_type) or de_data.get(list_type)
            if list:
                if not bib_data.get(list_type[:-1]):
                    self.errors.append(f"{pub_path}: Field '{list_type[:-1]}' is missing from BibTeX file ({list})")
                else:
                    md_person = {author.lower().replace(' ', '.') for author in list}
                    bib_person = {f"{author.split(', ')[-1].lower()}.{author.split(', ')[0].lower()}" for author in bib_data.get(list_type[:-1]).split(' and ')}
                    if md_person != bib_person:
                        self.errors.append(f"{pub_path}: Field '{list_type[:-1]}' mismatch: MD {md_person - bib_person} vs BibTeX {bib_person - md_person}")
            elif bib_data.get(list_type[:-1]):
                self.errors.append(f"{pub_path}: Field '{list_type[:-1]}' is missing from en/de MD file ({bib_data.get(list_type[:-1])})")
        unchecked_bib_fields -= {'author', 'editor', 'translator'}

        # Check Year
        if not bib_data.get('year') and en_data.get('date'):
            self.errors.append(f"{pub_path}: Field 'year' is missing from BibTeX file")
        elif en_data.get('date', '    ')[:4] != bib_data.get('year', '    '):
            self.errors.append(f"{pub_path}: MD 'date' and BibTeX 'year' differ ({en_data['date']} != {bib_data['year']})")
        if en_data.get('date') != de_data.get('date'):
            self.errors.append(f"{pub_path}: 'date' differs between EN and DE MD versions ({en_data['date']} != {de_data['date']})")
        elif bib_data.get('date') and en_data.get('date') != bib_data.get('date'):
            self.errors.append(f"{pub_path}: 'date' differs between MD and BibTeX ({en_data.get('date')} != {bib_data['date']})")
        elif en_data.get('date') and not re.match(r'\d{4}-01-01.*', en_data.get('date')) and en_data.get('date') != bib_data.get('date'):
            self.errors.append(f"{pub_path}: MD 'date' ({en_data['date']}) is missing in BibTeX ({bib_data.get('date')})")
        unchecked_bib_fields -= {'year', 'date'}

        # Check links URLs
        if 'links' in en_data and 'links' in de_data:
            en_links = en_data['links']
            de_links = de_data['links']

            if len(en_links) != len(de_links):
                self.errors.append(f"{pub_path}: Different number of links in en/de MD versions")
            else:
                if 'url' in bib_data.keys():
                    bib_match_found = False
                else:
                    bib_match_found = True
                    if len(en_links) >= 1:
                        self.errors.append(f"{pub_path}: BibTeX URL is missing (MD contains {len(en_links)} links)")
                for i, (en_link, de_link) in enumerate(zip(en_links, de_links)):
                    if not bib_match_found and en_link.get('url') == bib_data['url']:
                        bib_match_found = True
                    if en_link.get('url') != de_link.get('url'):
                        self.errors.append(f"{pub_path}: {i}. Link URL differs between EN and DE versions")
                    elif en_link.get('icon') != de_link.get('icon'):
                        self.errors.append(f"{pub_path}: {i}. Link icon differs between EN and DE versions")
                if not bib_match_found:
                    self.errors.append(f"{pub_path}: BibTeX URL ({bib_data['url']}) differs from MD links")
        unchecked_bib_fields.remove('url')

        # Check image filenames
        if 'image' in en_data and 'image' in de_data:
            en_image = en_data['image'].get('filename', '')
            de_image = de_data['image'].get('filename', '')

            if en_image.replace(".en.", ".de.") != de_image:
                self.errors.append(f"{pub_path}: Images differs between EN and DE versions ({en_image} != {de_image})")
            # elif not (en_image or de_image) and not ((pub_path / "featured.jpg").exists() or (pub_path / "featured.png").exists()):
            #     self.warnings.append(f"{pub_path}: Image is declared but doesn't link to a file in {'german' if en_image else 'english'} version")
            elif (en_image or de_image) and ((pub_path / "featured.jpg").exists() or (pub_path / "featured.png").exists()):
                self.errors.append(f"{pub_path}: There is a featured image but another one is referenced in {'german' if en_image else 'english'} version")

        # Check (main) language
        lang = ''
        if en_data.get('language') and de_data.get('language'):
            if en_data['language'] == de_data['language']:
                lang = en_data['language'].lower()
            else:
                self.errors.append(f"{pub_path}: 'language' field is different in EN and DE MD versions")
        elif en_data.get('language') or de_data.get('language'):
            lang = (en_data.get('language') or de_data.get('language')).lower()
            self.errors.append(f"{pub_path}: 'language' field is missing in {'german' if en_data.get('language') else 'english'} MD version")
        if bib_data.get('language') and lang:
            if bib_data['language'].lower() != lang:
                lang = ''
                self.errors.append(f"{pub_path}: BibTeX language ({bib_data['language']}) does not match publications language ({lang})")
        elif bib_data.get('language') or lang:
            self.errors.append(f"{pub_path}: 'language' field is missing in {'BibTeX' if lang else 'MD'}")
            lang = lang or bib_data.get('language')
        de_count, en_count = ((100, 0) if lang == 'german' else (0, 100)) if lang else (0, 0)

        # Check translation
        for field in original_translation:
            en_val = self.normalize(en_data.get(field))
            de_val = self.normalize(de_data.get(field))
            if en_val and de_val:
                if lang:
                    original, translation = (en_val, de_val) if lang == 'english' else (de_val, en_val)
                    if original not in translation:
                        # TODO: maybe check if majority of split (word list) is contained
                        self.errors.append(f"{pub_path}: The original {lang} '{field}' ({(de_data if lang == 'german' else en_data)[field]}) is not named in the {'german' if lang == 'english' else 'english'} translation")
                else:
                    if en_val not in de_val and de_val not in en_val:
                        self.errors.append(f"{pub_path}: Field '{field}' is not properly translated between EN and DE versions - the original {field} is not stated in the translation")
                        en_kept = sum(1 for word in en_val.split() if word in de_val)
                        de_kept = sum(1 for word in de_val.split() if word in en_val)
                        if en_kept >= de_kept:
                          en_count += 1
                        else:
                          de_count += 1
                    else:
                        de_count += de_val in en_val
                        en_count += en_val in de_val

        # Determine probable original language if not specified
        if not lang and en_count/(en_count+de_count) > 0.65:
            lang = "english"
            self.warnings.append(f"{pub_path}: EN version is mostly translated, consider setting 'language' field to 'english'")
        elif not lang and de_count/(en_count+de_count) > 0.65:
            lang = "german"
            self.warnings.append(f"{pub_path}: DE version is mostly translated, consider setting 'language' field to 'german'")
        elif not lang: lang = "english"

        missed_translations = {f for f in expected_translation_fields if en_data.get(f) and en_data.get(f) == de_data.get(f)}
        if missed_translations and lang == 'german':
            self.errors.append(f"{pub_path}: The following fields are not translated at all: {', '.join({f"{f} ({en_data.get(f)})" for f in missed_translations})}")

        # Determine which language to use for BibTeX comparison
        source_data = en_data if lang.startswith('eng') else de_data

        # Check tags/keywords
        if source_data.get('tags') and bib_data.get('keywords'):
            tags, keywords = {self.normalize(t, repl=' ') for t in source_data['tags']}, {self.normalize(k, repl=' ') for k in bib_data['keywords'].split(", ")}
            if tags != keywords:
                if tags - keywords:
                    self.warnings.append(f"{pub_path}: Some tags ({', '.join(tags - keywords)}) from the MD frontmatter are missing in BibTeX 'keywords' ({', '.join(keywords)})")
                if keywords - tags:
                    self.errors.append(f"{pub_path}: Some keywords ({', '.join(keywords - tags)}) from the BibTeX are missing as MD frontmatter 'tags' ({', '.join(tags)})")
        elif bib_data.get('keywords'):
            self.errors.append(f"{pub_path}: 'tags' field is missing in 'MD'")
        elif source_data.get('tags'):
            self.notifications.append(f"{pub_path}: 'tags' from MD {source_data.get('tags')} might be added as 'keywords' in 'BibTeX'")
        unchecked_bib_fields.remove('keywords')

        # Check publication sub/descriptive type
        md_type, bib_subtype = self.normalize(source_data.get('sub_type')), self.normalize(bib_data.get('type'))
        if source_data.get('publication_types')[0] and source_data.get('publication_types')[0] == 'review':
            if source_data.get('sub_type') != VALID_PUBLICATION_TYPES.get(bib_data.get('bib_type').lower()):
                self.errors.append(
                    f"{pub_path}: The publication type ({VALID_PUBLICATION_TYPES.get(bib_data.get('bib_type').lower())} for {bib_data.get('bib_type')}) should be specified in the MD frontmatter 'sub_type' (current: {md_type}) to ensure correct citation for reviews")
        elif source_data.get('publication_types')[0] and source_data.get('publication_types')[0] == 'thesis':
            if bib_data.get('bib_type').lower() == 'phdthesis':
                if source_data.get('sub_type') != ('Doctoral Dissertation' if lang == 'english' else 'Doktorarbeit'):
                    self.errors.append(f"{pub_path}: The dissertation `sub_type` should be {'Doctoral Dissertation' if lang == 'english' else 'Doktorarbeit'} instead of {source_data.get('sub_type')} in the MD frontmatter")
            elif bib_data.get('bib_type').lower() == 'masterthesis':
                if source_data.get('sub_type') != ('Masters Thesis' if lang == 'english' else 'Masterarbeit'):
                    self.errors.append(f"{pub_path}: The thesis `sub_type` should be {'Masters Thesis' if lang == 'english' else 'Masterarbeit'} instead of {source_data.get('sub_type')} in the MD frontmatter")
            elif source_data.get('sub_type') != bib_data.get('bib_type'):
                self.errors.append(f"{pub_path}: The thesis `sub_type` ({source_data.get('sub_type')}) should match the descriptive type in BibTeX ({bib_data.get('type')})")
        else:
            if md_type and bib_subtype:
                if md_type != bib_subtype:
                    self.errors.append(f"{pub_path}: The publications subtype differs between MD frontmatter ({md_type}) and BibTeX 'type' ({bib_subtype})")
            elif bib_data.get('type'):
                self.errors.append(f"{pub_path}: 'sub_type' field is missing in 'MD'")
            elif md_type:
                self.notifications.append(f"{pub_path}: 'sub_type' from MD {md_type} might be added as 'type' in 'BibTeX'")
        unchecked_bib_fields.remove('type')

        for field in unchecked_bib_fields:
            pub_val = source_data.get(field)
            bib_val = bib_data.get(field)
            if pub_val and bib_val:
                pub_str = self.normalize(pub_val, r'[^\w\säöüß]', '')
                bib_str = self.normalize(bib_val, r'[^\w\säöüß]', '')
                if pub_str != bib_str and len(pub_str) < 700:
                    self.warnings.append(f"{pub_path}: Field '{field}' differs between frontmatter and BibTeX ({pub_val} != {bib_val})")
            elif (pub_val or bib_val) and len(pub_val or '') < 700:
                self.warnings.append(f"{pub_path}: Field '{field}' is {'missing' if (field not in source_data) or (field not in bib_data) else 'empty'} from {'BibTeX' if pub_val else 'MD frontmatter'}")

        remaining_fields = (en_keys | de_keys) - set(exact_match_fields) - individual_fields
        missing_de = {f for f in remaining_fields if en_data.get(f) and not de_data.get(f)}
        if missing_de:
            self.errors.append(f"{pub_path}: The following fields are missing a german translation/version: {', '.join({f"{f} ({en_data.get(f)})" for f in missing_de})}")
        missing_en = {f for f in remaining_fields if not en_data.get(f) and de_data.get(f)}
        if missing_en:
            self.errors.append(f"{pub_path}: The following fields are missing an english translation/version: {', '.join({f"{f} ({de_data.get(f)})" for f in missing_en})}")

        self.ignored_proper_translation = self.ignored_proper_translation | (remaining_fields - expected_translation_fields)

    def validate_publication(self, pub_dir: Path) -> None:
        """Validate a single publication directory."""
        en_file = pub_dir / 'index.en.md'
        de_file = pub_dir / 'index.de.md'
        bib_file = pub_dir / 'cite.bib'

        if not en_file.exists():
            self.errors.append(f"{pub_dir}: Missing index.en.md")
            return
        if not de_file.exists():
            self.errors.append(f"{pub_dir}: Missing index.de.md")
            return
        if not bib_file.exists():
            self.errors.append(f"{pub_dir}: Missing cite.bib")
            return

        # Load all files
        en_data = self.load_yaml_frontmatter(en_file)
        de_data = self.load_yaml_frontmatter(de_file)
        bib_data = self.load_bib_file(bib_file)

        # Run all checks
        self.check_null_values(en_data, pub_dir)
        self.check_publication_types(en_data, pub_dir)
        self.check_date_parameter(en_data, pub_dir)
        self.check_type_specific_requirements(en_data, pub_dir)
        self.check_address_location_consistency(en_data, pub_dir)
        self.check_short_parameters(en_data, pub_dir)
        self.check_publication_parameter(en_data, pub_dir)
        self.check_author_exists(en_data, pub_dir)
        self.check_pubstate_parameter(en_data, pub_dir)
        self.check_links(en_data, pub_dir)

        self.check_coherence_between_files(en_data, de_data, bib_data, pub_dir)

    @staticmethod
    def print_results(errors, warnings, notifications) -> None:
        """Print validation results."""
        print(f"Publication Validation Results")
        print(f"=" * 40)

        if errors:
            print(f"\n❌ ERRORS ({len(errors)}):")
            for error in sorted(errors):
                print(f"  • {error}")
        else:
            print(f"\n✅ No errors found!")

        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for warning in sorted(warnings):
                print(f"  • {warning}")

        if notifications:
            print(f"\n📣 NOTIFICATIONS ({len(notifications)}):")
            for notification in sorted(notifications):
                print(f"  • {notification}")

        print(f"\n📊 Summary: {len(errors)} errors, {len(warnings)} warnings, {len(notifications)} notifications")

    def validate_all(self) -> int:
        """Validate all publications and return errors and warnings."""
        publications_dir = self.work_dir / 'content' / 'publication'
        if not publications_dir.exists():
            self.errors.append(f"Publications directory {publications_dir} does not exist")
        else:
            i = 0
            for pub_dir in publications_dir.iterdir():
                if pub_dir.is_dir():
                    self.validate_publication(pub_dir)
                    i += 1
            print(f"Checked {i} publications")

        if self.ignored_proper_translation:
            self.notifications.append(f"A proper translation has not been checked on: {', '.join(self.ignored_proper_translation)}")

        self.print_results(self.errors, self.warnings, self.notifications)

        return len(self.errors) == 0



def main():
    """Main function."""
    work_dir = Path(__file__).parent.parent

    validator = PublicationValidator(work_dir)
    success = validator.validate_all()

    exit(0 if success else 1)


if __name__ == '__main__':
    main()
