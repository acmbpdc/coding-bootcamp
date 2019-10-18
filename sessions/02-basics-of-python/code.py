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

print(type(a))
print(type(b))
print(type(c))

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