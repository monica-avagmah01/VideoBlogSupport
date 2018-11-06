#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:39:38 2018

@author: monica
"""

import nltk
#ntlk.download('punkt')
#nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = """Thank you all so very much. Thank you to the Academy. 
Thank you to all of you in this room. 
I have to congratulate the other incredible nominees this year. 
The Revenant was the product of the tireless efforts of an unbelievable cast 
and crew. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your 
talent on screen can only be surpassed by your friendship off screen … thank you
 for creating a transcendent cinematic experience. Thank you to everybody at Fox
 and New Regency … my entire team. I have to thank everyone from the very onset
 of my career … To my parents; none of this would be possible without you. And 
 to my friends, I love you dearly; you know who you are."""
 
 
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(words)

lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words]
    sentences[i] = ' '.join(words)


for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [word for word in words if word not in stopwords.words('english')]
    sentences[i] = ' '.join(words)

