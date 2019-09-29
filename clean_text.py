import pandas as pd 
import numpy as np
from nltk import RegexpTokenizer 
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer,PorterStemmer
import sys

tokenizer=RegexpTokenizer(r'\w+')
sw=set(stopwords.words('english'))
ps = PorterStemmer()

def getCleanedReview(review):
	review=review.replace('<br /><br />'," ")
	tokens=tokenizer.tokenize(review.lower())
	new_tokens=[w for w in tokens if w not in sw]
	stemmed_tokens=[ps.stem(w) for w in new_tokens]
	cleaned_tokens=' '.join(stemmed_tokens)
	return cleaned_tokens

#reading from input file and outputing to output file.

