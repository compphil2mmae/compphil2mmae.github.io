---
title: 'Titel der Publikation (Übersetzung des Titels, falls englisch)'
subtitle: ''  # optional subtitle

# A YAML list of author names
# If author has an own page at `content/authors/prename.name`, use prename.name instead of `Prename Name`
authors:
  - prename.name
  - External Autor

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list, displayed on (i) hover
author_notes: []

# Date of the publication
date: {{ now.Format "2006-01-02" }}
# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: {{ now.Format "2006-01-02" }}

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements). Compare to /data/publication_types.yaml.
# Remove/Comment out the others.
publication_types:
#  - uncategorized
#  - conference-paper  # Conference/@inproceedings paper
  - article-journal  # Journal/@article paper
#  - preprint  # Preprint/Working Paper/@unpublished paper
#  - report  # @report/@techreport
#  - book  # @book/@proceedings/@booklet/@manual
#  - chapter  # Book section/Chapter as @inbook/@incollection
#  - thesis  # @thesis/@phdthesis/@masterthesis
#  - patent  # @patent
#  - review  # of some other type (specify in 'type'-parameter) but to list separately

# Article
journal: ''
journal_short: ''
series: ''
volume: ''
number: ''
pages: ''  # e.g. '63--77'

# Book or chapter
booktitle: ''  # for chapter, 
chapter: ''
edition: ''
editors: []
translators: []

publisher: '*Karlsruher Institut für Technologie*'
publisher_short: 'KIT'
school: ''  # '*Karlsruher Institut für Technologie*'  # for thesis
institution: ''  # for report and other
address: ''
location: 'Karlsruhe'
database: ''  # for thesis apa citation
eventtitle: ''  # for conference paper
sub_type: ''  # descriptive subtype (e.g. "PhD thesis", "Technical Report") or actual publication type for reviews
pubstate: ''  # publication state, 'inpreparation', 'submitted', 'forthcoming', 'inpress', 'prepublished', 'published' are translated (used by biblatex https://latex.org.uk/info/translations/biblatex/de/biblatex-de-Benutzerhandbuch.pdf)

defenseDate: ''  # for thesis
language: english  # Language of the publication [english, german]
pagetotal: ''

note: ''  # for "In Progress." use pubstate inpress

doi: ''
isbn: ''
issn: ''

abstract: ''

# Summary. An optional shortened abstract to display in previews or list views.
summary: ""

tags: []  # existing tags can be found at /public/tag/...
featured: false  # to feature this on the landingpage, add the tag 'highlight'

# Custom links (optional). Cite & DOI Links are auto generated if specified
links:
#- name: Report  # required for publication_type: report
#  icon: file-lines
#  url: https://re-models.github.io/re-technical-report/  # Link to (a web view of) the paper
- name: PDF
  icon: file-pdf
  url: Title-of-the-publication.pdf  # add the pdf file to the folder of the publication
#- name: Code
#  icon: file-code
#  url: https://github.com/re-models/re-technical-report  # Link to a public code repository
- name: URL  # name required for citation
  icon: open-access  #/closed-access if no more specific icon, e.g. springer from https://jpswalsh.github.io/academicons/ is applicable
  icon_pack: ai
  url: https://publikationen.bibliothek.kit.edu/1000028245  # where to find the publication online/link to the publishers website
#- name: Book
#  icon: book
#  icon_pack: fas
#  url: https://katalog.bibliothek.kit.edu/cgi-bin/koha/opac-detail.pl?biblionumber=1444370  # for external information about the book/publication (not direct access)
- name: Philpapers
  icon: philpapers
  icon_pack: ai
  url: https://philpapers.org/rec/GREEAO-4  # Philpapers entry
#- name: Projekt
#  icon: folder-tree
#  icon_pack: fas
#  url: https://re-models.github.io/  # External project page

# Featured image
# To use, put the publications cover under /assets/media/covers/, add an image to the publication bundle/folder and reference it or name it `featured.jpg/png`.
image:
#  filename: '/covers/Title-of-the-publication.jpg'  # references to /assets/media/covers/ (or place and link to image in publications folder)
#  alt: 'Cover - <Publications Title>'
#  caption: ''
#  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name (slug) without extension (no translation or other change, case-sensitive!).
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
---
