# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_books.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vzhao <vzhao@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/20 10:11:23 by vzhao             #+#    #+#              #
#    Updated: 2020/02/20 13:18:59 by vzhao            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

a_in = open("a_example.txt")
b_in = open("b_read_on.txt")

def total_libary_score(library, bookscore):
	"""
	Traverses libary to see maximum score of library
	"""
	score = sum(x for x in library['books'])
	score 
	return score

def check_if_scanned(scanned, book_number):
	"""
	Checks if a certain book has been scanned already
	Args:
	scanned = int array of books that has been scanned
	book_number = book number that is being scanned
	"""
	for element in scanned:
		if book_number == element:
			return (1)
	return (0)

def find_max(library):
	max = 0

	for each in library:
		if library[each]['used'] == False:
			if max < library[each]['max_score']:
				max = library[each]['max_score']
	return (max)

def find(lst, key, value):
	for i, dic in enumerate(lst):
		if dic[key]['used'] == False:
			if dic[key] == value:
				return i
	return -1

data = a_in.readlines()
num_books, num_library, days_for_scanning = map(int, data[0].split())
ind_book_scores = list(map(int, data[1].split()))

total_max = sum(ind_book_scores)
bookscore = {}
for i in range(num_books):
	bookscore[i] = ind_book_scores[i]

library = {}
# for i in range(num_library):
# 	library[i] = {}
# 	t_books, signup, ship = map(int, data[2 + 2*i].split())
# 	library[i]['name'] = i
# 	library[i]['signup'] = signup
# 	library[i]['ship'] = ship
# 	library[i]['t_books'] = t_books
# 	library[i]['books'] = {}
# 	tmp = list(map(int, data[2 + (2*i + 1)].split()))
# 	library[i]['books'] = {key: bookscore[key] for key in bookscore.keys() & tmp}
# 	library[i]['Used'] = False
# 	# max_score added

for i in range(num_library):
    library[i] = {}
    t_books, signup, ship = map(int, data[2 + 2*i].split())
    library[i]['name'] = i
    library[i]['signup'] = signup
    library[i]['ship'] = ship
    library[i]['t_books'] = t_books
    book_id_with_score = {}
    tmp = list(map(int, data[2 + (2*i + 1)].split()))
    book_id_with_score = {key: bookscore[key] for key in bookscore.keys() & tmp}
    t = (days_for_scanning - signup) * library[i]['ship']
    limit = (lambda: t_books, lambda: t)[t < t_books]()
    s = {}
    s = sorted(book_id_with_score.items(), reverse=True, key=lambda x: x[1])[:limit]
    score = sum([pair[1] for pair in s])
    library[i]['max_score'] = score
    library[i]['books'] = sorted(book_id_with_score.items(), reverse=True, key=lambda x: x[1])[:limit]
    library[i]['used'] = False

res = sorted(library.items(), reverse=True, key = lambda x: x[1]['max_score'])
points = 0
lib_count = 0
while days_for_scanning > 0:
	potential_points = res[lib_count][1]['max_score']
	print ("potential points = ", potential_points)
	# days_for_scanning -= res[lib_count][1]['signup']
	if days_for_scanning - res[lib_count][1]['signup'] > 0:
		if res[lib_count][1]['used'] == False:
			points += potential_points
			res[lib_count][1]['used'] = True
			days_for_scanning -= res[lib_count][1]['signup']
			del res[lib_count]
	# library_used = find(library, 'max_score', potential_points)
	print ("points = ", points)
	print ("days left for scanning = ", days_for_scanning)
	print ("total max = ", total_max)
	# days_for_scanning -= 1
	if points == total_max:
		break


# print (res[0])
# del res[0]
# print (res[0])