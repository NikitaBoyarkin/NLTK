from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

exemle_sentence = "This is example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(exemle_sentence)

filtered_sentence = [w for w in words if not w in stop_words]

"""for w in words:
    if w not in stop_words:
       filtered_sentence.append(w)"""

print(filtered_sentence) 