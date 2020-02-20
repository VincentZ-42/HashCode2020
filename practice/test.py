# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vzhao <vzhao@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/19 11:56:47 by vzhao             #+#    #+#              #
#    Updated: 2020/02/19 16:00:17 by vzhao            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def subset_sum(file, OG, numbers, target, partial =[]):
	"""
	Function traverses through list of numbers to find the combination
	that matches the target value (Function runs recursively)
	Args:
	(file) file = the file id that we will write into
	(list) OG = original set of numbers
	(list) numbers = list of pizza types that is changed throughout recursion
	(int) target = the total number of pizzas we want
	(list) partial = list placeholder we use to hold the different types of pizzas
	Returns:
	Nothing...recursion stops once all combinations are found
	"""
	s = sum(partial)
	
	if s == target:
		file.write(str(len(partial)))
		file.write("\n")
		for j in range(len(partial)):
			file.write(str(OG.index(partial[j])))
			if j < len(partial) - 1:
				file.write(" ")
		file.write("\n")
	if s >= target:
		return 

	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		subset_sum(file, OG, remaining, target, partial + [n])

a_in = open("a_example.in", "r")	# This opens the text file and saves it into a variable
b_in = open("b_small.in", "r")
c_in = open("c_medium.in", "r")
d_in = open("d_quite_big.in", "r")
e_in = open("e_also_big.in", "r")

# -----------------------------Change this to get different outputs--------------------
# Reads the entire file and saves it into list
# Replace......
# a_in --> b_in (input from example b)
# a_out --> b_out (output of example b)
# "a_out" --> b_out (path name of newly created output file)
lines = c_in.readlines()		# Change a_in to b_in
a_out = open("c_out", "w")		# Change "a_out" to b_out
file_path = "c_out"				# Change "a_out" to b_out
#---------------------------------------------------------------------------------------

slices, types = map(int, lines[0].split())		# Splits the first line into int variales
pizzas = map(int, lines[1].split())				# Splits the 2nd line into list of integers

# This checks if the file is empty or not
# Can also use os.stat(file_path).st_size == 0 as condition
if os.path.getsize(file_path) == 0:
	print "File is empty"
else:
	print "File is not empty"

while os.path.getsize(file_path) == 0:
	a_out = open(file_path, "w")
	subset_sum(a_out, pizzas, pizzas, slices)
	slices -= 1
	a_out.close()

if os.path.getsize(file_path) == 0:
	print "File is empty"
else:
	print "File is not empty"

a_in.close()
b_in.close()
c_in.close()
d_in.close()
e_in.close()
