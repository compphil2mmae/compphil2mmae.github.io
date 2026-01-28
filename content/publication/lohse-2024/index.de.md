---
title: Pluralism, Consensus, and Justification (Pluralismus, Konsens und Rechtfertigung)
subtitle: A Simulation Study on Overlapping Consensus in Liberal Democracies (Eine Simulationsstudie zu sich überschneidenden Konsensen in liberalen Demokratien)

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- richard.lohse

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-12-31'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-01-14T08:00:16.558926Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- thesis

# Publication name and optional abbreviated publication name.
publication: '*Karlsruher Institut für Technologie (KIT)*'
publication_short: 'KIT'

publisher: 'Karlsruher Institut für Technologie (KIT)'
school: 'Karlsruher Institut für Technologie (KIT)'
address: Karlsruhe

language: english
pagetotal: 228

#doi: '10.5445/IR/1000169559'

abstract: 'Diese Dissertation untersucht die Bedingungen für einen überlappenden Konsens in pluralistischen Gesellschaften. Sie kombiniert philosophische Analyse mit formaler Modellierung und Simulation, um zu erforschen, wie Pluralismus, Konsens und Rechtfertigung in Verfassungsfragen gleichzeitig möglich sein können. Die Studie zeigt, dass für globale überlappende Konsense nur verfassungsstützende Weltbilder in der öffentlichen Debatte zulässig sind, während für lokale Konsense neutrale Weltbilder akzeptabel sind.'

# Summary. An optional shortened abstract.
summary: ''

tags:
- Überlappender Konsens
- Überlegungsgleichgewicht
- John Rawls
- Computationale Philosophie
- Formale Methoden
- Modellierung
- Pluralismus
- Verfassungstheorie
- Demokratische Legitimität
- Politische Philosophie

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
- name: PDF
  icon: file-pdf
  url: Pluralism-Consensus-and-Justification.pdf
- name: Buch
  icon: book
  icon_pack: fas
  url: https://katalog.bibliothek.kit.edu/cgi-bin/koha/opac-detail.pl?biblionumber=1444370
- name: Projekt
  icon: folder-tree
  icon_pack: fas
  url: https://re-models.github.io/

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  filename: 'symbolic-images/graduation/symbolic.png'
  alt: 'symbolischer Doktorhut'
  caption: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [DFG_RE]
---
# Übersicht
Viele Gesellschaften sind pluralistisch. Das heißt insbesondere, dass sie eine Vielfalt an Weltanschauungen aufweisen. Trotzdem wäre es gut, wenn es unter den Bürgerinnen einen Konsens zumindest in grundlegenden Verfassungsfragen gibt. Zudem ist es wünschenswert, dass jede einzelne Bürgerin die Verfassung nicht aus Zwang, sondern aus guten Gründen akzeptiert, d.h. in ihren Meinungen gerechtfertigt ist. Diese drei Bedingungen (Pluralismus, Konsens, Rechtfertigung) können in einem Spannungsverhältnis stehen. Insbesondere kann es sein, dass die Vielfalt an Weltanschauungen derart ist, dass ein gerechtfertigter Konsens in Verfassungsfragen unmöglich wird.

Wenn dies der Fall ist, gibt es vie rMöglichkeiten, damit umzugehen: Wir können entweder auf Konsens verzichten, auf Rechtfertigung verzichten, Pluralismus ganz abschaffen oder aber Bedingungen schaffen, die zu einem Pluralismus führen, der Konsens und Rechtfertigung nicht im Wege steht. Die ersten drei Optionen, so argumentiere ich, sind mit erheblichen Problemen verschiedener Art verbunden.

Daher ist es von großer Bedeutung, die vierte Option zu untersuchen und Umstände zu finden, unter denen es gleichzeitig Pluralismus, Konsens und Rechtfertigung geben kann. Um es mit dem Begriff von John Rawls zu sagen, müssen wir Umstände finden, unter denen ein überlappender Konsens möglich ist. In dieser Arbeit versuche ich, einen Beitrag zu diesem Ziel zu leisten. Dabei konzentriere ich mich auf den erkenntnistheoretischen Aspekt der Aufgabe: Was muss der Fall sein, damit das Rechtfertigungskriterium erlaubt, dass eine Konstellation von Glaubenssystemen sowohl Pluralismus als auch Konsens aufweist? Diese Frage hat bis dato wenig direkte Aufmerksamkeit erfahren.

Meine Methodik zur Untersuchung dieser Frage stützt sich auf formale und rechnergestützte Erkenntnistheorie. Insbesondere kann die vorliegende Dissertation in zwei Teile geteilt werden.

Im ersten Teil, dem *philosophischen* Teil, wenn man so will, stelle ich zunächst die Rawls’sche Idee eines überlappenden Konsens etwas detaillierter dar. Ich betone jedoch, dass meine Arbeit eine strukturelle, der Logik nicht unähnliche Perspektive einnimmt und damit von vielen heiß diskutierten Fragen der Rawls’schen Theorie unabhängig ist. Das heißt insbesondere, dass die Arbeit für Philosophinnen verschiedener Lager von Interesse ist. Anschließend entwickle ich eine Handvoll Definitionen für verschiedene Stadien eines überlappenden Konsenses. Diese Definitionen sind meines Wissens so noch nicht formuliert worden und bilden die Grundlage für die vorliegende und eventuell anschließende Arbeiten. Besonders hervorzuheben ist die Unterscheidung zwischen einem globalen und einem lokalen überlappenden Konsens. Letzterer ist der schwächere Begriff und erfordert lediglich, dass es in einer Teilgesellschaft Pluralismus, Konsens und Rechtfertigung gibt. Man kann versuchen, daraus einen globalen überlappenden Konsens zu machen, indem man untersucht, welche günstigen Bedingungen in der Teilgesellschaft herrschen und versucht, diese günstigen Bedingungen auch im Rest der Gesellschaft herzustellen.

Des Weiteren entwickle ich in diesem ersten, philosophischen Teil der Dissertation eine Definition des hier relevanten Rechtfertigungsbegriffs. Dieser fußt auf der Methode des Überlegungsgleichgewichts. Grob gesagt gilt ein Meinungssystem als gerechtfertigt genau dann, wenn es das Ergebnis der Anwendung dieser Methode hätte sein können. Bei Anwendung der Methode müssen auch alternative Sichtweisen und Argumente, nicht nur die eigenen, berücksichtigt werden. Die Gesamtheit aller zu berücksichtigenden Sichtweisen und Argumente nenne ich *dialektische Situation*. Ich argumentiere, dass die dialektische Situation jeder Bürgerin mindestens all jene Sichtweisen und Argumente enthält, die in breiter Weise *öffentlich debattiert* werden, z.B. in den klassischen und sozialen Medien, in Parlamenten, etc. Die dialektischen Situationen der Bürgerinnen werden erwartbarer weise einen signifikanten Einfluss auf die Möglichkeit eines überlappenden Konsenses haben. Die vorliegende Dissertation soll diesen Einfluss untersuchen.

Genauer geht es um den Einfluss der inferentiellen Beziehungen zwischen den öffentlich debattierten Weltanschauungen und der Verfassung. Ich stelle die in der Arbeit zu prüfende Hypothese auf, dass nur Weltbilder, die die Verfassung *stützen*, einen überlappenden Konsens bezüglich selbiger möglich machen. Sollte sich diese Hypothese als zutreffend erweisen, könnte dies einen hohen Standard an die öffentliche Debatte stellen. Insbesondere könnte das im schlimmsten Fall bedeuten, dass mit der Verfassung *inkompatible* oder auch nur *neutrale* Weltbilder von der öffentlichen Debatte aus geschlossen werden müssen. Insbesondere bezüglich letzterer ist das nicht wünschenswert, da äußerst illiberal. Es ist also wichtig, diese Hypothese zu überprüfen.

Im zweiten Teil der Dissertation, dem formalen und rechnergestützten Teil, schlage ich mathematische Explikationen der verschiedenen Arten von überlappendem Konsens vor. Anschließend stelle ich Design und Ergebnisse einer Simulationsstudie vor, die dazu dient, die o.g. Hypothese zu überprüfen.

Die mathematische Explikation des zuvor definierten Rechtfertigungsbegriffs basiert auf dem formalen Modell des Überlegungsgleichgewichts, das jüngst von Claus Beisbart, {{% mention gregor.betz %}} und Georg Brun vorgestellt wurde. Ich stelle dieses vor, passe es an die vorliegende Problematik an und gebe schließlich ein mathematisches Kriterium für Rechtfertigung an. Dieses kann auch von Computern in sog. Simulationen berechnet werden. Anschließend stelle ich verschiedene mathematische Maße für Konsens und Pluralismus vor. Diese sind so entworfen, dass sie der Untersuchung der Frage nach überlappendem Konsens dienen. Die mathematischen Explikationen von Rechtfertigung, Konsens und Pluralism werden nun zu präzisen und in Studien anwendbaren Explikationen der verschiedenen Arten von überlappendem Konsens zusammengefügt.

Anschließend stelle ich eine breit angelegte Simulationsstudie vor, die die Hypothese testen soll. Diese Studie beruht nicht auf empirischen Daten. Stattdessen werden zufällig generierte, künstliche, und relativ kleine Gesellschaften simuliert. Die ‘Bürgerinnen’ befinden sich je nach Gesellschaft in verschiedensten dialektischen Situationen. Insbesondere liegen verschiedenste Kombinationen von inferentiellen Beziehungen zwischen Weltbildern und Verfassung vor. Für jede Gesellschaft kann mit den zuvor entwickelten Explikationen untersucht werden, ob ein überlappender Konsens in globalem oder lokalem Sinne vorliegt. Es wird dann ausgewertet, für welche Kombinationen von inferentiellen Beziehungen besonders oft oder besonders selten ein überlappender Konsens vorliegt. Anhand dieser Auswertung kann die Hypothese überprüft werden. Natürlich sind wir letztlich nicht an künstlichen Gesellschaften interessiert. Ich erkläre, warum sich aus den Ergebnissen auch entsprechende Rückschlüsse auf echte Gesellschaften ziehen lassen.

Das Ergebnis der Simulationsstudie ist, grob gesagt, dass die Hypothese für *globale* überlappende Konsense bestätigt oder zumindest nicht falsifiziert wird. Das heißt, dass in der öffentlichen Debatte nur stützende Weltbilder einen globalen überlappenden Konsens möglich machen. Allerdings gilt für *lokale* überlappende Konsense ein niedrigerer Standard. Für solche ist lediglich erforderlich, dass es keine inkompatible Weltbilder in der öffentlichen Debatte gibt. Neutrale Weltbilder hingegen sind nicht hinderlich.

Ich diskutiere auch, welche Konsequenzen sich aus diesen Ergebnissen ziehen lassen. Zunächst ist das Ergebnis für globale überlappende Konsense besorgniserregend, weil es wie erwähnt bedeuten könnte, dass inkompatible und neutrale Weltbilder von der öffentlichen Debatte ausgeschlossen werden müssen. Ich lote aus, inwieweit sich diese illiberale Konsequenz eventuell vermeiden lässt. Das Ergebnis für lokale überlappende Konsense hingegen macht Hoffnung. Wie erwähnt kann man untersuchen, welche Bedingungen in der jeweiligen Teilgesellschaft vorliegen und untersuchen, ob solche günstigen Bedingungen auch im Rest der Gesellschaft herstellbar sind. Ich spekuliere, was diese Bedingungen sein könnten und schlage Folgestudien vor, die diese Spekulation überprüfen. Sollte wir entsprechende günstige Bedingungen finden, lässt sich das besorgniserregende Ergebnis für globale überlappende Konsense möglicherweise vermeiden.

Die vorliegende Dissertation legt den Grundstein für weitere Untersuchungen der hochrelevanten Frage, wie ein gerechtfertigter Konsens in Verfassungsfragen trotz weltanschaulichem Pluralismus möglich ist. Insbesondere legt sie eine Reihe fruchtbarer begrifflicher Präzisierungen vor, die für solche Untersuchungen, insbesondere empirischer Natur, unerlässlich sind. Desweiteren liefert sie mit der durchgeführten Simulationsstudie einen Aufschlag, der weiterführende Forschung anregt.
