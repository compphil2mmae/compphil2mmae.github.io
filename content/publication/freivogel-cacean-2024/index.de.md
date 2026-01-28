---
title: 'Assessing a Formal Model of Reflective Equilibrium (Bewertung eines formalen Modells des reflektiven Gleichgewichts)'

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

abstract: 'In der Philosophie, insbesondere in der Ethik, gilt das reflektive Gleichgewicht (Reflective Equilibrium - RE) oft als wirkungsvolle Methode zur Gewinnung von sich gegenseitig stützenden Überzeugungen, die durch Evidenz gerechtfertigt und durch gute Gründe gestützt sind.
Beisbart, Betz und Brun ([2021](https://re-models.github.io/re-technical-report/references.html#ref-beisbart_making_2021)) haben ein formales Modell des reflektiven Gleichgewichts eingeführt, das auf der Theorie dialektischer Strukturen von Betz ([2013](https://re-models.github.io/re-technical-report/references.html#ref-betz_debate_2013)) basiert und als methodologisches Werkzeug zum besseren Verständnis der Methode des reflektiven Gleichgewichts dient.


Dieser Bericht ist ein Ergebnis des Forschungsprojekts „*Wie weit bringt uns das reflektive Gleichgewicht? Untersuchung der Leistungsfähigkeit einer philosophischen Methode*“ ([How far does Reflective Equilibrium Take us? Investigating  the Power of a Philosophical Method](https://re-models.github.io/)) und fasst die Ergebnisse einer gründlichen Bewertung des Modells durch numerische Untersuchung zusammen. Wir simulieren RE-Prozesse für ein breites Spektrum von Modellparametern und Anfangsbedingungen und verwenden vier verschiedene Modellvarianten (einschließlich des ursprünglichen Modells). Wir analysieren die Abhängigkeit der Simulationsergebnisse von verschiedenen Parametern und bewerten die Eignung der Modelle hinsichtlich ihrer Konsistenz und ihrer Fähigkeit, globale Optima und volle RE-Zustände zu erreichen.


Die Ergebnisse zeigen, dass das Verhalten der Modelle entscheidend von den Besonderheiten des Simulationsaufbaus abhängt (z.B. der Größe des Satzpools und den Gewichten). Wir können daher keine allgemeinen Schlussfolgerungen über die Gesamtleistung der Modellvarianten ziehen. Vielmehr müssen die Besonderheiten des Kontexts, in dem ein RE-Modell verwendet wird, bei der Wahl eines bestimmten Modells berücksichtigt werden. Abschließend identifizieren wir einige kritische Wissenslücken, die wir mit diesem Bericht nicht schließen können und die weitere Forschung in der RE-Modellierung erfordern.


(*Originalsprache Englisch*)'

# Summary. An optional shortened abstract.
summary: 'In der Philosophie und insbesondere in der Ethik wird das reflektierte Gleichgewicht (Reflective Equilibrium, RE) oft als eine wirkungsvolle Methode angesehen, um zu Überzeugungen zu gelangen, die sich gegenseitig stützen, durch Beweise gerechtfertigt sind und durch gute Gründe untermauert werden. Basierend auf Beisbart, Betz und Brun (2021) bewertet dieser Bericht formale RE-Modelle durch numerische Untersuchungen, um die Methode zu hinterfragen und weiterzuentwickeln.'

tags:
- Reflektives Gleichgewicht
- Philosophische Methode
- Rawls
- Formale Erkenntnistheorie
- Formale Methoden
- Moralische Argumentation
- Modellierung

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

## Haupterkenntnisse
- **Umfassende Modellbewertung**: Erste gründliche numerische Untersuchung des formalen RE-Modells anhand mehrerer Validierungskriterien (globale Optima, vollständige RE-Zustände, Konsistenz)
- **Variantenanalyse**: Systematische Analyse von vier verschiedenen Modellvarianten, darunter das ursprüngliche Beisbart-Betz-Brun-Modell
- **Kontextabhängige Ergebnisse**: Keine allgemeinen Schlussfolgerungen zur Gesamtleistung der Modellvarianten möglich – jedes Modell erfüllt die Validierungskriterien nur innerhalb bestimmter Simulationskonfigurationen
- **Konsistenzförderlichkeit**: Alle Modellvarianten weisen eine zufriedenstellend hohe Konsistenzleistung auf; LinearLocalRE schneidet bei zunehmender Satzpoolgröße am besten ab
- **Parametersensitivität**: Die Modellleistung ist sehr empfindlich gegenüber α-Gewichtungskonfigurationen; spezifische „Kipplinien” in linearen Modellen markieren grundlegend unterschiedliche Verhaltensbereiche

## Forschungsbeiträge
- **Methodische Innovation**: Etablierung eines umfassenden Bewertungsrahmens für formale philosophische Modelle unter Verwendung numerischer Untersuchungen anhand mehrerer Validierungskriterien
- **Empirische Grundlage**: Erste systematische numerische Untersuchung des formalen RE-Modells auf der Grundlage der Theorie dialektischer Strukturen mit vier Modellvarianten
- **Kontextbewusste Modellierung**: Nachweis, dass die Auswahl des RE-Modells einen Ausgleich zwischen Konsistenz, Erreichbarkeit globaler Optima und vollständigen RE-Zuständen innerhalb spezifischer Kontexte erfordert
- **Analytische Erkenntnisse**: Identifizierung des „Tipping-Line”-Phänomens in linearen Modellen und Bereitstellung analytischer Erklärungen für Verhaltensübergänge
- **Forschungsfahrplan**: Skizzierung wichtiger zukünftiger Forschungsrichtungen, darunter Optimierung der Nachbarschaftstiefe, alternative Systematikmaße und inferentielle Dichteanalyse
- **Praktischer Rahmen**: Bereitstellung einer evidenzbasierten Methodik für die kontextspezifische Modellauswahl auf der Grundlage von α-Gewichtskonfigurationen und Satzpoolgrößen

## Publikationsdetails
- **Seiten**: 168
- **Verlag**: Zenodo
- **Publikationsdatum**: 11. August 2024
- **DOI**: [10.5281/zenodo.13294165](https://doi.org/10.5281/zenodo.13294165)
- **Projekt**: „Wie weit führt uns das reflektive Gleichgewicht? Untersuchung der Leistungsfähigkeit einer philosophischen Methode“ ([How far does Reflective Equilibrium Take us? Investigating  the Power of a Philosophical Method](https://re-models.github.io/))
