
import csv
import sys
import time
import numpy as np


words = list()

with open('most100.txt', 'r') as fre:
	for line in fre:
		words.append(line.strip("\n"))



with open('dev_most100.csv', 'r') as dev:
	data = list(csv.reader(dev))


dev = list()
c = 0
for i in range(0, 30):
	term = list()
	term.append(data[i][0])
	for j in range(1, 101):
		
		ex = words[j-1]
		
		if (data[i][j] == "1"):
			term.append(ex)
		elif (data[i][j] == "2"):
			term.append(ex)
			term.append(ex)
		elif (data[i][j] == "3"):
			term.append(ex)
			term.append(ex)
			term.append(ex)

	dev.append(term)


for line in dev:
	print line
