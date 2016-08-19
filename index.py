#!/usr/bin/env python

import numpy as np
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

from tabulate import tabulate
from LetrasCom import LetrasCom


def main():
  nltk.download()
  stop_spa = stopwords.words('spanish')

  words = [w for w in LetrasCom.get_words() if w not in stop_spa]

  print tabulate(bow(words), headers=['Word', 'Count'], tablefmt='orgtbl')


def bow(palabras):
  vectorizer = CountVectorizer(
    analyzer     = "word", \
    tokenizer    = None,   \
    preprocessor = None,   \
    stop_words   = None,   \
    max_features = 5000
  )

  data_features = vectorizer.fit_transform(palabras).toarray()

  vocab = vectorizer.get_feature_names()
  dist  = np.sum(data_features, axis=0)
  dicc  = zip(vocab, dist)

  return sorted(dicc, key = lambda x: x[1], reverse = True)


if __name__ == '__main__':
    main()
