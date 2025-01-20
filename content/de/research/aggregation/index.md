---
title: Belief aggregation on argument maps in diverse and polarised groups
summary: When citizens and their governments rely on expert panels for policy advice, should they favour a diversified group  composition? Should they avoid polarised expert panels?  
tags:
  - Computationale Philosophie
  - Norms of Public Reasoning
  - Angewandte Ethik
date: '2024-07-01T00:00:00Z'
type: 'project'
authors: 
  - felix.kopecky
  - gregor.betz

# Optional external URL for project (replaces project detail page).
#external_link: 'https://debatelab.philosophie.kit.edu/'

image:
  # caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ''
---
When citizens and their governments rely on expert panels for policy
advice, should they favour a diversified group composition? Should they avoid
polarised expert panels? 

In this project we estimated epistemic group performance as the ability to avoid logical
inconsistencies in sentence-wise majority voting.
These inconsistencies can arise in groups that aggregate beliefs even if
all group members hold individually consistent beliefs (List & Pettit 2002). 
Although it is not a sufficient condition for reaching the optimal
solution, forming a consistent group opinion is a necessary condition
for decent advice to politicians and the public, and it is a
particularly important indicator when the optimal solution is uncertain.

In our agent-based model, we observed inconsistent aggregation
predominantly in highly diverse, but not in highly polarised or
moderately diverse groups. This effect is amplified by encoding more inferential
information in the model. There seems to be a penalty for being diverse in rich
but imperfect information environments.

These results suggest that epistemic problem solving might be more difficult
for expert panels with high opinion diversity. We also see important questions 
about which expectations we may reasonably hold towards expert panels that 
evaluate inconclusive, permissive evidence at short notice.

## Methods

We model group decision tasks through argument maps. Given that agents
vote about advising acceptance or rejection of $p_1, p_2,...,p_n$, these maps
contain reasons in favour, against, or generally about these issues. Agents in
our model form beliefs about every proposition under discussion by
assigning a truth value to it. An example for a decision scenario is
given in this Figure:

![Illustration of a synthetically generated tree-like argument map.
$p_0$, $p_1$, and $p_2$ are key statements for this map: they are
conclusions for arguments at the root of the tree. Support relations
between arguments are expressed by solid arrows, defeats by dashed
ones.](synthetised-debate.png)

All agents in the model must hold beliefs that allow all presented
arguments to be valid. We assume that agreement on validity makes
aggregating diverse opinions more interesting, since inconsistencies in
our model do not arise from disputed argument quality or relevance.

Our goal was to understand whether groups are more or less likely to
aggregate inconsistent group opinions on argument maps depending on their 
opinion diversity and belief polarisation scores. We measured opinion diversity 
through the Gini-Simpson index (Tuomisto 2010), and polarisation in terms
of statistical dispersion (Bramson et al. 2017). We synthesised thousands of argument
maps as well as groups that all hold validity-respecting views in light of these 
maps, but that have varying opinion diversity and belief polarisation.

## Results

These two Figures plot the inconsistency prevalence
for diverse (above) and polarised (below) groups:

![Coherence of group opinion in 1960 samples of 51 agents with varying
diversity, expressed as the Gini-Simpson index, and varying
informational influence, expressed as inferential
density.](Experiment-Diversity.png)

![Coherence of group opinion in 2054 samples of 51 agents with varying
polarisation, measured as dispersion, and inferential
density.](Experiment-Polarisation.png)

A single measurement is
a consistency query for a sample of 51 agents. The complexity of the
argument map is measured in terms of inferential density. An
inferentially dense map imposes more validity constraints on the agent's
belief systems (please see our paper for an in-depth treatment of density).

Inconsistent majority opinions are much more likely in diverse than in
homogeneous samples. This is true across different degrees of
informational influence, but a higher inferential density increases the
prevalence of inconsistent aggregation in diverse groups. Groups with a
Gini-Simpson index below 0.5 rarely aggregate their beliefs to
inconsistent group opinions – incoherence is only a risk for diverse
groups. With increasing inferential density, inconsistent aggregations
become somewhat more likely in less diverse groups too, but the risk of
inconsistent aggregation rises significantly for diverse groups.

Groups with high polarisation do not show an increased inconsistency
risk. Highly polarised groups with a dispersion above 0.75 mostly
aggregate consistent group opinions, and increasing informational
influence slightly lowers the maximum polarisation at which we observe
inconsistency. Moderately polarised groups show a completely different
picture. In low to medium areas of inferential density, those groups
rarely achieve consistent group opinions. Rising informational influence
seems to help a bit: consistent group judgements become more likely
overall, and particularly so for moderately polarised groups.

## Conclusions

Are groups with highly diverse beliefs better at epistemic problem
solving, and polarised groups always worse? No – specifically, when
faced with majoritarian aggregation under uncertainty and permissive
evidence, diverse groups are worse problem solvers and polarised groups
succeed in the majority of cases. This is true even if individual
expertise and consistency are guaranteed.

Basing public decision making on homogeneous expert panels incurs a
democratic legitimacy risk. Calls for increased opinion diversity in
such panels are understandable, yet their implementation might reduce
the legitimacy of expert advice through the under-appreciated risk of
inconsistent aggregation.

There are difficult but worthwhile problems related to managing this
kind of inconsistent aggregation. Should citizens and policy makers be
more lenient towards epistemic groups that require extensive deliberation
or additional fact-finding? In how far should expert advise be
superseded in case of inconsistent aggregation, such as by political or moral
ideals? And how should the experts themselves deal with inconsistent majority
opinions when commissioned to advise the public? Should they issue
separate recommendations that are individually consistent but cannot win
a majority among them? Or should they explicitly restrict their
recommendations to issues with a consistent group response?

## Publication
 Kopecky, Felix & Gregor Betz. In print. Inconsistent belief aggregation in 
diverse and polarised groups. *Philosophy of Science*. DOI: [10.1017/psa.2024.29](https://doi.org/10.1017/psa.2024.29).

## References
Bramson, Aaron, Patrick Grim, Daniel J. Singer, William J. Berger, Graham
Sack, Steven Fisher, Carissa Flocken & Bennett Holman. 2017. Understanding 
polarization: Meanings, measures, and model evaluation. *Philosophy
of Science* 84 (1), pp. 115–159. DOI: [10.1086/688938](https://doi.org/10.1086/688938).

List, Christian & Philip Pettit. 2002. Aggregating sets of judgments: An 
impossibility result. *Economics & Philosophy* 18 (1), pp. 89–110. 
DOI: [10.1017/S0266267102001098](https://doi.org/10.1017/S0266267102001098).

Tuomisto, Hanna. 2010. A consistent terminology for quantifying species diversity? 
Yes, it does exist. *Oecologia* 164, pp. 853–860. DOI: [10.1007/s00442-010-1812-0](https://doi.org/10.1007/s00442-010-1812-0]).