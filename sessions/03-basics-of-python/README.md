# Basics Of Python

<p align="center"><img src="python-logo.png"></p>

# Lists

<p align="center"><img src="horcruxes.jpg"></p>


A `list` is a collection of arbitrary objects, similar to arrays in other programming languages. A `list` is defined by enclosing a comma-separated sequence of objects in square brackets `[]`

```python
>>> squares = [1, 4, 9, 16, 25]	# list of numbers
>>> names 	= ['harry', 'ron', 'hermione', 'ginny'] # list of strings
>>> variety = [3, 'slytherin', 2.718, True, [9, 8, 7]] # list of varying data types
```

The `len` function returns the length of a `list`

```python
>>> horcruxes = ["diary", "ring", "cup", "locket", "diadem", "snake", "boy"]
>>> len(horcruxes)	# returns the number of elements in the list
7
```

To understand accessing elements of a `list`, it is very important to understand the concept of slicing.

![](./slicing.png)

```python
>>> my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
... #        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
```

In python, you can use both +ve and -ve indices to access elements

```python
>>> my_list[0]		# 1st element from the front
0
>>> my_list[5]		# 6th element from the front
5
>>> my_list[9]		# 10th element from the front
9
>>> my_list[-1]		# 1st element from the back
9
>>> my_list[-5]		# 5th element from the back
5
>>> my_list[-10]	# 10th element from the back
0
```

To get a `range` of elements, we use the following syntax:

```python
list[start:end:step]
```

*	start - Starting position of `range`, defaults to **0**
*	end - Ending position of `range`, **non-inclusive**, defaults to **length** of `list`
*	step - Step size, defaults to **1**

```python
>>> my_list[0:5]	# 1st element from the front till the 5th element from the front
[0, 1, 2, 3, 4]
>>> my_list[3:8]	# 4th element from the front till the 8th element from the front
[3, 4, 5, 6, 7]
>>> my_list[0:-5]	# 1st element from the front till the 6th element from the back
[0, 1, 2, 3, 4]
>>> my_list[-7:-2]	# 7th element from the back till the 3rd element from the back
[3, 4, 5, 6, 7]
```

Since end is non-inclusive, how do you slice the entire `list`?

```python
>>> my_list[1:9]		# Does not work
[1, 2, 3, 4, 5, 6, 7, 8]
>>> my_list[1:10]		# Bad
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> my_list[1:len(my_list)]	# Okay
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> my_list[1:]			# Good
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This also works for the beginning

```python
>>> my_list[0:-1]		# Okay
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> my_list[:-1]		# Good
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```

You can also drop both start and end to slice the entire `list`

```python
>>> my_list[:]	# The entire range
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The step parameter skips values

```python
>>> my_list[2:9:2]	# pick every 2nd element
[2, 4, 6, 8]
```

The value of step can also be -ve which will run in reverse

```python
>>> my_list[8:1:-1]	# pick every 1st element in reverse
[8, 7, 6, 5, 4, 3, 2]
>>> my_list[8:1:-2]	# pick every 2nd element in reverse
[8, 6, 4, 2]
```

Using step you can reverse the entire `list`

```python
>>> my_list[::-1]	# get the entire list and pick every 1st element in reverse
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

<p align="center"><img src="harry-potter-sorting-hat.jpg"></p>

Now that you have an understanding of `list`, let's now see some built-in operators

The `in` and `not in` operators

```python
>>> gryffindor = ["harry", "ron", "hermione"]
>>> "harry" in gryffindor # checks if "harry" is in gryffindor
True
>>> "draco" not in gryffindor # checks if "draco" is not in gryffindor
True
```

You can concatenate two `list` objects by using the `+` operator

```python
>>> slytherin = ["draco", "tom", "snape", "vincent", "gregory"]
>>> ravenclaw = ["luna", "cho", "padma"]
>>> hufflepuff = ["cedric", "tonks"]
>>> hogwarts = gryffindor + slytherin + ravenclaw + hufflepuff
>>> hogwarts
['harry', 'ron', 'hermione', 'draco', 'tom', 'snape', 'vincent', 'gregory', 'luna', 'cho', 'padma', 'cedric', 'tonks']
```

You can repeat a `list` by using the `*` operator

```python
>>> [0, 1, 2] * 3	# repeats list [0, 1, 2] 3 times and concatenates
[0, 1, 2, 0, 1, 2, 0, 1, 2]
```

You can also use mathematical functions

```python
>>> my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> min(my_list)	# returns the minimum or smallest element in the list
0
>>> max(my_list)	# returns the maximum or largest element in the list
9
>>> sum(my_list)	# returns the sum of elements in the list
45
```

Keep in mind that a `list` can also be nested

<p align="center"><img src="harry-potter-quidditch-balls.jpg"></p>

```python
>>> l = [[0, 1, 2], ['quaffle', 'bludger', 'bludger', 'snitch']] # l comprises of 2 nested lists
>>> l[0][2]	# l[0] = [0, 1, 2]
2
>>> l[1][:2]	# l[1] = ['quaffle', 'bludger', 'bludger', 'snitch']
['quaffle', 'bludger']
>>> l[0][::-1]
[2, 1, 0]
```

One fundamental concept of `list` is that it is mutable. This means you can change values in a `list`, elements can be added, deleted, shifted and moved around at will.

> A **mutable** object can be modified after it is created. In contrast, an **immutable** object is one whose state cannot be modified after it is created.

We will use the following example

<p align="center"><img src="harry-potter-spell-cast.jpg"></p>

```python
>>> spells = ["riddikulus", "obliviate", "sectumsempra", "avada kedavara", "alohomora", "lumos", "expelliarmus","wingardium leviosa", "accio", "expecto patronum"]
```

To modify a single value

```python
>>> spells[0] = 'stupefy'	# modify element at position 1
>>> spells
['stupefy', 'obliviate', 'sectumsempra', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum']
```

Or modify a `range` of values

```python
>>> spells[:3] = ['crucio', 'imperio', 'incendio'] # modify all elements in range(0, 3)
>>> spells
['crucio', 'imperio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum']
```

You can `append` elements at end of a `list`

```python
>>> spells.append('reducto')
>>> spells
['crucio', 'imperio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reducto']
```

Or `insert` at a specific index

```python
>>> spells.insert(2, "silencio")
>>> spells
['crucio', 'imperio', 'silencio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reducto']
>>> spells.insert(-1, "reparo") # negative indices also work
>>> spells
['crucio', 'imperio', 'silencio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reparo', 'reducto']
```

To delete a single value

```python
>>> del spells[2]
>>> spells
['crucio', 'imperio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reparo', 'reducto']
>>> del spells[-2]
>>> spells
['crucio', 'imperio', 'incendio', 'avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reducto']
```

Or delete a `range` of values

```python
>>> del spells[:3]
>>> spells
['avada kedavara', 'alohomora', 'lumos', 'expelliarmus', 'wingardium leviosa', 'accio', 'expecto patronum', 'reducto']
```

One neat property of a `list` is unpacking

```python
>>> student = ['Neville', 29, 1980]	# list packing
>>> name, age, year = student		# list unpacking
>>> print(name, age, year)		# prints as space separated values by default
Neville 29 1980
```

However, if we try to unpack more/less values than expected, python throws an error
```python
>>> student = ['Neville', 29, 1980]
>>> name, age, year, id_no = student	# trying to unpack 4 values from a list of 3 values
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
```

You can convert an `str` object or a string to a `list` using type casting

```python
>>> list("python")	# breaks the string into a list of characters
['p', 'y', 't', 'h', 'o', 'n']
```

> Type casting or type coercion refers to converting one data type into another.

We can use type casting to better understand the `range` function

```python
>>> list(range(5))		# returns a list of elements from 0 to 4
[0, 1, 2, 3, 4]
>>> list(range(1, 10, 2))	# returns a list of odd elements from 1 to 9
[1, 3, 5, 7, 9]
```

To iterate over a `list`

```python
>>> animals = ['hippogriff', 'phoenix', 'unicorn', 'centaur']
>>> for animal in animals:	# loops through a sequence of elements
...     print(animal)
...
hippogriff
phoenix
unicorn
centaur
```

To empty a `list`

```python
>>> animals = ['hippogriff', 'phoenix', 'unicorn', 'centaur']
>>> animals.clear()		# delete all elements in list
>>> animals
[]
```

<p align="center"><img src="hippogriff.png"></p>

---

# Tuples

A `tuple` is identical to a `list` in all respects, except for the following properties:

*	A `tuple` is defined using parenthesis `()` instead of square brackets `[]` as in a `list`
*	A `tuple` is immutable

Why use a `tuple` over `list`?

*	Faster execution
*	Data remains constant

```python
>>> my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> my_tuple[5]
5
>>> my_tuple[-3]
7
>>> my_tuple[:5]
(0, 1, 2, 3, 4)
>>> my_tuple[1:]
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> my_tuple[2:9:2]
(2, 4, 6, 8)
>>> my_tuple[::-1]
(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

Since they are immutable, you _cannot_ change their values

```python
>>> my_tuple[0] = 10		# error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

To iterate over a `tuple`

```python
>>> levels = ('prefect', 'head', 'caretaker', 'professor', 'headmaster')
>>> for level in levels:	# loops through a sequence of elements
...     print(level)
...
prefect
head
caretaker
professor
headmaster
```

<p align="center"><img src="prefect.jpg"></p>

We can now try to see `enumerate` function

```python
>>> tuple(enumerate(levels))	# adds a counter for each value as a tuple of (counter, value)
((0, 'prefect'), (1, 'head'), (2, 'caretaker'), (3, 'professor'), (4, 'headmaster'))
```

The default starting value for the counter is **0** in `enumerate`. However, you can specify a different starting value

```python
>>> tuple(enumerate(levels, 100))	# starts the counter from 100
((100, 'prefect'), (101, 'head'), (102, 'caretaker'), (103, 'professor'), (104, 'headmaster'))
```

Using `tuple` unpacking we can loop through with `enumerate`

```python
>>> levels = ('prefect', 'head', 'caretaker', 'professor', 'headmaster')
>>> for index, level in enumerate(levels):	# loop through a sequence of elements with tuple unpacking
...     print(index, level)
...
0 prefect
1 head
2 caretaker
3 professor
4 headmaster
```

---

# Dictionaries

A dictionary is a collection of key-value pairs. The key is a _unique_ identifier that is mapped to a value, almost like a real-world dictionary where each word is a key and the definition is the value. You can define a dictionary using curly braces `{}`, a colon `:` separates each key from its value

<p align="center"><img src="courses.jpg"></p>

```python
>>> student = {'name': 'Harry', 'age': 14, 'courses': ['Charms', 'Defence Against the Dark Arts', 'Potions', 'Herbology']}	# dict
```

We access values of a `dict` similar to a `list` but instead of specifying the position (which doesn't make much sense in a dictionary), we specify the key

```python
>>> student['name']		# accessing the key 'name'
'Harry'
>>> student['age']		# accessing the key 'age'
14
>>> student['courses']	# accessing the key 'courses'
['Charms', 'Defence Against the Dark Arts', 'Potions', 'Herbology']
```

If the key, does not exist it will throw an error, a better way is to use the `get` method

```python
>>> student['idno']		# error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'idno'
>>> print(student.get('idno'))	# returns None if key does not exist
None
```

Adding an entry is as easy as assigning a new key and a value

```python
>>> student['idno'] = 'the-boy-who-lived'	# updates the value if key exists else creates a new key with value
>>> student
{'name': 'Harry', 'age': 25, 'courses': ['Charms', 'Defence Against the Dark Arts', 'Potions', 'Herbology'], 'idno': 'the-boy-who-lived'}
```

To delete an entry

```python
>>> del student['idno']	# delete key-value pair with key 'idno'
>>> student
{'name': 'Harry', 'age': 25, 'courses': ['Charms', 'Defence Against the Dark Arts', 'Potions', 'Herbology']}
```

We can have a variety of keys and values just like in a `list` or `tuple` as long as the _keys_ are of immutable data type

```python
>>> variety = {13: 'prime', 'constants': [3.14, 2.718, 1.618], (1 + 4.2j): True}	# dict of varying data types
```

Let's now look at some built-in methods. We'll use the following example

```python
>>> letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
```

Some common methods

```python
>>> letters.items()	# returns the key-value pairs of dict
dict_items([(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')])
>>> letters.keys()	# returns the keys of dict
dict_keys([0, 1, 2, 3, 4])
>>> letters.values()	# returns the values of dict
dict_values(['a', 'b', 'c', 'd', 'e'])
```

Using the `items` method and `tuple` unpacking, we can loop through a `dict`

```python
>>> letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
>>> for key, value in letters.items():	# loop through a sequence of elements with tuple unpacking
...     print(key, value)
...
0 a
1 b
2 c
3 d
4 e
```

To merge a dictionary using another dictionary

```python
>>> letters.update({5: 'f', 6: 'g', 7: 'h'})	# updates the value if key present else creates a new one
>>> letters
{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
```

To empty a `dict`

```python
>>> letters.clear()	# delete all key-value pairs in dict
>>> letters
{}
```

---

# Sets

A `set` is an unordered collection with no duplicate elements. A `set` itself may be modified, but the elements of a set must be _immutable_.

<p align="center"><img src="weasleys.png"></p>

There are two ways to create a `set`

```python
>>> weasleys = {"ron", "fred", "george", "fred", "ginny", "ron"}		# Using {}
>>> weasleys	# duplicate elements automatically removed
{'george', 'ron', 'fred', 'ginny'}
>>> weasleys = set(["ron", "fred", "george", "fred", "ginny", "ron"])	# Using the set function
>>> weasleys	# duplicate elements automatically removed
{'george', 'ron', 'fred', 'ginny'}
```

Elements in a `set` can be of varying data types as long as they are immutable

```python
>>> variety = {"python", 5, ("breakfast", "lunch", "dinner"), 2.718} # set of varying data types
>>> variety
{('breakfast', 'lunch', 'dinner'), 2.718, 5, 'python'}
>>> s = {[1, 2, 3]}	# error: lists aren't mutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

You can modify a `set`

```python
>>> weasleys = {'george', 'ron', 'ginny', 'fred'}
>>> weasleys.add('percy')		# adds an element to the set
>>> weasleys
{'fred', 'george', 'percy', 'ron', 'ginny'}
>>> weasleys.remove('fred') 	# removes an element from the set. accidental spoilers!
>>> weasleys
{'george', 'percy', 'ron', 'ginny'}
```

Be careful when you `remove` elements, a better way is to use `discard`

```python
>>> weasleys.remove('harry')		# removes an element if it exists else raises an error
Traceback (most recent call last):  	# error: element not in set
  File "<stdin>", line 1, in <module>
KeyError: 'harry'
>>> weasleys.discard('harry')		# removes an element if it exists else does nothing
```

To iterate over a `set`

```python
>>> weasleys = {'fred', 'george', 'percy', 'ron', 'ginny'}
>>> for fruit in weasleys:  # loops through a sequence of elements
...     print(fruit)
...
fred
george
percy
ron
ginny
```

To empty a `set`

```python
>>> weasleys.clear()  # delete all elements in set
>>> weasleys
set()
```

You can use operators on `set`. We'll use the following example

```python
>>> odds = {1, 3, 5, 7, 9}	# set of odd numbers
>>> evens = {0, 2, 4, 6, 8}	# set of even numbers
>>> ints = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # set of integers
>>> primes = {2, 3, 5, 7}  	# set of primes
```

The `in` and `not in` operators can be used to test if elements are in a `set`

```python
>>> 5 in odds		# check if element is present in set
True
>>> 2 not in odds	# check if element is not present in set
True
```

Let's now take a look at mathematical operations on a `set`. Find the `union` of two or more sets

```python
>>> odds.union(evens)	# returns the set of elements in either a or b
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> odds & ints
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

Find the `intersection` of two or more sets

```python
>>> odds.intersection(evens)  # returns the set of elements common to both a and b
set()
>>> evens & primes
{2}
```

Get the `difference` of two or more sets

```python
>>> ints.difference(odds) # returns the set of elements in a but not in b
{0, 2, 4, 6, 8}
>>> ints - evens
{1, 3, 5, 7, 9}
```

Get the `symmetric_difference` of two or more sets

```python
>>> primes.symmetric_difference(odds) # returns the set of elements in either a or b but not both
{1, 2, 9}
>>> primes ^ evens
{0, 3, 4, 5, 6, 7, 8}
```

> Just like a `list` has an immutable data type called `tuple`, a `set` also has an immutable data type called `frozenset`.

---

# Functions

Functions allow you to write a piece of code to carry out a specified task. Functions help break your code into smaller chunks. As your program grows larger, functions make it more organized and manageable. Futhermore, they allow you to avoid repetition and make code reusable.

There are 3 types of functions:

* Built-in functions
* User-defined functions
* Anonymous functions

You have already seen a few built-in functions. The `len`, `min`, `max` and `sum` are a few examples. We'll mainly be focusing on user-defined functions.

Functions have the following syntax

```python
def function_name(parameter(s)):
	"""docstring"""
	statement(s)
	[return object]
```

Below are the steps in defining a function:

1.  Use the keyword `def` to **def**ine the function followed by the name of the function.
2.  Add _parameter(s)_ to the function, this is optional.
3.  A colon `:` marks the end of function header.
4.  Optional **doc**umentation **string** to decribe what the function does.
5.  Statement(s) making up the function body, must be indented.
6.  An optional `return` statement to `return` a value from the function.

Let's now create some functions!

```python
def greet():
...     """This function greets by printing 'Hello, Everyone!'"""
...     print("Hello, Everyone!")
```

<p align="center"><img src="hello.gif"></p>

To call a function, simply type the function name with appropriate parameters

```python
>>> greet()
Hello, World!
```

Let's add a name parameter to our function

```python
>>> def greet(name):
...     """Greets the person whose name is passed as a parameter"""
...     print("Hello, " + name + "!")
```

Now we call it by passing a name as an argument, if we don't we get an error

```python
>>> greet("Voldemort")
Hello, Voldemort!
>>> greet()	# error: no name passed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: greet() missing 1 required positional argument: 'name'
```

To solve this we can use default arguments

```python
>>> def greet(name='Everyone'):
...     """Greets the person whose name is passed as a parameter, default='Everyone'"""
...     print("Hello, " + name + "!")
...
>>> greet()		# no argument passed, uses default value
Hello, Everyone!
>>> greet("Dumbledore")	# argument passed, uses argument value
Hello, Dumbledore!
```

You can have multiple arguments

```python
>>> def greet(msg, name="Everyone"):
...     """Greets the person whose name is passed as a parameter, default='Everyone' with a message"""
...     print("Hello, " + name + "! " + msg)
```

Keep the ordering of arguments when calling the function

```python
>>> greet("The boy who lived come to die? :P", "Harry")	# name passed, uses argument value
Hello, Harry! The boy who lived come to die? :P
>>> greet("Hope you like our session!")			# no name passed, uses default value
Hello, Everyone! Hope you like our session!
```

When having multiple arguments, default arguments must be followed after required arguments

```python
>>> def greet(name="Everyone", msg):	# error: default argument before required argument
...     print("Hello, " + name + "! " + msg)
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

You can `return` values from a function. Let's define a basic exponent function

```python
>>> def exponent(a, b):
...     """Returns a to the power b"""
...     return a ** b
...
>>> exponent(5, 3)	# returns 5 to the power 3
125
```

When we call a function with values, the values get assigned to the arguments according to their position. However, python allows functions to be called using keyword arguments

```python
>>> exponent(2, 3)	# called using positional arguments
8
>>> exponent(3, 2)	# switching the position matters
9
>>> exponent(a=2, b=3)	# called using keyword arguments
8
>>> exponent(b=3, a=2)	# switching the position does not matter
8
```

When using both positional and keyword arguments, make sure keyword arguments follow positional arguments, else python throws you an error

```python
>>> # Goal: a = 5 and b = 3
... exponent(5, b=3)	# a = 5 and b = 3
125
>>> exponent(b=3, 5)	# error: keyword arguments must follow positional arguments
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

Also, make sure you are using the right keyword names

```python
>>> exponent(5, c=3)	# error: what is c?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exponent() got an unexpected keyword argument 'c'
```

You might still get an error when mixing positional and keyword arguments

```python
>>> # Goal: a = 3 and b = 5
... exponent(5, a=3)	# error: a = 5 or a = 3?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exponent() got multiple values for argument 'a'
```

The last type of arguments you can have are arbitrary arguments. We use them when we do not know in advance the number of arguments that will be passed into a function. We use an asterisk `*` before the parameter name to denote this argument

```python
>>> def add(*numbers):
...     """Returns the sum of all numbers"""
...     return sum(numbers)
...
>>> add(10, 20, 30)
60
>>> add(1, 2, 3, 4, 5)
15
```

Bear in mind, functions immediately exit when they come across a `return` statement

```python
>>> def add(*numbers):
...     """Returns the sum of all numbers"""
...     return sum(numbers)
...     print("This never gets executed")
...
>>> add(9, 4)
13
```

<!-- An example of everything: required arguments, default arguments and arbitrary arguments -->

---

# Summary

We covered:

*	[Lists](#lists)
*	[Tuples](#tuples)
*	[Dictionaries](#dictionaries)
*	[Sets](#sets)
*	[Functions](#functions)