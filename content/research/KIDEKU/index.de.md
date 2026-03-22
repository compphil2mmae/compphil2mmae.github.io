---
title: Chancen von KI zur Stärkung unserer deliberativen Kultur (KIdeKu)
summary: KIdeKu untersuchte die Chancen dieser Technologien zur Stärkung unserer deliberativen Kultur, und insbesondere zur Steigerung der Teilhabe an zivilgesellschaftlichen und politischen Debatten.
tags:
  - LLMs
  - Angewandte Ethik
  - Deliberation
  - Computergestützte Philosophie
  - Normen der öffentlichen Argumentation
date: '2024-06-01'
type: 'project'
authors:
- gregor.betz
- inga.bones
- sebastian.cacean
- christian.seidel
- reta.luescher-rieger
- leonie.wahl

# Optional external URL for project (replaces project detail page).
# external_link: ''

image:
  caption: Foto von playground.com (generated with Stable Diffusion XL)
  focal_point: Smart

links:
  - icon: linkedin
    icon_pack: fab
    name: Visit
    url: 'https://www.linkedin.com/company/kideku'
  - icon: envelope
    icon_pack: fas
    name: Mail
    url: 'mailto:kideku@itz.kit.edu'

#url_code: ''
#url_pdf: ''
#url_slides: ''
#url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Im Projekt **_KIdeKu_** gingen wir der Frage nach, wie Large Language Models (LLMs) wie bspw. ChatGPT benutzt werden können, um unsere deliberative Kultur zu stärken. Welche Chancen bieten diese Technologien zur Verbesserung unserer demokratischen Praxis? Konkreter:

+ Wie können LLMs benutzt werden, um die Qualität des öffentlichen Diskurses zu verbessern? 
+ Welche derzeitigen Probleme (Desinformation, Hassrede, ...) können durch die Verwendung von LLMs adressiert werden? 
+ Welche Voraussetzungen müssen für einen erfolgreichen Einsatz von LLMs erfüllt sein? 
+ Welche konkreten Einsatzszenarien sind vielversprechend für einen positiven Beitrag von LLMs zur deliberativen Kultur? 
+ Wie können wir politische Teilhabe durch LLMs stärken?
  + Für welche Zielgruppen ist der Einsatz von LLMs besonders aussichtsreich? 
  + Welche besonderen Herausforderungen stellt die Zielgruppe junger Menschen? 
+ ...

<!-- Ziele -->
## Ziele & Vorgehen

![Vorgehen in KIdeKu](kideku_ziele_ablauf.jpg)

Verfolgte Ziele: 

1. 👥 **Entwicklung von Einsatzszenarien:** In Abstimmung mit zivilgesellschaftlichen Akteur:innen konzipierten wir relevante und neuartige Einsatzszenarien. Wir wollten einen möglichst breiten Überblick darüber schaffen, wie LLMs gemeinwohlorientiert in unserer demokratischen Praxis verwendet werden können und welche Ziele damit verfolgt werden können. Es sollten sowohl die Anforderungen zivilgesellschaftlicher Organisationen an die Verwendung und Einbindung LLM-basierter Applikationen als auch die Bedarfe der unterschiedlichen Zielgruppen erfasst werden. Beispiele für solche Einsatzszenarien umfassen:
   + Faktenprüfer, Hate Speech Detektoren, KI-Assistenz beim Verfassen von Redebeiträgen, (partiell) automatisierte Moderation in Onlinedebatten, Debattenzusammenfassung, Argumentationserklärung, Argumentprüfung, ... 
2. 🤖 **Schaffung technischer Grundlagen:** Für einige der konzeptionierten Einsatzszenarien entwickeln wir technische Grundlagen, die von der Community benutzt und weiterentwickelt werden können. Diese Grundlagen umfassen:
   + **Anforderungen**, anhand derer sich die Eignung von Sprachmodellen für den vorgesehenen Einsatz systematisch prüfen lässt. Diese Anforderungen können in Form deliberativer Benchmarks (Testdatensätze) operationalisiert werden.
   + **Demoapps**, die den Einsatz von LLMs illustrieren und Ausgangspunkt für die Entwicklung einsatzbereiter Apps darstellen. 
3. 📋 **Handlungsorientierung:** Ein Endbericht fasst den derzeitigen Wissensstand zur Nutzung von LLMs in deliberativen Demokratien zur Stärkung unserer deliberativen Kultur zusammen, trägt Projektergebnisse zusammen und formuliert Empfehlungen und Best Practices für zivilgesellschaftliche und politische Akteur:innen.

Insgesamt erarbeiteten wir in **_KIdeKu_** damit Konzepte und Studien zur Schaffung eines geeigneten operativen Rahmens für die Entwicklung und den Einsatz gemeinwohlorientierter KI in unserer demokratischen Praxis und hoffen, dass die Ergebnisse und Ideen aufgegriffen sowie weiterentwickelt werden. 

## Projektergebnisse

### 🕵️‍♀️ EvidenceSeeker Boilerplate

Ein Code Template für eine RAG/LLM-basierte Fact-Checking-App relativ zu einer gegebenen Datenbasis. 

📖 Dokumentation: <https://debatelab.github.io/evidence-seeker/>

📊 Webseite mit Beispielergebnissen: <https://debatelab.github.io/evidence-seeker-results/>

🧩 Code: <https://github.com/debatelab/evidence-seeker>

🤗 Gradio DemoApp: <https://huggingface.co/spaces/DebateLabKIT/evidence-seeker-demo>

### 📣 Toxicity Detektor 

Eine auf Sprachmodellen basierte Pipeline zur Detektion toxischer Sprache.

🧩 Code: <https://github.com/debatelab/toxicity-detector>

### syncIALO 🤖🗯️

Synthetische Argumentkartendatensätze 

🧩 Code: <https://github.com/debatelab/syncIALO>

<!--
### 📋 Abschlussbericht

-->


---
*Projektlaufzeit:* 01.06.2024--31.12.2025

{{< figure src="/logos/bmbfsfj/BMBFSFJ_de_v1_farbig.png" 
    alt="Bundesministerium für Familie, Senioren, Frauen und Jugend" 
    width="350px" 
    class="float-left mt-0"
    >}}
