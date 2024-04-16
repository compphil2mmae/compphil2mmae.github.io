---
title: Tour
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
              brightness: 0.6
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
            filename: contact.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Zum ILIAS-Kurs
          url: https://ilias.studium.kit.edu/goto.php?target=crs_2342049&client_id=produktiv  
      - title: Einführung in die Philosophie
        content: 'Das Wahre & das Gute -- über die großen Fragen nachdenken'
        align: right
        background:
          image:
            caption: Test
            filename: raffael.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Zur ILIAS-Modulinformationsseite
          url: https://ilias.studium.kit.edu/goto.php?target=crs_1616180&client_id=produktiv
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
      title: Mission Statement
      text: |2-
        In der Lehre des [Departments für Philosophie](https://www.philosophie.kit.edu/) ist CompPhil²MMAE gemeinsam für die philosophische Grundlagenbildung zuständig.

        Text.

  - block: markdown
    id: ressurces
    content:
      title: "Materialien für Student:innen"
      text: |2-
        - {{% staticref "uploads/hinweise-essays.pdf" "newtab" %}}Einige Hinweise zum Verfassen von philosophischen Essays{{% /staticref %}}
        - test
        - test

        
---