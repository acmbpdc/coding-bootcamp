#!/bin/python

# Usage:
# python code.py



# Lists

squares = [1, 4, 9, 16, 25]	# list of numbers
names 	= ['rahul', 'mary', 'abdul', 'harshita'] # list of strings
variety = [3, 'jacob', 2.718, True, [9, 8, 7]] # list of varying data types

squares = [1, 4, 9, 16, 25]
print(len(squares))	# returns the number of elements in the list

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list[0])		# 1st element from the front
print(my_list[5])		# 5th element from the front
print(my_list[9])		# 9th element from the front
print(my_list[-1])		# 1st element from the back
print(my_list[-5])		# 5th element from the back
print(my_list[-10])		# 10th element from the back

print(my_list[0:5])		# 1st element from the front till the 4th element from the front
print(my_list[3:8])		# 3rd element from the front till the 7th element from the front
print(my_list[0:-5])	# 1st element from the front till the 6th element from the back
print(my_list[-7:-2])	# 7th element from the back till the 3rd element from the back

print(my_list[1:9])				# Does not work
print(my_list[1:10])			# Bad
print(my_list[1:len(my_list)])	# Okay
print(my_list[1:])				# Good

print(my_list[0:-1])	# Okay
print(my_list[:-1])		# Good

print(my_list[:])		# The entire range

print(my_list[2:9:1])	# the default value of step, pick every 1st element
print(my_list[2:9:2])	# pick every 2nd element

print(my_list[8:1:-1])	# pick every 1st element in reverse
print(my_list[8:1:-2])	# pick every 2nd element in reverse

print(my_list[::-1])	# get the entire list and pick every 1st element in reverse

print(5 in my_list)			# checks if 5 is in my_list
print(10 not in my_list)	# checks if 10 is not in my_list

print([0, 1, 2] + [3, 4, 5])	# concatenates the 2 lists
print([0, 1, 2] * 3)			# repeats list [0, 1, 2] 3 times and concatenates

print(min(my_list))		# returns the minimum or smallest element in the list
print(max(my_list))		# returns the maximum or largest element in the list
print(sum(my_list))		# returns the sum of elements in the list

l = [[0, 1, 2], ['zainab', 'rahul', 'james']]	# l comprises of 2 nested lists
print(l[0][2])		# l[0] = [0, 1, 2]
print(l[1][:2])		# l[1] = ['zainab', 'rahul', 'james']
print(l[0][::-1])

dogs = ['pug', 'beagle', 'poodle', 'shiba inu', 'chow chow']

dogs[1] = 'bulldog'	# modify element at position 1
print(dogs)

dogs[:3] = ['retriever', 'husky', 'terrier'] # modify all elements in range(0, 3)
print(dogs)

dogs.append('boxer') # add 'boxer' at end of the list
print(dogs)

dogs.insert(2, 'papillon')	# insert 'papillion' at position 2
dogs.insert(-1, 'maltese')	# negative indices also work
print(dogs)

del dogs[2]		# delete element at position 2
del dogs[-2]	# negative indices also work
print(dogs)

del dogs[:3]	# delete all elements in the range(0, 3)
print(dogs)

student = ['Neha', 19, 2019]		# list packing
name, age, year = student			# list unpacking
print(name, age, year)				# prints as space separated values by default
# name, age, year, id_no = student	# error: trying to unpack 4 values from a list of 3 values

print(list("python"))			# breaks the string into a list of characters
print(list(range(5)))			# returns a list of elements from 0 to 4
print(list(range(1, 10, 2)))	# returns a list of odd elements from 1 to 9

animals = ['lion', 'cat', 'panda', 'dog']
for animal in animals:	# loops through a sequence of elements
	print(animal)



# Tuples

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[5])
print(my_tuple[-3])
print(my_tuple[:5])
print(my_tuple[1:])
print(my_tuple[2:9:2])
print(my_tuple[::-1])

# my_tuple[0] = 10		# error: tuples are immutable

levels = ('preschool', 'elementary', 'intermediate', 'senior high', 'university')
for level in levels:	# loops through a sequence of elements
	print(level)

print(tuple(enumerate(levels)))			# adds a counter for each value as a tuple of (counter, value)
print(tuple(enumerate(levels, 100)))	# starts the counter from 100

levels = ('preschool', 'elementary', 'intermediate', 'senior high', 'university')
for index, level in enumerate(levels):	# loop through a sequence of elements with tuple unpacking
	print(index, level)



# Dictionaries

student = {'name': 'Rahul', 'age': 21, 'courses': ['CS', 'Chem', 'TRW', 'Bio']}	# dict

print(student['name'])		# accessing the key 'name'
print(student['age'])		# accessing the key 'age'
print(student['courses'])	# accessing the key 'courses'

# student['idno']			# error: key does not exist
print(student.get('idno'))	# returns None if key does not exist

student['idno'] = '2019A7PS0903U'	# updates the value if key exists else creates a new key with value
print(student)

del student['idno']	# delete key-value pair with key 'idno'
print(student)

variety = {13: 'prime', 'constants': [3.14, 2.718, 1.618], (1 + 4.2j): True}	# dict of varying data types

letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

print(letters.items())	# returns the key-value pairs of dict
print(letters.keys())	# returns the keys of dict
print(letters.values())	# returns the values of dict

letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
for key, value in letters.items():	# loop through a sequence of elements with tuple unpacking
	print(key, value)

letters.update({5: 'f', 6: 'g', 7: 'h'})	# updates the value if key present else creates a new one
print(letters)

letters.clear()	# delete all key-value pairs in dict
print(letters)



# Sets

fruits = {"apple", "orange", "banana", "orange", "pear", "apple"}	# Using {} or curly braces
fruits = set(["apple", "orange", "banana", "orange", "pear", "apple"])	# Using the set function
print(fruits)	# duplicate elements automatically removed

variety = {"python", 5, ("breakfast", "lunch", "dinner"), 2.718} # set of varying data types
# s = {[1, 2, 3]}	# error: lists aren't mutable

fruits.add('grape')   # adds an element to the set
print(fruits)
fruits.remove('orange') # removes an element from the set
print(fruits)

# fruits.remove('carrot')   # error: element not in set
fruits.discard('carrot')  # removes an element if it exists else does nothing

for fruit in fruits:  # loops through a sequence of elements
	print(fruit)

fruits.clear()
print(fruits)

odds = {1, 3, 5, 7, 9}		# set of odd numbers
evens = {0, 2, 4, 6, 8}	# set of even numbers
ints = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # set of integers
primes = {2, 3, 5, 7}   # set of primes

print(5 in odds)    # check if element is present in set
print(2 not in odds)  # check if element is not present in set

print(odds.union(evens))   # returns the set of elements in either a or b
print(odds & ints)

print(odds.intersection(evens))  # returns the set of elements common to both a and b
print(evens & primes)

print(ints.difference(odds)) # returns the set of elements in a but not in b
print(ints - evens)

print(primes.symmetric_difference(odds)) # returns the set of elements in either a or b but not both
print(primes ^ evens)



# Functions

def greet():
	"""This function greets by printing 'Hello, Everyone!'"""
	print("Hello, Everyone!")

greet()

def greet(name):
	"""Greets the person whose name is passed as a parameter"""
	print("Hello, " + name + "!")

greet("Zack")
# greet()		# error: no name passed

def greet(name='Everyone'):
	"""Greets the person whose name is passed as a parameter, default='Everyone'"""
	print("Hello, " + name + "!")

greet()			# no argument passed, uses default value
greet("Alice")	# argument passed, uses argument value

def greet(msg, name="Everyone"):
	"""Greets the person whose name is passed as a parameter, default='Everyone' with a message"""
	print("Hello, " + name + "! " + msg)

greet("Hope you are doing well :)", "Abdul")	# name passed, uses argument value
greet("Hope you like our session!")				# no name passed, uses default value

# def greet(name="Everyone", msg):	# error: default argument before required argument
# 	print("Hello, " + name + "! " + msg)

def exponent(a, b):
	"""Returns a to the power b"""
	return a ** b

print(exponent(5, 3))	# returns 5 to the power 3

print(exponent(2, 3))		# called using positional arguments
print(exponent(3, 2))		# switching the position matters
print(exponent(a=2, b=3))	# called using keyword arguments
print(exponent(b=3, a=2))	# switching the position does not matter

# Goal: a = 5 and b = 3
print(exponent(5, b=3))		# a = 5 and b = 3
# print(exponent(b=3, 5))	# error: keyword arguments must follow positional arguments
# print(exponent(5, c=3))	# error: what is c?
# print(exponent(5, a=3))	# error: a = 5 or a = 3?

def add(*numbers):
	"""Returns the sum of all numbers"""
	return sum(numbers)

print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))

def add(*numbers):
	"""Returns the sum of all numbers"""
	return sum(numbers)
	print("This never gets executed")

print(add(9, 4))