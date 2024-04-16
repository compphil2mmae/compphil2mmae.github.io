---
title: 
type: landing
  
sections:
  # - block: about.biography
  #   id: about
  #   content:
  #     title: ''
  #     # Choose a user profile to display (a folder name within `content/authors/`)
  #     username: christian.seidel

  - block: collection
    content:
      title: Veranstaltungen
      subtitle: Workshops, Vorträge, Gastvorträge
      text:
      count: 0
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: 'empty'
        exclude_future: false
        exclude_past: false
  - block: collection
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
        exclude_past: true
      offset: 0
      order: desc
      page_type: event
      archive:
        enable: true
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: compact # showcase
      
---