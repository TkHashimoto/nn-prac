#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import csv

#output = csv.writer(open("test","w"))
output = csv.writer(open("train", "w"))

for i in range(10000):
	if random.random()>0.6:
		r = random.randint(0,100)
		g = random.randint(0,100)
		b = random.randint(200,255)
	else:
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
	o = 0
	if r<100 and g<100 and b>200:
		o = 1
	else:
		o = -1
	
	output.writerow([o,r,g,b])	
