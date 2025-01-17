# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def ner(text):
    st = StanfordNERTagger(
        '/var/www/opm/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/var/www/opm/stanford-ner/stanford-ner.jar', encoding='utf-8'
        )

    #text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    entities = []
    for i in classified_text:
        if i[1] != 'O':
            entities.append(i)

    return entities
