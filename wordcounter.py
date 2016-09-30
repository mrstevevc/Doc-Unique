'''
Author: Stephen Lester
Last updated: September 30th, 2016
'''

import sys
from tkinter import *
import PyPDF2

def wordcounter(filename, text):
	if filename[0].endswith('.txt'):
		textcounter(filename, text)
#elif filename[0].endswith('.pdf'):
#pdfcounter(filename, text)

def textcounter(filename, text):
	count = {}
	total = 0
	unique_words = 0
	temp_var = 0
	for w in open(filename).read().split():
		if w in count:
			count[w] += 1
		else:
			count[w] = 1
		total += 1
	text[0] = "The total number of words is %d" %total
	text[1] = "The total number of unique words is %d" %len(count)


