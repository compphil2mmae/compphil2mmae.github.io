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
      - title: '[Publications](#pubs)'
        content: 
        align: center
        background:
          image:
            filename: books.jpg
            filters:
              brightness: 0.5
          position: right
          color: '#666'
      - title: '[Talks](#talks)'
        content: 
        align: center
        background:
          image:
            filename: talk.jpg
            filters:
              brightness: 0.6
          position: center
          color: '#555'
      - title: '[News](#news)'
        content: 
        align: center
        background:
          image:
            filename: news.png
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
      slide_height: '400px'
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
      title: Publications
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
      title: Books
      subtitle: Monographes & Edited Collections
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
        text: All <strong>talks</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase

  - block: collection
    content:
      title: Articles 
      subtitle: in journals
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
        text: All <strong>talks</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    

  - block: collection
    content:
      title: Articles 
      subtitle: in collections
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
        text: All <strong>talks</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    

  - block: collection
    content:
      title: Reviews
      subtitle: Bibliographies etc.
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
        text: All <strong>talks</strong> 
    design:
      columns: '2'
      view: citation # compact # showcase    


  - block: collection
    id: talks
    content:
      title: Talks
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
        text: All <strong>talks</strong> 
    design:
      columns: '2'
      view: compact # showcase

  - block: collection
    id: news
    content:
      title: News 
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
      #   text: Weitere <strong>News</strong> 
      #   position: center
      #   link: post/
    design:
      view: compact # showcase # compact  
      columns: '2'
      flip_alt_rows: true
    
---