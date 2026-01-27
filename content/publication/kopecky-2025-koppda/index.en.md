---
title: 'Polarisation, Diversity, and Dialectical Structures'
subtitle: 'An Argumentation-Based Approach to Computational Social Epistemology'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Felix Kopecky

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-08-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-12-27T22:31:43.930940Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- thesis

# Publication name and optional abbreviated publication name.
publication: 'KIT'
publication_short: ''
publisher: 'Karlsruhe Institute of Technology (KIT)'
address: 'Karlsruhe'

doi: '10.5445/IR/1000183401'

# double line break needed for correct markdown rendering
abstract: "This dissertation is about the study of belief polarisation and opinion diversity in agent-based, computational models. Simulations on these models reveal that beliefs of artificial agents can polarise through deliberation – even if all agents hold a productive mindset and adhere to standards of epistemic rationality. Different deliberative practices affect polarisation dynamics differently in these models. Polarisation dynamics are soothed as agents engage with the beliefs of others in their reasoning. The largest polarisation effect is observed in agents who continuously fortify their own beliefs.

A second result is that, when artificial agents vote on a collective response towards a body of arguments, the probability that their vote yields an inconsistent majority opinion is strongly associated with the group’s opinion diversity. This improves our understanding of the difficulties that diverse groups can face in decision-making. When they can not use majority voting as part of their decision-making, they need to find alternative, likely more demanding, aggregation procedures to settle their difference of opinion.

These results are gathered from computational models based on the theory of dialectical structures. This theory describes deliberation through argument maps. Individual arguments in these maps are composed of premises and conclusions. The beliefs of agents in dialectical structure models are implemented as mappings from the discussed premises and conclusions to discrete truth values.

There are two kinds of dialectical structure models. In the first, agents iteratively add arguments to an evolving argument map, and they update their beliefs following the introductions by others. Both introduction of and response to arguments are constrained by factors that ensure epistemically rational behaviour. Beyond these constraints, agents compose new arguments according to pre-defined argumentation strategies. These strategies can be divided into allocentric and egocentric strategies, the two of which have fundamentally different effects on belief polarisation. The population polarises if agents only follow egocentric strategies, and the population depolarises if they argue allocentrically.

The second kind of dialectical structure model does not evolve through iterative additions of arguments. It instead synthesises an argument map according to an algorithm found in the literature on dialectical structures. An argument map generated in this way poses an epistemic decision problem. Agents are tasked with finding a belief system that jointly accepts the validity of all presented arguments. There are usually many beliefs that meet this criterion, but even more that do not. This decision problem becomes a problem in collective decision-making if agents with different, individually validity-respecting beliefs need to settle on a single belief system to endorse collectively. In the model presented here, agents perform a sentence-wise majority vote to do so. These votes do not necessarily yield a consistent opinion. Analysis of computationally gathered data reveals that inconsistent aggregation is strongly associated with rising opinion diversity, but not with belief polarisation.

'taupy', a new Python implementation for the study of dialectical structures, is implemented and released to the public as part of this dissertation. This implementation provides features that were not previously available. It implements the clustering of agents’ beliefs with two state-of-the-art clustering algorithms, as well as measures of belief polarisation and opinion diversity, a majority voting mechanism, and other features necessary to observe the results presented here. A user guide is supplied in this thesis.

Dialectical structure models improve our understanding of dynamic aspects of concepts, constraints, and norms that we study in philosophy. This makes computational modelling such a fruitful approach to philosophy, particularly in social epistemology. In this thesis, the discovery of belief polarisation under condition of epistemic rationality reveals a dynamic property of our concept of rationality. Computational approaches are a useful addition to philosophical methods because such dynamic aspects would not be accessible from established methods of analysis.

This thesis pursues computational methods out of purely philosophical interest, but it relies on and contributes to inter-disciplinary efforts in several ways. Polarisation and diversity are understood as they are in other fields, and the agent-based modelling presented here is related to sociological models that have similarly suggested arguments as drivers of polarisation.

While this dissertation studies beliefs and their dynamics in artificial, epistemically rational agents, the results are relevant for our understanding of human deliberation and reasoning, too. As a matter of principle, the adherence to norms of epistemic rationality does not prevent the rise of belief polarisation. This means that occurrences of belief polarisation in humans can not automatically be taken as evidence of epistemic shortcomings in any individual. And the issue of inconsistent belief aggregation in groups with diverse opinions illustrates the difficulties groups with epistemic goals can face. This helps us understand the conditions and limitations of experts advising the public, particularly in exceptional situations involving high uncertainty and limited time. Results from this thesis suggest that we should indeed moderate our expectations towards these groups when exceptional circumstances hold.

Epistemically rational belief polarisation and inconsistent belief aggregation are instances of a broader phenomenon. These are cases in which the accumulation of individually rational capabilities does not yield an optimal outcome for the collective. By continuing the study of such intriguing phenomena, we can hope to gain insights into noteworthy conditions of human reasoning, rationality, and decision-making."

# Summary. An optional shortened abstract.
summary: ''

tags: []

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
links:
- name: URL
  icon: open-access
  icon_pack: ai
  url: https://publikationen.bibliothek.kit.edu/1000183401
- name: PhilPapers
  icon: philpapers
  icon_pack: ai
  url: https://philpapers.org/rec/KOPPDA

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  filename: symbolic-images/graduation/symbolic.png
  alt: 'symbolic graduation cap'
  caption: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [aggregation, polarisation]
---
