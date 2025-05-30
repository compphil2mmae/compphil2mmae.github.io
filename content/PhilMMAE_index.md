---
# Leave the homepage title empty to use the site title
draft: true
title: 
date: 2024-01-01
type: landing

sections:
  - block: hero
    content:
      title: Arbeitsbereich **Philosophische Methoden, Moralphilosophie & Angewandte Ethik**
  - block: hero
    content:
      image: 
        filename: wordcloud.png  
      text: |2-
         
        Das Team des Arbeitsbereichs **Philosophische Methoden, Moralphilosophie & Angewandte Ethik (PhilMMAE)** forscht und lehrt  
        
        - zu grundlegenden moraltheoretischen Fragen,  
        - zur Ethik des öffentlichen Diskurses,  
        - zu normativen Problemen in gesellschaftlich relevanten, angewandten Kontexten wie Klimawandel, Überwachung oder künstlicher Intelligenz sowie  
        - zur britischen Moral- und Sozialphilosophie des 19. Jahrhunderts.
        
        PhilMMAE ist Teil des Departments für Philosophie am Karlsruher Institut für Technologie (KIT) und dort in der Lehre für die philosophischen Grundlagen zuständig.  
    design:  
      background:
        color: white

  - block: collection
    content:
      title: Neuigkeiten
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the teammates →" %}}
    design:
      columns: '1'
---
