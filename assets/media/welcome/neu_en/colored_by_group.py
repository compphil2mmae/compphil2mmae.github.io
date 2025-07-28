#!/usr/bin/env python
"""
Colored by Group Example
========================

Generating a word cloud that assigns colors to words based on
a predefined mapping from colors to words
"""

from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt


class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.

       Uses wordcloud.get_single_color_func

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

text = """consequentialism
computational methods
moralism
science
climate ethics
argumentative analysis
moral theory
LLMs
Mill
dialectical structures
Sidgwick
AI
autonomy
scientific controversies
ethics of risk
epistemic agency
impartialism
deliberative quality
hedonism
public deliberation
intuitionism
probability
altruism
uncertainty
egoism
logical analysis
hate speech
debate dynamics
EEC Jones
democracy
Whewell
risk
Parfit
rationality
reasons
argument maps
egalitarianism
reflective equilibrium
state mass surveillance
justification
climate models
climate engineering
prediction
vagueness
economics
justice
reasoning
self-determination
confirmation
decision theory
identity
Bayesianism
"""
# Since the text is small collocations are turned off and text is lower-cased
# wc = WordCloud(collocations=False).generate(text.lower())
wc = WordCloud(collocations=False,
               background_color=None,
               mode='RGBA',
               font_path="/usr/share/fonts/truetype/Fira_Sans/FiraSans-Regular.ttf",
               width=1920,#               width=1140,
               height=700,#               height=465,
               relative_scaling=0.3,
               regexp="[ \w\.\-]+").generate(text)

color_to_words = {
    # words below will be colored with a green single color function
    'seagreen': ['consequentialism',
                 'hate speech',
                 'moralism',
                 'climate ethics',
                 'autonomy',
                 'Mill',
                 'Sidgwick',
                 'EEC Jones',
                 'impartialism',
                 'moral theory',
                 'Whewell',
                 'Parfit',
                 'reasons',
                 'hedonism',
                 'intuitionism',
                 'altruism',
                 'egoism',
                 # 'democracy',
                 # 'science',
                 'ethics of risk',
                 'vagueness',
                 'justice',
                 'state mass surveillance',
                 #'KI',
                 'egalitarianism',
                 'self-determination',
                 'rationality',
                 'identity'],
    # will be colored with a red single color function
    'cornflowerblue': ['computational methods',
                       'science',                       
                       'argumentative analysis',
                       'LLMs',
                       'dialectical structures',
                       'AI',
                       'scientific controversies',
                       'epistemic agency',
                       'deliberative quality',
                       'public deliberation',
                       'probability',
                       'uncertainty',
                       'logical analysis',
                       'debate dynamics',
                       'democracy',
                       'risk',
                       #'rationality',
                       'argument maps',
                       'reflective equilibrium',
                       'justification',
                       'climate models',
                       'climate engineering',
                       'prediction',
                       'economics',
                       'reasoning',
                       'confirmation',
                       'decision theory',
                       'Bayesianism']
}

# Words that are not in any of the color_to_words values
# will be colored with a grey single color function
default_color = 'red'

# Create a color function with single tone
# grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)

# Create a color function with multiple tones
grouped_color_func = GroupedColorFunc(color_to_words, default_color)

# Apply our color function
wc.recolor(color_func=grouped_color_func)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
from os import path
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# the path to save worldcloud
imgname1 = 'output.png'
imgname2 = 'output.svg'
wc.to_file(path.join(d, imgname1))
#wc.to_svg(path.join(d, imgname2))

# Plot
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
