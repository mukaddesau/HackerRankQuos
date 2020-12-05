'''
File Name : FibonacciNumbersMemoization.py
Author : Mukaddes Altuntas

Created On : 05/12/2020

Version : Pyhton 3.7.4

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the n'th fibonacci number using one of the dynamic programming
			   tecniques which is memoization.  
'''
				
# 1, 2, 3, 4, 5, 6, 7,  8,  9,  10,...
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

# We can find the nth fibonacci number to down from top step by step.
# We use the MEMOIZATION (TOP-DOWN) technique in which results of overlapping subproblems
# are cached and then they are reused later without recomputing. 

# memo dictionary is created as default even if the user does not give it as an argument to the function.
def FibonacciNumbersMemoization(n, memo = {}):

	# check if nth fibonacci number is saved beforehand. If it is saved, you do not have to 
	# recompute it, just use its value. 
	if n in memo:
		return memo[n]

	# stop point of the recursion. 
	if n <= 2:
		return 1

	# After computation of the nth fibonacci number, add it to the memo dictionary. 
	memo[n] = FibonacciNumbersMemoization(n-1) + FibonacciNumbersMemoization(n-2)
	return memo[n]



while True:
	print("Enter 1 to find the nth Fibonacci number.")
	print("Enter 2 to quit.")
	print("-----------------------------------------------------------")


	userChoice = int(input())

	if userChoice is 1:
		print("Enter n value: ")
		n = int(input())

		fibonacciN = FibonacciNumbersMemoization(n)

		print("************************************************************")
		print("The {}th Fibonacci number: {}".format(n,fibonacciN))
		print("************************************************************")

	elif userChoice is 2:
		print("You are quited the program.")
		print("-----------------------------------------------------------")
		quit()

	else:
		print("Wrong choice!!!")	
	