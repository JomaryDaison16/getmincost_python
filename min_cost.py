# !/bin/python3

import math
import os
import random
import re
import sys


def getMinimumCost(k, c):
	Cost = 0 #Initialize the total cost
	NumPurchase = 0 #Initialize number of costumer's purchase

	c.sort(reverse=True)

	if n >= 0 and k > 0: #Check if the input is valid k should be 1 or more and n should not have negative value
		if (n >= 0 and n <= k):
			for i in range(n):
				Cost += 1 * c[i]
			return Cost
		
		elif(n > k):
			for i in range(n):
				Cost += (NumPurchase + 1) * c[i]
				if (i+1)%k==0:
					NumPurchase += 1
			return Cost
		
		else:
			print("Please enter valid Input")
	else:
			print("Please enter valid Input")



if __name__ == "__main__":
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	c = list(map(int, input().rstrip().split()))

	print(getMinimumCost(k, c))
