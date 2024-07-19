---
title: Veranstaltungen
type: landing
  
sections:

  - block: collection
    content:
      title: Veranstaltungen
      subtitle: "[Workshops](#workshops), [Vorträge](#talks), [Gäste](#guests)"
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

  # - block: slider
  #   content:
  #     slides:
  #     - title: '[Workshops](#workshops)'
  #       content: 
  #       align: center
  #       background:
  #         image:
  #           filename: coders.jpg
  #           filters:
  #             brightness: 0.7
  #         position: right
  #         color: '#666'
  #     - title: '[Vorträge](#talks)'
  #       content: 
  #       align: center
  #       background:
  #         image:
  #           filename: contact.jpg
  #           filters:
  #             brightness: 0.7
  #         position: center
  #         color: '#555'
  #     - title: '[Gäste](#guests)'
  #       content: '@ CompPhil²MMAE'
  #       align: center
  #       background:
  #         image:
  #           filename: Logo_ResearchSemiar.png
  #           filters:
  #             brightness: 0.4
  #         position: center
  #         color: '#98AFC7' # '#333'
  #       # link:
  #       #   icon: graduation-cap
  #       #   icon_pack: fas
  #       #   text: Join Us
  #       #   url: '#news.cs'
  #   design:
  #     # Slide height is automatic unless you force a specific height (e.g. '400px')
  #     slide_height: '400px'
  #     is_fullscreen: false
  #     # Automatically transition through slides?
  #     loop: true
  #     # Duration of transition between slides (in ms)
  #     interval: 4000

  - block: collection
    id: workshops
    content:
      title: Workshops 
      subtitle: # 'des CompPhil²MMAE-Teams'
      text:   
      count: 0
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: Workshops
        exclude_future: false
        exclude_past: true
      offset: 0
      order: asc #desc
      page_type: event
      archive:
        enable: true
        text: Alle <strong>Workshops</strong> 
    design:
      columns: '2'
      view: compact # showcase

  - block: collection
    id: talks
    content:
      title: Vorträge 
      subtitle: # 'des CompPhil²MMAE-Teams'
      text:   
      count: 0
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: Vortrag
        exclude_future: false
        exclude_past: true
      offset: 0
      order: asc #desc
      page_type: event
      archive:
        enable: true
        text: Alle <strong>Vorträge</strong> 
    design:
      columns: '2'
      view: compact # showcase

  - block: collection
    id: guests
    content:
      title: Gäste 
      subtitle: '@ CompPhil²MMAE'
      text:   
      count: 0
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: Gastvortrag
        exclude_future: false
        exclude_past: true
      offset: 0
      order: asc # desc
      page_type: event
      archive:
        enable: true
        text: Alle <strong>Gastvorträge</strong> 
    design:
      columns: '2'
      view: compact # showcase

---