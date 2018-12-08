'''
Two strings are said to be anagrams of one another if you can turn the first string into
the second by rearranging its letters. For example, "table" and "bleat" are anagrams, as
are "tear" and "rate." Your job is to write a function that takes in two strings as input and
determines whether they're anagrams of one another.

Solution should run in O(n1 + n2)
There are two solutions:
	one is using counter
	another one is also using dictionary, but slightly faster. (tests say it's actually not)
'''
from collections import Counter
import random
import string
import time
def are_anagrams(str1, str2):
	if len(str1) != len(str2):
		return False
	dict1 = Counter(str1)
	dict2 = Counter(str2)
	for char in dict1:
		if not char in dict2 or dict2[char] != dict1[char]:
			return False
	return True

assert are_anagrams('table', 'bleat') == True
assert are_anagrams('table', 'bleate') == False
assert are_anagrams('honey', 'eyhon') == True
assert are_anagrams('area', 'are') == False
assert are_anagrams('', '') == True

def are_anagrams_fast(str1, str2):
	if len(str1) != len(str2):
		return False

	char_dict = {}
	for char in str1:
		if not char in char_dict:
			char_dict[char] = 0
		char_dict[char] += 1

	for char in str2:
		if char not in char_dict or char_dict[char] <= 0:
			return False
		char_dict[char] -= 1
	return True

assert are_anagrams_fast('table', 'bleat') == True
assert are_anagrams_fast('table', 'bleate') == False
assert are_anagrams_fast('honey', 'eyhon') == True
assert are_anagrams_fast('area', 'are') == False
assert are_anagrams_fast('', '') == True

def time_test():
	"""a time test to evaluate the performance two methods
	results say anagrams_fast takes almost twice as much time :( """
	loops = 10000
	A = ""
	B = ""
	for x in range(1000):
		A = A + random.choice(string.ascii_letters)
	
	A_shuff = list(A)
	random.shuffle(A_shuff)
	A_shuff = "".join(A_shuff)

	s = time.clock()
	for i in range(loops):
		are_anagrams(A, A_shuff)
	e = time.clock()
	print("time by are_anagrams \t", e -s)
	s = time.clock()
	for i in range (loops):
		are_anagrams_fast(A, A_shuff)
	e = time.clock()
	print("time by are_anagrams_fast\t", e -s)

time_test()


