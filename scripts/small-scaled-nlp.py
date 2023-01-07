"""How to do text summarization
Text cleaning
Sentence tokenization
Word tokenization
Word-frequency table
Summarization"""

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
def clean(text):
    nlp = spacy.load("en_core_web_sm")    
    doc = nlp(text)

def tokenize(doc):
    tokens = [token.text for token in doc]
    print(tokens)
    punctuation = punctuation + "\n"
    punctuation
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    print(word_frequencies)

