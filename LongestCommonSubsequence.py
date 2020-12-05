'''
File Name : LongestCommonSubsequence.py
Author : Mukaddes Altuntas

Created On : 03/12/2020

Version : Pyhton 3.7.4

Copyright (c) 2020 Mukaddes Altuntas. All rights reserved.

Description : This program finds the longest subsequences between two strings using dynamic programming. 
			  The subsequence does not have to consist of consecutive letters but,
			  order of letters is important. 
			  The longest common subsequence is a dynamic programming problem which is solved by tabulation method.
			  The tabulation is a bottom-up technique comprising of table-filling.
'''

import numpy as np

# create a table comprising of number of common letters between two strings.
def createTable(str1, str2):
	table = np.zeros((len(str1)+1 , len(str2)+1))

	for i in range (1 , len(str1)+1):
		for j in range(1 , len(str2)+1):

			# if the letter that we are looking at is common,
			# add one to previous situation.
			# previous situation is parts of the strings that we looked at in previous step.
			if str1[i-1] == str2[j-1]:
				table[i,j] = table[i-1, j-1] + 1

			# if the letter is not common,
			# take the max one of the previous two situations.
			else:
				table[i,j] = max(table[i-1, j], table[i, j-1])

	return table

# find Common Letters to top from bottom.
def findCommonLetters(table,str1,str2):
	commonLetters = []
	i , j = table.shape[0] - 1 , table.shape[1] - 1

	while(i != 0 and j != 0):
	
		if table[i, j] == table[i-1, j]:
			i -= 1

		elif table[i, j] == table[i, j-1]:
			j -= 1

		else:
			commonLetters.append(str1[i-1])
			i -= 1
			j -= 1

	return commonLetters	

while True:
	print("Enter 1 find the longest subsequences between two strings.")
	print("Enter 2 to quit.")
	print("-----------------------------------------------------------")


	userChoice = int(input())

	if userChoice is 1:
		print("Enter the first sequence: ")
		str1 = input()
		print("Enter the second sequence: ")
		str2 = input()

		table = createTable(str1, str2)
		commonLetters = findCommonLetters(table, str1, str2)
		print("************************************************************")
		print("Strings: ", str1, str2)
		print("The longest common subsequence: ", ''.join(commonLetters[::-1]))
		print("************************************************************")

	elif userChoice is 2:
		print("You are quited.")
		print("-----------------------------------------------------------")
		quit()

	else:
		print("Wrong choice!!!")	
	





