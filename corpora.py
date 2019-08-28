import nltk
print(nltk.__file__)

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])