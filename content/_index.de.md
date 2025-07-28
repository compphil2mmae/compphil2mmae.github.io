---
# Leave the homepage title empty to use the site title
title: 
date: 2024-01-01
type: landing

sections:   
  - block: hero
    content:
      title: Arbeitsbereich **Computationale Philosophie, Philosophische Methoden, Moralphilosophie & Angewandte Ethik**
    design:
      spacing:
        padding: ['50px', '0', '40px', '0']        

  - block: hero
    content:
      title:   
      text:  |2-
        ![](transparent2.png)
    design:
      background:
        color: white
        image: 
          filename: welcome_new.jpg  
          filters:
            brightness: 1.07
          parallax: false
          position: center
          size: contain # fit: contain
      spacing:
        padding: ['10px', '0px', '10px', '0px']        

# - block: markdown
  #   content:
  #     text: |2-  
  #       <font size="+3"> Arbeitsbereich **Computationale Philosophie, Philosophische Methoden, Moralphilosophie & Angewandte Ethik**

  # - block: markdown
  #   content:
  #     title:  
  #     subtitle: ''
  #     text:  |2-
  #       ![](welcome_new.jpg)
  #       {height="200px"}
  #   design:   
  #     spacing:
  #       padding: ['1px', '0', '1px', '0']        

  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text: 
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: welcome_new.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: contain
  #         text_color_light: true
  #     spacing:
  #       padding: ['50px', '0', '50px', '0']        
  #     css_class: fullscreen

  - block: markdown
    content:
      text: |2-  # "|" stands for multi-line preserving newlines, adivsable for markdown; ">" stands for folded code, converting newlines into spaces; "2" is the indentation indicator (here: 2 chars); "-" strips trailing blank lines, https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines
        <font size="+2"> Das Team des Arbeitsbereichs **Computationale Philosophie, Philosophische Methoden, Moralphilosophie & Angewandte Ethik (CompPhil²MMAE)** forscht und lehrt </font>
        <font size="+1"> 
        - zur Reichtweite und Leistungsfähigkeit computationaler (LLM-basierter) Methoden in der Philosophie,  
        - zu normativen Modellen des Schlussfolgerns und Argumentierens,  
        - zur logischen Analyse politischer und wissenschaftlicher Debatten,  
        - zu Methoden und Instrumenten, die die epistemische Qualität öffentlicher Deliberation verbessern,  
        - zu grundlegenden moraltheoretischen Fragen,  
        - zur Ethik des öffentlichen Diskurses,  
        - zu normativen Problemen in gesellschaftlich relevanten, angewandten Kontexten wie Klimawandel, Überwachung oder künstlicher Intelligenz sowie  
        - zur britischen Moral- und Sozialphilosophie des 19. Jahrhunderts.
        {.c .c2}
        </font>
        <font size="+2"> Wir unterstützen die Grundsätze der <a href="https://betterscience.ch/#/" target="_blank" rel="noopener">Better Science Initiative</a>.</font>
        {{% cta cta_link="./research/" cta_text="Mehr über unsere **Forschung** erfahren →" %}}
    design:  
      # background:
      #   color: white
      spacing:
        padding: ['40px', '0', '10px', '0']        

  - block: markdown
    content:
      text: |2-  # "|" stands for multi-line preserving newlines, adivsable for markdown; ">" stands for folded code, converting newlines into spaces; "2" is the indentation indicator (here: 2 chars); "-" strips trailing blank lines, https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines       
        <font size="+2"> **CompPhil²MMAE** ist ein Zusammenschluss der Arbeitsgruppen des Lehrstuhls für Wissenschaftstheorie ([DebateLab](https://debatelab.philosophie.kit.edu)) und des Lehrstuhls für Philosophische Anthropologie. Als Teil des [Departments für Philosophie](https://www.philosophie.kit.edu/) am [Karlsruher Institut für Technologie (KIT)](https://www.kit.edu) sind wir in der Lehre gemeinsam für die philosophische Grundlagenbildung zuständig. {{% cta cta_link="./teaching/" cta_text="Mehr über unsere **Lehre** erfahren →" %}} </font>
    design:  
      # background:
      #   color: white
      spacing:
        padding: ['40px', '0', '10px', '0']        
  # - block: markdown
  #   content:
  #     text: |2-  # "|" stands for multi-line preserving newlines, adivsable for markdown; ">" stands for folded code, converting newlines into spaces; "2" is the indentation indicator (here: 2 chars); "-" strips trailing blank lines, https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines
  #       <font size="+2"> Das Team des Arbeitsbereichs **Computationale Philosophie, Philosophische Methoden, Moralphilosophie & Angewandte Ethik (CompPhil²MMAE)** forscht und lehrt </font>
  #       <font size="+1"> 
  #       - zu normativen Modellen des Schlussfolgerns und Argumentierens,  
  #       - zur logischen Analyse politischer und wissenschaftlicher Debatten,  
  #       - zu Methoden und Instrumenten, die die epistemische Qualität öffentlicher Deliberation verbessern, 
  #       - zur Reichtweite und Leistungsfähigkeit computationaler Methoden in der Philosophie,
  #       - zu grundlegenden moraltheoretischen Fragen,  
  #       - zur Ethik des öffentlichen Diskurses,  
  #       - zu normativen Problemen in gesellschaftlich relevanten, angewandten Kontexten wie Klimawandel, Überwachung oder künstlicher Intelligenz sowie  
  #       - zur britischen Moral- und Sozialphilosophie des 19. Jahrhunderts.
  #       {.c .c2}
  #       </font>
        
  #       <font size="+2"> **CompPhil²MMAE** ist ein Zusammenschluss der Arbeitsgruppen des Lehrstuhls für Wissenschaftstheorie ([DebateLab](https://debatelab.philosophie.kit.edu)) und des Lehrstuhls für Philosophische Anthropologie. Als Teil des [Departments für Philosophie](https://www.philosophie.kit.edu/) am [Karlsruher Institut für Technologie (KIT)](https://www.kit.edu) sind wir in der Lehre gemeinsam für die philosophische Grundlagenbildung zuständig. {{% cta cta_link="./teaching/" cta_text="Mehr über unserer **Lehre** erfahren →" %}} </font>
  #   design:  
  #     # background:
  #     #   color: white
  #     spacing:
  #       padding: ['40px', '0', '0px', '0']        


  # - block: hero
  #   content:
  #     text: |2-   # "|" stands for multi-line preserving newlines, adivsable for markdown; ">" stands for folded code, converting newlines into spaces; "2" is the indentation indicator (here: 2 chars); "-" strips trailing blank lines, https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines
  #       - zu grundlegenden moraltheoretischen Fragen,  
  #       - zur Ethik des öffentlichen Diskurses,  
  #       - zu normativen Problemen in gesellschaftlich relevanten, angewandten Kontexten wie Klimawandel, Überwachung oder künstlicher Intelligenz sowie  
  #       - zur britischen Moral- und Sozialphilosophie des 19. Jahrhunderts.
  #   design:  
  #     background:
  #       color: white

  # - block: markdown
  #   content:
  #     text: |2-  
  #       <font size="+2"> **CompPhil²MMAE** ist ein Zusammenschluss der Arbeitsgruppen des Lehrstuhls für Wissenschaftstheorie ([DebateLab](https://debatelab.philosophie.kit.edu)) und des Lehrstuhls für Philosophische Anthropologie. Als Teil des [Departments für Philosophie](https://www.philosophie.kit.edu/) am [Karlsruher Institut für Technologie (KIT)](https://www.kit.edu) sind wir in der Lehre gemeinsam für die philosophische Grundlagenbildung zuständig.  </font>
  #   design:  
  #     background:
  #       color: white

  - block: collection
    content:
      title: Neuigkeiten 
      subtitle: 
      text:  
      count: 10
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: 'highlight'
      offset: 0
      order: desc
      page_type: post
      # archive:
      #   enable: true
      #   text: Weitere <strong>Neuigkeiten</strong> 
      #   position: center
      #   link: post/
    design:
      view: showcase # compact  
      columns: '1'
      flip_alt_rows: true
      spacing:
        padding: ['40px', '0', '0px', '0']

  - block: markdown
    content:
      title: 
      subtitle: ''
      text: |
        {{% cta cta_link="./post/" cta_text="Mehr **Neuigkeiten** erfahren →" %}}
    design:
      background: 
        color: white
      spacing:
        padding: ['0px', '0', '10px', '0']

  - block: markdown
    content:
      title: Team
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1.4
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['40px', '0', '0px', '0']
      css_class: fullscreen
    
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./team/" cta_text="Unser **Team** kennenlernen →" %}}
    design:
      columns: '1'
      spacing:
        padding: ['10px', '0', '0px', '0']
---
