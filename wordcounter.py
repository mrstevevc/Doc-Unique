'''
Author: Stephen Lester
Last updated: September 30th, 2016
'''

import sys
from tkinter import *


def wordcounter(filename, text):
	textcounter(filename, text)

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


