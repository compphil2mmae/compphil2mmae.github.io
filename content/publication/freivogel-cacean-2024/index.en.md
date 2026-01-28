---
title: Assessing a Formal Model of Reflective Equilibrium

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Andreas Freivogel
- sebastian.cacean

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-08-11'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-01-28T00:31:02.812260Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- report

# Publication name and optional abbreviated publication name.
publication: '*Zenodo*'
publication_short: ''

publisher: Zenodo

language: english
pagetotal: 168

doi: 10.5281/zenodo.13294165

abstract: "In philosophy, and especially in ethics, reflective equilibrium (RE) is often considered a powerful method for obtaining beliefs that mutually support each other, are justified by evidence, and are backed by good reasons.
Beisbart, Betz, and Brun ([2021](https://re-models.github.io/re-technical-report/references.html#ref-beisbart_making_2021)) have introduced a formal model of reflective equilibrium based on the theory of dialectical structures Betz ([2013](https://re-models.github.io/re-technical-report/references.html#ref-betz_debate_2013)), which they use as a methodological tool to understand the method of reflective equilibrium better.


This report is an outcome of the research project '[How far does Reflective Equilibrium Take us? Investigating  the Power of a Philosophical Method](https://re-models.github.io/)' and summarizes the findings of assessing the model thoroughly by numerical investigation. We simulate RE processes for a broad
  spectrum of model parameters and initial conditions and use four different model
  variants (including the original model). We analyze the dependence of simulation
  results on different parameters and assess the models' conduciveness towards consistency,
  and ability to reach global optima and full RE states.
  

The results show that the
  models' behavior depends crucially on the specifics of the simulation setup. We
  can, therefore, not draw any general conclusions about the overall performance of
  the model variants. Rather, the specifics of the context in which an RE model is
  used must be considered to choose a specific model. Finally, we identify some critical
  knowledge gaps we cannot close with this report that call for further research into
  RE modelling."

# Summary. An optional shortened abstract.
summary: 'In philosophy, and especially in ethics, reflective equilibrium (RE) is often considered a powerful method for obtaining beliefs that mutually support each other, are justified by evidence, and are backed by good reasons. Based on Beisbart, Betz, and Brun (2021), this report assesses formal RE models by numerical investigation to scrutinize and advance the method.'

tags:
- Reflective equilibrium
- Philosophical method
- Rawls
- Formal epistemology
- Formal methods
- Moral reasoning
- Modelling

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'https://re-models.github.io/'
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
links:
- name: Report
  icon: file-lines
  url: https://re-models.github.io/re-technical-report/
- name: PDF
  icon: file-pdf
  url: Assessing-a-Formal-Model-of-Reflective-Equilibrium.pdf
- name: Code
  icon: file-code
  url: https://github.com/re-models/re-technical-report
#- name: Zenodo  # acadmicon seems faulty and is already covered by doi
#  icon: zenodo
#  icon_pack: ai
#  url: https://zenodo.org/records/13294165
- name: Philpapers
  icon: philpapers
  icon_pack: ai
  url: https://philpapers.org/rec/FREAAF-3

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  filename: 'uploads/zenodo-logo.png'
  alt: 'Zenodo Logo'
  caption: 'Zenodo - Open Science Repository'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [DFG_RE]
---

## Key Findings
- **Comprehensive Assessment**: First thorough numerical investigation of the formal RE model across multiple validation criteria (global optima, full RE states, consistency)
- **Model Variant Comparison**: Systematic analysis of four different model variants including the original Beisbart-Betz-Brun model
- **Context-Dependent Results**: No general conclusions possible about overall model variant performance - each model meets validation criteria only within specific simulation setups
- **Consistency Conduciveness**: All model variants show satisfactorily high consistency performance; LinearLocalRE performs best with increasing sentence pool sizes
- **Full RE States**: Relative share of full RE states among global optima and fixed points is rather low across all model variants
- **Parameter Sensitivity**: Model performance highly sensitive to α-weight configurations; specific "tipping lines" in linear models mark fundamentally different behavioral regions

## Research Contributions
- **Methodological Innovation**: Established comprehensive assessment framework for formal philosophical models using numerical investigation across multiple validation criteria
- **Empirical Foundation**: First systematic numerical investigation of the RE formal model based on dialectical structures theory with four model variants
- **Context-Aware Modeling**: Demonstrated that RE model selection requires balancing trade-offs between consistency, global optima reachability, and full RE states within specific contexts
- **Analytical Insights**: Identified "tipping line" phenomenon in linear models and provided analytical explanations for behavioral transitions
- **Research Roadmap**: Outlined critical future research directions including neighborhood depth optimization, alternative systematicity measures, and inferential density analysis
- **Practical Framework**: Provided evidence-based methodology for context-specific model selection based on α-weight configurations and sentence pool sizes

## Publication Details
- **Pages**: 168
- **Publisher**: Zenodo
- **Publication Date**: August 11, 2024
- **DOI**: [10.5281/zenodo.13294165](https://doi.org/10.5281/zenodo.13294165)
- **Project**: '[How far does Reflective Equilibrium Take us? Investigating the Power of a Philosophical Method](https://re-models.github.io/)'
