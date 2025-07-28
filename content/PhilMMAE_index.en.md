---
# Leave the homepage title empty to use the site title
draft: true
title: 
date: 2024-01-01
type: landing

sections:
  - block: hero
    content:
      title: Department **Philosophical Methods, Moral Philosophy & Applied Ethics**
  - block: hero
    content:
      image: 
        filename: wordcloud.png  
      text: |2-
         
        The team of the research area **Philosophical Methods, Moral Philosophy & Applied Ethics (PhilMMAE)** researches and teaches  
        
        - on fundamental questions of moral theory,  
        - the ethics of public discourse,  
        - normative problems in socially relevant, applied contexts such as climate change, surveillance and artificial intelligence, and  
        - British moral and social philosophy of the 19th century.
        
        PhilMMAE is part of the Department of Philosophy at the Karlsruhe Institute of Technology (KIT), where it is responsible for teaching the philosophical foundations.  
    design:  
      background:
        color: white

  - block: collection
    content:
      title: News
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
