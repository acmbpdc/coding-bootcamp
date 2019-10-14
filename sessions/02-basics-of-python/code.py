#!/bin/python

# Usage:
# python code.py



# Basics

print("Hello, World!")	# your first line of code

## Comments

# This is ignored by the python interpreter

"""
This is a multiline comment
using triple double quotes
"""

'''
This is a multiline comment
using triple single quotes
'''



# Data Types

## Variables

a = 10
b = 20

a, b = 10, 20

print(a)
print(b)

## Numbers

a = -10				# int
b = 3.14159			# float
c = -2.2 + 5.3j		# complex

print(12121212121212121212121212121212121212121212121212121212121212121212121 + 1)

## Boolean

a = True	# bool
b = False	# bool

## Strings

str1 = "I like cats."	# str enclosed in double quotes
str2 = 'I like dogs.'	# str enclosed in single quotes

str1 = 'I\'ll have what he is having.'
str2 = "\"To be or not to be\" - William Shakespeare"

str1 = "I'll have what he is having."				# string with single quotes enclosed in double quotes
str2 = '"To be or not be" - William Shakespeare'	# string with double quotes enclosed in single quotes

print('C:\some\name')
print(r'C:\some\name')



# Operators

## Arithmetic Operators

a = 5
b = 3
print(+a)	# unary addition
print(-b)	# unary subtraction

print(2 + 2)	# addition
print(8 - 5)	# subtraction
print(3 * 5)	# multiplication
print(8 / 2)	# division

print(11 / 4)		# floating point division
print(11 // 4)		# floor division

print(10 // 3)		# int // int => int
print(10.0 // 3)	# float // int => float
print(10 // 3.0)	# int // float => float
print(10.0 // 3.0)	# float // float => float

print(5**2)		# exponentiation, 5 squared
print(10 % 3)	# modulus, returns remainder of division

## Comparison Operators

print(5 == 5)	# (a == b) returns True if a is equal to b else False
print(5 != 5)	# (a != b) returns True if a is not equal to b else False
print(2 < 3)	# (a < b) returns True if a is strictly less than b else False
print(2 > 3)	# (a > b) returns True if a is strictly greater than b else False
print(7 >= 7)	# (a >= b) returns True if a is greater than or equal to b else False
print(7 <= 4)	# (a <= b) returns True if a is less than or equal to b else False

## Assignment Operators

num = 8		# a = b			num = 8
num += 3	# a = a + b 	num = 11
num -= 5	# a = a - b		num = 6
num *= 6	# a = a * b		num = 36
num /= 5	# a = a / b		num = 7.2
num //= 3	# a = a // b	num = 2.0
num **= 3	# a = a ** b	num = 8.0
num %= 5	# a = a % b		num = 3.0
print(num)

## Logical Operators

a = True
b = False
print(a and b)	# returns True if both the operands are True
print(a or b)	# returns True if either of the operand is True
print(not a)	# returns True if operand is False



# Control Flow

## if Statement

raining = True
if raining:		# the condition is True
	print("Stay at home")

raining = False
if raining:		# the condition is False
	print("Stay at home")
else:
	print("Let's go outside")

age = 21
if age < 4:		# False
	print("Join nursery")
elif age < 18:	# False
	print("Stay in school")
elif age < 24:	# True!
	print("Work hard in university")
elif age < 60:	# skips
	print("Get working")
else:			# skips
	print("Time to retire")

print("Stay at home" if raining else "Let's go outside")	# conditional expression

## while Loop

i = 0
while i < 5:	# loop over numbers from 0 through 4
	print(i)
	i += 1

i = 0
while i < 5:
	if i == 3:	# breaks the loop when i = 3
		break
	print(i)
	i += 1

i = 0
while i < 5:
	if i == 3:	# skips the rest of the code block when i = 3
		i += 1	# causes an infinite loop otherwise!
		continue
	print(i)
	i += 1

## for Loop

for c in "python":	# loop over a sequence of elements
	print(c)

for i in range(5):	# loop over numbers from 0 through 4
	print(i)

for i in range(1, 10, 2):	# loop over numbers from 0 through 9 picking every 2nd value
	print(i)



# Iterables

## Lists

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

## Tuples

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

## Dictionaries

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