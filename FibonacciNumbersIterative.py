'''
File Name : FibonacciNumbersIterative.py
Author : Mukaddes Altuntas

Created On : 04/12/2020

Version : Pyhton 3.7.4

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the n'th fibonacci number iteratively. 
'''
				
# 1, 2, 3, 4, 5, 6, 7,  8,  9,  10,...
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

import numpy as np 

def FibonacciNumbersIterative(n):
	# fibonacci numbers will be kept in an array.
	# fibonacci[0] = 1
	# fibonacci[1] = 1
	fibonacciNumbers = np.ones(n)
	
	# fibonacci[2] = fibonacci[0] + fibonacci[1]
	# fibonacci[3] = fibonacci[1] + fibonacci[2]
	# fibonacci[4] = fibonacci[2] + fibonacci[3]
	# fibonacci[5] = fibonacci[3] + fibonacci[4]
	# fibonacci[6] = fibonacci[4] + fibonacci[5]
	# fibonacci[7] = fibonacci[5] + fibonacci[6]
	# ................
	# We can find the nth fibonacci number to up from down step by step.
	# We use the TABULATION (BOTTOM-UP) technique in which solved subproblems
	# in a sequence to bigger from smaller. 
	for i in range (n-2):
		fibonacciNumbers[i+2] = fibonacciNumbers[i] + fibonacciNumbers[i+1]

	return int(fibonacciNumbers[n-1])

while True:
	print("Enter 1 to find the nth Fibonacci number.")
	print("Enter 2 to quit.")
	print("-----------------------------------------------------------")


	userChoice = int(input())

	if userChoice is 1:
		print("Enter n value: ")
		n = int(input())

		fibonacciN = FibonacciNumbersIterative(n)

		print("************************************************************")
		print("The nth Fibonacci number: ", fibonacciN)
		print("************************************************************")

	elif userChoice is 2:
		print("You are quited the program.")
		print("-----------------------------------------------------------")
		quit()

	else:
		print("Wrong choice!!!")	
	