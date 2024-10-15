---
title: Teaching
date: 2022-10-24

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: '|{{< icon name="book-open-reader" pack="fas" >}} | {{< icon name="chalkboard-user" pack="fas" >}} | {{< icon name="laptop-code" pack="fas" >}} |  <br /> CompPhil²MMAE in teaching'
        content: Basic philosophical education
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
          text: Learn more
          url: '#mission'  
      - title: "Ars Rationalis" 
        content: 'Learn to think critically & develop argumentative skills'
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
          text: To the ILIAS-course
          url: https://ilias.studium.kit.edu/goto.php?target=crs_2342049&client_id=produktiv  
      - title: Einführung in die Philosophie (Introduction to philosophy)
        content: 'Das Wahre & das Gute -- über die großen Fragen nachdenken (The true & the good -- thinking about the big questions)'
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
          text: To the ILIAS module information page
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
      title: "Mission Statement"
      text: |2-
         <font size="+1"> In the [Department of Philosophy](https://www.philosophie.kit.edu/), CompPhil²MMAE is jointly responsible for the **philosophical foundation**. We are responsible for the specialised modules in the first year of study:
        - **Ars Rationalis**: This [module](https://ilias.studium.kit.edu/goto.php?target=crs_2342049&client_id=produktiv) aims to teach critical thinking and develop argumentative skills. These skills are central to all academic disciplines and so the module is also part of other degree programmes.  
        - **Introduction to Philosophy**: This [module](https://ilias.studium.kit.edu/goto.php?target=crs_1616180&client_id=produktiv) offers an initial introduction to the major questions of philosophy and provides important basic knowledge for the further study of philosophy. It is part of all degree programmes in which Philosophy can be studied as a major or minor subject, and is also open to the [Studium Generale](https://www.zak.kit.edu/studium_generale.php).

        In teaching, we rely on **innovative teaching formats** and **activating methods** such as inverted classroom, live feedback, argument reconstruction in teamwork, peer assessment, small group tutorials for discussing essays or study projects. Some of our courses (such as the [CompPhil²MMAE project seminar]({{< relref "/event/240508_W_Blockseminar_Argumentationsanalyse" >}}) organised in cooperation with the University of Bern and most of our interdisciplinary courses in cooperation with the Department of Computer Science) are **project-based**. 

        In the CompPhil²MMAE research seminar "Current Texts in Philosophy", we introduce advanced students to current research questions in the sense of **research-orientated teaching**. In this central discussion and reflection space for our team, CompPhil³MMAE members and [external speakers]({{< relref "/event#guests" >}}) present their research work from philosophy and related disciplines and students present their final theses (usually in a pre-read format) for discussion.

        **Philosophical writing** is a particular concern of ours. We are convinced that philosophical reflection is essentially realised in independent philosophical writing. Within the framework of an argumentation-based writing propaedeutic, we therefore try to gradually enable students, initially through many low-threshold writing occasions (written reflection on lecture content, philosophical diary), then through formats of medium frequency and moderate scope (reading notes on individual seminar texts, short essays on several seminar texts), to finally be able to independently present their own more extensive philosophical reflections in term papers and theses. 

        CompPhil²MMAE [researches]({{< relref "/research/" >}}) also on **Large Language Models (LLMs)**. We believe that this technology will fundamentally change our society very quickly and that our society is inadequately prepared for this change - especially because the technology is currently often used without reflection. Against this background, we also want our teaching portfolio to contribute to the development of **computational literacy**; by this we mean the ability to use computational methods in a reflective, productive way and to help shape LLM technology. However, we consider it essential that students develop **fundamental higher-level deliberative skills** at a level that enables them to reflect *on their own* use of the technology and, for example, to check whether the output generated by an LLM-based artificial actor corresponds to *their own* thoughts. In order to be able to utilise the opportunities offered by technology productively and competently, one must first learn to *think for oneself* -- and that means *write for oneself*: learn to *write*. 
        
  - block: markdown
    id: ressources
    content:
      title: "Materials for students"
      text: |2-
        {{% staticref "uploads/hinweise-essays.pdf" "newtab" %}} Some tips on writing philosophical essays{{% /staticref %}}
     
---