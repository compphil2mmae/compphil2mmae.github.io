---
title: Forschung
date: 2024-04-01

type: landing

sections:
  - block: portfolio
    id: projects
    content:
      title: Forschungsprojekte
      filters:
        folders:
          - research
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: Alle
          tag: '*'
        - name: Computationale Philosophie
          tag: Computationale Philosophie
        - name: LLMs
          tag: LLMs
        - name: Norms of (Public) Reasoning
          tag: Norms of Public Reasoning
        - name: Philosophische Methoden
          tag: Philosophische Methoden
        - name: Moralphilosophie
          tag: Moralphilosophie
        - name: Angewandte Ethik
          tag: Angewandte Ethik
        - name: Britische Moral- & Sozialphilosophie des 19. Jh.
          tag: BMSP19
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      view: showcase-authors
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false

  # - block: slider
  #   content:
  #     slides:
  #     - title: 👋 Welcome to the group
  #       content: Take a look at what we're working on...
  #       align: center
  #       background:
  #         image:
  #           filename: coders.jpg
  #           filters:
  #             brightness: 0.7
  #         position: right
  #         color: '#666'
  #     - title: Lunch & Learn ☕️
  #       content: 'Share your knowledge with the group and explore exciting new topics together!'
  #       align: left
  #       background:
  #         image:
  #           filename: contact.jpg
  #           filters:
  #             brightness: 0.7
  #         position: center
  #         color: '#555'
  #     - title: World-Class Semiconductor Lab
  #       content: 'Just opened last month!'
  #       align: right
  #       background:
  #         image:
  #           filename: welcome.jpg
  #           filters:
  #             brightness: 0.5
  #         position: center
  #         color: '#333'
  #       link:
  #         icon: graduation-cap
  #         icon_pack: fas
  #         text: Join Us
  #         url: ../contact/
  #   design:
  #     # Slide height is automatic unless you force a specific height (e.g. '400px')
  #     slide_height: ''
  #     is_fullscreen: true
  #     # Automatically transition through slides?
  #     loop: false
  #     # Duration of transition between slides (in ms)
  #     interval: 2000
---
