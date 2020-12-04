'''
File Name : FibonacciNumbersRecursive.py
Author : Mukaddes Altuntas

Created On : 04/12/2020

Version : Pyhton 3.7.4

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the n'th fibonacci number using recursion. 
'''
				
# 1, 2, 3, 4, 5, 6, 7,  8,  9,  10,...
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# fibonacci[0] = 1
# fibonacci[1] = 1
# fibonacci[2] = fibonacci[0] + fibonacci[1]
# fibonacci[3] = fibonacci[1] + fibonacci[2]
# fibonacci[4] = fibonacci[2] + fibonacci[3]
# fibonacci[5] = fibonacci[3] + fibonacci[4]
# fibonacci[6] = fibonacci[4] + fibonacci[5]
# fibonacci[7] = fibonacci[5] + fibonacci[6]
# .............

def FibonacciNumbersRecursive(n):
	if n <= 2:
		return 1
	return FibonacciNumbersRecursive(n-1) + FibonacciNumbersRecursive(n-2)

while True:
	print("Enter 1 to find the nth Fibonacci number.")
	print("Enter 2 to quit.")
	print("-----------------------------------------------------------")


	userChoice = int(input())

	if userChoice is 1:
		print("Enter n value: ")
		n = int(input())

		fibonacciN = FibonacciNumbersRecursive(n)

		print("************************************************************")
		print("The nth Fibonacci number: ", fibonacciN)
		print("************************************************************")

	elif userChoice is 2:
		print("You are quited the program.")
		print("-----------------------------------------------------------")
		quit()

	else:
		print("Wrong choice!!!")	
	