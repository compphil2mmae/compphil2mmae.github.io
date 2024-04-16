---
title: 
type: landing
  
sections:
  - block: about.biography
    id: about
    content:
      title: ''
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: christian.seidel

  - block: slider
    content:
      slides:
      - title: '[Publikationen](#pubs)'
        content: 
        align: center
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: '[Vorträge](#talks)'
        content: 
        align: center
        background:
          image:
            filename: contact.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: '[Aktuelles](#news)'
        content: 
        align: center
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        # link:
        #   icon: graduation-cap
        #   icon_pack: fas
        #   text: Join Us
        #   url: '#news.cs'
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: '200px'
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 4000
  # - block: collection
  #   content:
  #     title: Veranstaltungen
  #     subtitle: Workshops, Vorträge, Gastvorträge
  #     text:
  #     count: 0
  #     filters:
  #       author: ''
  #       category: ''
  #       exclude_featured: false
  #       publication_type: ''
  #       tag: 'empty'
  #       exclude_future: false
  #       exclude_past: false
 
  - block: collection
    id: pubs
    content:
      title: Publikationen 
      count: 0
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: 'empty'
        exclude_future: false
        exclude_past: false
    design:
      columns: '1'  

  - block: collection
    content:
      title: Bücher 
      subtitle: Monographien & Sammelbände
      text:   
      count: 0
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: 'book'
        tag: ''
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      page_type: publication
      archive:
        enable: false
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase

  - block: collection
    content:
      title: Aufsätze 
      subtitle: in Zeitschriften
      text:   
      count: 0
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: 'article-journal'
        tag: ''
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      page_type: publication
      archive:
        enable: false
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    

  - block: collection
    content:
      title: Aufsätze 
      subtitle: in Sammelbänden
      text:   
      count: 0
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: 'chapter'
        tag: ''
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      page_type: publication
      archive:
        enable: false
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    

  - block: collection
    content:
      title: Rezensionen 
      subtitle: Bibliographien etc.
      text:   
      count: 0
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: 'review'
        tag: ''
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      page_type: publication
      archive:
        enable: false
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    


  - block: collection
    id: talks
    content:
      title: Vorträge 
      subtitle: # 'des CompPhil²MMAE-Teams'
      text:   
      count: 0
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: Vortrag
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      page_type: event
      archive:
        enable: false
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: compact # showcase

  - block: collection
    id: news
    content:
      title: Neuigkeiten 
      subtitle: 
      text:  
      count: 10
      filters:
        author: 'christian.seidel'
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: '' # 'highlight'
      offset: 0
      order: desc
      page_type: post
      # archive:
      #   enable: true
      #   text: Weitere <strong>Neuigkeiten</strong> 
      #   position: center
      #   link: post/
    design:
      view: compact # showcase # compact  
      columns: '2'
      flip_alt_rows: true
    
---