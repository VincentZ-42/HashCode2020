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
lines = b_in.readlines()		# Change a_in to b_in
a_out = open("b_out", "w")		# Change "a_out" to b_out
file_path = "b_out"				# Change "a_out" to b_out
#---------------------------------------------------------------------------------------

slices, types = map(int, lines[0].split())		# Splits the first line into int variales
pizzas = map(int, lines[1].split())				# Splits the 2nd line into list of integers

ans = []
pizza_holder = []
for i in range(types):
	ans.append(slices - pizzas[i])
print "ans array = %s" % ans
for j in range(types):
	print "index = %d" % j
	for element in pizzas:
		if ans[j] - element == 0:
			ans[j] -= element
			print element
			pizza_holder.append(element)
			break
	if pizza_holder:
		break
pizza_holder.append(pizzas[j])
print (pizza_holder)