---
title: 'Probing Practical Deliberation in LLMs'
subtitle: 'A Proof Of Concept'  # optional subtitle

# A YAML list of author names
# If author has an own page at `content/authors/prename.name`, use prename.name instead of `Prename Name`
authors:
  - gregor.betz
  - christian.seidel

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list, displayed on (i) hover
author_notes: []

# Date of the publication
date: 2025-07-17
# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: 2025-07-17

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements). Compare to /data/publication_types.yaml.
# Remove/Comment out the others.
publication_types:
#  - uncategorized
#  - conference-paper  # Conference/@inproceedings paper
#  - article-journal  # Journal/@article paper
#-  - preprint  # Preprint/Working Paper/@unpublished paper
  - report  # @report/@techreport
#  - book  # @book/@proceedings/@booklet/@manual
#  - chapter  # Book section/Chapter as @inbook/@incollection
#  - thesis  # @thesis/@phdthesis/@masterthesis
#  - patent  # @patent
#  - review  # of some other type (specify in 'type'-parameter) but to list separately

# Report
publisher: 'GitHub'
edition: 'v.0.1.0'

defenseDate: ''  # for thesis
language: english  # Language of the publication [english, german]
pagetotal: ''

note: ''  # for "In Progress." use pubstate inpress

doi: ''
isbn: ''
issn: ''

abstract: "In this repository, we're exploring how to probe the ability of large language models (LLMs) to engage in practical deliberation. In the main notebook, we're testing whether an LLM's all-things-considered judgements in decision situations from the kellycyy/daily_dilemmas dataset are in fact insensitive to invariance transformations, such as strengthen the reasons in favor of the preferred options. We conceive of this as a proof of concept, which is meant to demonstrate the feasibility of a more comprehensive computational investigation; as work in progress, so feedback and contributions are welcome; as a preliminary experimental setup, which is meant to be adapted and extended for further research on practical deliberation in LLMs."

# Summary. An optional shortened abstract to display in previews or list views.
summary: "In this repository, we're exploring how to probe the ability of large language models (LLMs) to engage in practical deliberation."

tags: []  # existing tags can be found at /public/tag/...
featured: false  # to feature this on the landingpage, add the tag 'highlight'

# Custom links (optional). Cite & DOI Links are auto generated if specified
links:
#- name: Report  # required for publication_type: report
#  icon: file-lines
#  url: https://re-models.github.io/re-technical-report/  # Link to (a web view of) the paper
# - name: PDF
#   icon: file-pdf
#   url: Title-of-the-publication.pdf  # add the pdf file to the folder of the publication
#- name: Code
#  icon: file-code
#  url: https://github.com/re-models/re-technical-report  # Link to a public code repository
- name: URL  # name required for citation
  icon: open-access  #/closed-access if no more specific icon, e.g. springer from https://jpswalsh.github.io/academicons/ is applicable
  icon_pack: ai
  url: https://github.com/debatelab/practical-deliberation-llms  # where to find the publication online/link to the publishers website
#- name: Book
#  icon: book
#  icon_pack: fas
#  url: https://katalog.bibliothek.kit.edu/cgi-bin/koha/opac-detail.pl?biblionumber=1444370  # for external information about the book/publication (not direct access)
#- name: Philpapers
#  icon: philpapers
#  icon_pack: ai
#  url: https://philpapers.org/rec/GREEAO-4  # Philpapers entry
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
projects: ['phil_llms']
---
