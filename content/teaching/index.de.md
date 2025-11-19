---
title: Lehre
date: 2022-10-24

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: '|{{< icon name="book-open-reader" pack="fas" >}} | {{< icon name="chalkboard-user" pack="fas" >}} | {{< icon name="laptop-code" pack="fas" >}} |  <br /> CompPhil²MMAE in der Lehre'
        content: Philosophische Grundlagenbildung
        align: center
        background:
          image:
            filename: lehre-1.jpg
            filters:
              brightness: 0.35
          position: center
          color: '#666'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Mehr erfahren
          url: '#mission'  
      - title: "Ars Rationalis" 
        content: 'Kritisches Denken lernen & argumentative Kompetenzen entwickeln'
        align: left
        background:
          image:
            filename: argdown_vscode_ars.png
            filters:
              brightness: 0.4
          position: center
          color: '#555'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Zum ILIAS-Kurs
          url: https://ilias.studium.kit.edu/goto.php/crs/2748649
      - title: Einführung in die Philosophie
        content: 'Das Wahre & das Gute -- über die großen Fragen nachdenken'
        align: right
        background:
          image:
            caption: Test
            filename: raffael.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Zur ILIAS-Modulinformationsseite
          url: https://ilias.studium.kit.edu/goto.php/crs/1616180
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 4000

  - block: markdown
    id: mission
    content:
      title: "Mission Statement"
      text: |2-
        <font size="+1"> In der Lehre des [Departments für Philosophie](https://www.philosophie.kit.edu/) ist CompPhil²MMAE gemeinsam für die **philosophische Grundlagenbildung** zuständig. Wir verantworten die fachlichen Module im ersten Studienjahr:
        - **Ars Rationalis**: Dieses {{< link "current_ars-rationalis" >}}Modul{{< /link >}} zielt darauf ab, kritisches Denken zu lernen und argumentative Kompetenzen zu entwickeln. Diese Fähigkeiten sind für alle akademischen Disziplinen von zentraler Bedeutung und so ist das Modul auch Bestandteil anderer Studiengänge.  
        - **Einführung in die Philosophie**: Dieses {{< link "modul-info_einführung-philo" >}}Modul{{< /link >}} bietet eine erste inhaltliche Einführung in die großen Fragen der Philosophie und vermittelt dabei wichtige Grundkenntnisse für das weitere Studium der Philosophie. Es ist Bestandteil aller Studiengänge, in denen  Philosophie als Haupt- oder Nebenfach studierbar ist, sowie zusätzlich geöffnet für das [Studium Generale](https://www.zak.kit.edu/studium_generale.php).

        In der Lehre setzen wir auf **innovative Lehrformate** und **aktivierende Methoden** wie Inverted Classroom, Live-Feedback, Argumentrekonstruktionen in Teamarbeit, Peer Assessment, Kleingruppen-Tutorials zur Besprechung von Essays oder Studienprojekten. Einige unserer Lehrveranstaltungen (wie das in Kooperation mit der Universität Bern durchgeführte [CompPhil²MMAE-Projektseminar]({{< relref "/event/240508_W_Blockseminar_Argumentationsanalyse" >}}) und die meisten unserer interdisziplinären Lehrveranstaltungen in Kooperation mit der Informatik)) führen wir **projektbasiert** durch. 

        Fortgeschrittene Student:innen führen wir im CompPhil²MMAE-Forschungsseminar “Aktuelle Texte der Philosophie” im Sinne der **forschungsorientierten Lehre** an aktuelle Forschungsfragen heran. In diesem für unser Team zentralen Diskussions- und Reflexionsraum stellen CompPhil³MMAE-Mitglieder sowie [auswärtige Referentinnen]({{< relref "/event#guests" >}})  ihre Forschungsarbeiten aus der Philosophie sowie angrenzender Disziplinen und Student:innen ihre Abschlussrbeiten (in der Regel in einem Pre-Read-Format) zur Diskussion.

        Ein besonderes Anliegen ist uns **das philosophische Schreiben**. Wir sind überzeugt, dass sich philosophisches Nachdenken ganz wesentlich im eigenständigen philosophischen Schreiben vollzieht. Im Rahmen einer argumentationsbasierten Schreibpropädeutik versuchen wir daher stufenweise, zunächst über viele niederschwellige Schreibanlässe (schriftliche Reflexion von Vorlesungsinhalten, Philosophisches Tagebuch), dann über Formate mittlerer Häufigkeit und moderaten Umfangs (Lektürenotizen zu einzelnen Seminartexten, Kurzessays zu mehreren Seminartexten) dazu zu befähigen, schließlich auch umfangreichere eigene philosophische Überlegungen in Hausarbeiten und Abschlussarbeiten eigenständig darstellen zu können. 

        CompPhil²MMAE [forscht]({{< relref "/research/" >}}) auch zu **Large Language Models (LLMs)**. Wir glauben, dass diese Technologie unsere Gesellschaft sehr schnell grundlegend wandeln wird und unsere Gesellschaft auf diesen Wandel nur unzureichend vorbereitet ist -- insbesondere auch, weil die Technologie derzeit häufig unreflektiert eingesetzt wird. Vor diesem Hintergrund wollen wir mit unserem Lehrportfolio auch zur Entwicklung von **computational literacy** beitragen; darunter verstehen wir die Befähigung zum reflektierten, produktiven Einsatz computationaler Methoden und zur Mitgestaltung der LLM-Technologie. Dafür halten wir allerdings für unverzichtbar, dass Student:innen **grundlegendere höherstufige deliberative Fähigkeiten** auf einem Niveau ausbilden, das sie überhaupt erst dazu befähigt, den Einsatz der Technologie *selbst* zu reflektieren und z.B. zu prüfen, ob der von einem LLM-basierten künstlichen Akteur generierte Output dem *eigenen* Gedanken entspricht. Um die Chancen der Technologie produktiv und kompetent nutzen zu können, muss man zunächst *selbst denken* -- und das heißt: *selbst schreiben* -- lernen. 
        
  - block: markdown
    id: ressources
    content:
      text: |2-
        {{% staticref "uploads/hinweise-essays.pdf" "newtab" %}}Einige Hinweise zum Verfassen von philosophischen Essays{{% /staticref %}}
      title: "Materialien für Student:innen"
---
