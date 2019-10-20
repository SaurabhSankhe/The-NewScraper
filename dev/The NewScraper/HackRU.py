#!/usr/bin/env python
# coding: utf-8

# In[1]:
import json
import requests
from urllib.request import urlopen
import newspaper
from newspaper import Article
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize 
def processing():
	url = ('https://newsapi.org/v2/top-headlines?'
		'country=us&'
		'apiKey=36a24dc9d4c84ec0a0fe7920ec643195')
	response = requests.get(url)
	a=json.loads(response.text)
	text=a['articles'][0]['url']
	#print(text)
	cnn_paper_1 = newspaper.build('https://www.cnn.com/', language='en')
	#for category in cnn_paper_1.category_urls():
    #print(category)
	article = Article(text)
	article.download()
	article.parse()
	article.title
	a=article.text
	article.nlp()
	output=article.summary
	#string.punctuation
	#clean = a.replace("\n", "")
	#clean
	return output,article.title
