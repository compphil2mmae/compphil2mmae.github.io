---
title: 'Polarisation, Diversity, and Dialectical Structures (Polarisierung, Diversität und dialektische Strukturen)'
subtitle: 'An Argumentation-Based Approach to Computational Social Epistemology (Ein argumentationsbasierter Ansatz zur computergestützten sozialen Erkenntnistheorie)'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- felix.kopecky

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-08-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-12-27T22:31:43.930940Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- thesis

# Publication name and optional abbreviated publication name.
publication: 'KIT'
publication_short: ''
publisher: 'Karlsruher Institut für Technologie (KIT)'
address: 'Karlsruhe'

doi: '10.5445/IR/1000183401'

# double line break needed for correct markdown rendering
abstract: "Diese Dissertation befasst sich mit der Untersuchung von Glaubenspolarisierung und Meinungsvielfalt in agentenbasierten Computermodellen. Simulationen dieser Modelle zeigen, dass sich die Überzeugungen künstlicher Agenten durch Deliberation polarisieren können – selbst wenn alle Agenten eine produktive Denkweise haben und sich an Standards epistemischer Rationalität halten. Unterschiedliche deliberative Praktiken wirken sich in diesen Modellen unterschiedlich auf die Polarisierungsdynamik aus. Die Polarisierungsdynamik wird gemildert, wenn Agenten die Überzeugungen anderer in ihre Überlegungen einbeziehen. Der größte Polarisierungseffekt wird bei Agenten beobachtet, die ihre eigenen Überzeugungen kontinuierlich festigen.

Ein zweites Ergebnis ist, dass, wenn künstliche Agenten über eine kollektive Antwort auf eine Reihe von Argumenten abstimmen, die Wahrscheinlichkeit, dass ihre Abstimmung zu einer inkonsistenten Mehrheitsmeinung führt, stark mit der Meinungsvielfalt der Gruppe zusammenhängt. Dies verbessert unser Verständnis für die Schwierigkeiten, mit denen vielfältige Gruppen bei der Entscheidungsfindung konfrontiert sein können. Wenn sie bei ihrer Entscheidungsfindung nicht auf Mehrheitsbeschlüsse zurückgreifen können, müssen sie alternative, wahrscheinlich anspruchsvollere Aggregationsverfahren finden, um ihre Meinungsverschiedenheiten beizulegen.

Diese Ergebnisse stammen aus Computermodellen, die auf der Theorie dialektischer Strukturen basieren. Diese Theorie beschreibt Überlegungen anhand von Argumentationskarten. Die einzelnen Argumente in diesen Karten bestehen aus Prämissen und Schlussfolgerungen. Die Überzeugungen der Akteure in dialektischen Strukturmodellen werden als Zuordnungen von den diskutierten Prämissen und Schlussfolgerungen zu diskreten Wahrheitswerten umgesetzt.

Es gibt zwei Arten von dialektischen Strukturmodellen. Im ersten Modell fügen Agenten iterativ Argumente zu einer sich entwickelnden Argumentationskarte hinzu und aktualisieren ihre Überzeugungen entsprechend den Einführungen anderer. Sowohl die Einführung von Argumenten als auch die Reaktion darauf werden durch Faktoren eingeschränkt, die ein epistemisch rationales Verhalten gewährleisten. Über diese Einschränkungen hinaus formulieren die Akteure neue Argumente gemäß vordefinierten Argumentationsstrategien. Diese Strategien lassen sich in allozentrische und egozentrische Strategien unterteilen, die sich grundlegend unterschiedlich auf die Polarisierung von Überzeugungen auswirken. Die Bevölkerung polarisiert sich, wenn die Akteure nur egozentrische Strategien verfolgen, und sie depolarisiert sich, wenn sie allozentrisch argumentieren.

Das zweite Modell einer dialektischen Struktur entwickelt sich nicht durch iterative Hinzufügung von Argumenten. Stattdessen synthetisiert es eine Argumentationskarte gemäß einem Algorithmus, der in der Literatur zu dialektischen Strukturen zu finden ist. Eine auf diese Weise erstellte Argumentationskarte wirft ein epistemisches Entscheidungsproblem auf. Die Akteure haben die Aufgabe, ein Glaubenssystem zu finden, das die Gültigkeit aller vorgelegten Argumente gemeinsam akzeptiert. In der Regel gibt es viele Überzeugungen, die dieses Kriterium erfüllen, aber noch mehr, die es nicht erfüllen. Dieses Entscheidungsproblem wird zu einem Problem der kollektiven Entscheidungsfindung, wenn Agenten mit unterschiedlichen, individuell gültigen Überzeugungen sich auf ein einziges Glaubenssystem einigen müssen, das sie gemeinsam vertreten. In dem hier vorgestellten Modell führen die Agenten dazu eine satzweise Mehrheitsabstimmung durch. Diese Abstimmungen führen nicht unbedingt zu einer einheitlichen Meinung. Die Analyse der computergestützt gesammelten Daten zeigt, dass eine inkonsistente Aggregation stark mit einer zunehmenden Meinungsvielfalt, jedoch nicht mit einer Polarisierung der Überzeugungen verbunden ist.

„taupy“, eine neue Python-Implementierung für die Untersuchung dialektischer Strukturen, wurde im Rahmen dieser Dissertation implementiert und der Öffentlichkeit zugänglich gemacht. Diese Implementierung bietet Funktionen, die zuvor nicht verfügbar waren. Sie implementiert die Clusterbildung der Überzeugungen von Akteuren mit zwei hochmodernen Clustering-Algorithmen sowie Messungen der Polarisierung von Überzeugungen und der Meinungsvielfalt, einen Mehrheitsbeschlussmechanismus und andere Funktionen, die zur Beobachtung der hier vorgestellten Ergebnisse erforderlich sind. Ein Benutzerhandbuch ist in dieser Arbeit enthalten.

Dialektische Strukturmodelle verbessern unser Verständnis der dynamischen Aspekte von Konzepten, Einschränkungen und Normen, die wir in der Philosophie untersuchen. Dies macht die computergestützte Modellierung zu einem so fruchtbaren Ansatz für die Philosophie, insbesondere in der sozialen Erkenntnistheorie. In dieser Arbeit offenbart die Entdeckung der Polarisierung von Überzeugungen unter der Bedingung epistemischer Rationalität eine dynamische Eigenschaft unseres Rationalitätsbegriffs. Computergestützte Ansätze sind eine nützliche Ergänzung zu philosophischen Methoden, da solche dynamischen Aspekte mit etablierten Analysemethoden nicht zugänglich wären.

Diese Arbeit befasst sich aus rein philosophischem Interesse mit rechnergestützten Methoden, stützt sich jedoch in mehrfacher Hinsicht auf interdisziplinäre Bemühungen und leistet einen Beitrag dazu. Polarisierung und Vielfalt werden wie in anderen Bereichen verstanden, und die hier vorgestellte agentenbasierte Modellierung steht in Zusammenhang mit soziologischen Modellen, die ähnliche Argumente als Triebkräfte der Polarisierung nahelegen.

Diese Dissertation untersucht zwar Überzeugungen und deren Dynamik bei künstlichen, epistemisch rationalen Agenten, doch sind die Ergebnisse auch für unser Verständnis menschlicher Überlegungen und Argumentationen relevant. Grundsätzlich verhindert die Einhaltung epistemischer Rationalitätsnormen nicht das Entstehen einer Polarisierung von Überzeugungen. Das bedeutet, dass das Auftreten einer Polarisierung von Überzeugungen bei Menschen nicht automatisch als Beweis für epistemische Mängel eines Individuums angesehen werden kann. Und das Problem der inkonsistenten Aggregation von Überzeugungen in Gruppen mit unterschiedlichen Meinungen veranschaulicht die Schwierigkeiten, mit denen Gruppen mit epistemischen Zielen konfrontiert sein können. Dies hilft uns, die Bedingungen und Grenzen der Beratung der Öffentlichkeit durch Experten zu verstehen, insbesondere in Ausnahmesituationen mit hoher Unsicherheit und begrenzter Zeit. Die Ergebnisse dieser Arbeit legen nahe, dass wir unsere Erwartungen an diese Gruppen in Ausnahmesituationen tatsächlich moderieren sollten.

Epistemisch rationale Polarisierung von Überzeugungen und inkonsistente Aggregation von Überzeugungen sind Beispiele für ein umfassenderes Phänomen. Dabei handelt es sich um Fälle, in denen die Anhäufung individuell rationaler Fähigkeiten nicht zu einem optimalen Ergebnis für die Gemeinschaft führt. Durch die weitere Erforschung solcher faszinierenden Phänomene können wir hoffen, Einblicke in bemerkenswerte Bedingungen des menschlichen Denkens, der Rationalität und der Entscheidungsfindung zu gewinnen.

(*Originalsprache Englisch*)"

# Summary. An optional shortened abstract.
summary: ''

tags: []

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
links:
- name: URL
  icon: open-access
  icon_pack: ai
  url: https://publikationen.bibliothek.kit.edu/1000183401
- name: PhilPapers
  icon: philpapers
  icon_pack: ai
  url: https://philpapers.org/rec/KOPPDA

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  filename: symbolic-images/graduation/symbolic.png
  alt: 'symbolischer Doktorhut'
  caption: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [aggregation, polarisation]
---
