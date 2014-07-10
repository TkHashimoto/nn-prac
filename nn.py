#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import csv
from functools import reduce

"""
	Practice of Naive Parceptron
"""
def StepFunc(val):
	return -1 if val<0 else 1

class BaseEstimator:
	def __init__(self):
		pass

	def fit(self, input_vectors):
		# must be Overriden
		return 0

	def output(self,input_vector):
		return self.threasholding(input_vector)

class BluePredictor(BaseEstimator):
	def __init__(self, coef=0.1, thresh_func=StepFunc):
		self.w = [ (random.random()-0.5)*2, (random.random()-0.5)*2, (random.random()-0.5)*2 ]
		print("coef = {0}".format(coef))
		print("w = [{0},\n    {1},\n    {2}]".format(self.w[0], self.w[1], self.w[2]))
		self.threshold_func = thresh_func
		self.coef = coef
		self.n = 0

	def fit(self, input_vectors):
		flag = []
		# scaling input_vector
		scaled_input_vectors = [ [elm/255.0 for elm in v[1:]] for v in input_vectors ]
		for v in scaled_input_vectors:	
			# calc sum of a unit
			total = sum([v[i]*self.w[i] for i in range(len(self.w))])
			
			# calc output
			result = self.threshold_func(total)
			
			if not v[0] == result:
				if v[0] == 1:
					flag.insert(len(flag), 1)
				else:
					flag.insert(len(flag),-1)
			else:
				flag.insert(len(flag), 0)
		
		for i in range(len(scaled_input_vectors)):
			if not flag[i] == 0:
				#print("	{0}\n	{1}\n	{2}\n	{3}".format(self.w, flag[i], self.coef, scaled_input_vectors[i]))
				self.w = [self.w[j] + flag[i] * self.coef * scaled_input_vectors[i][j]\
							for j in range(len(self.w))]	
		print("w' = [{0},\n     {1},\n     {2}]".format(self.w[0], self.w[1], self.w[2]))	
		tmp = reduce(lambda a,b: abs(a)+abs(b), flag)
		if not tmp == 0:
			print("##### GoTo Next cycle... next_index={0} #####".format(self.n))
			print("Total defference: {0}".format(tmp))
			self.n += 1
			self.fit(input_vectors)
		else: 
			print("Finish.")
			print("Loop = {0}".format(self.n))
	
	def predict(v):
		return self.threshold_func(sum([v[i]*self.w[i] for i in range(v)]))

def main():
	train = [[float(elm) for elm in row] for row in csv.reader(open("train"))]
	bp = BluePredictor(coef=0.001)
	bp.fit(train)

if __name__=="__main__":
	main()
