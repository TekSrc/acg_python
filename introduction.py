# Print "Hello, world!" to the console - first Python program
print('Hello, world!'); # Trailing comment
# If I need multiple lines for comments,
# the best way to do so is to just use multiple lines
# with hash lines

# python3 -m doctest -v <filename>.py

#---------------------------------------------------------

# TODO: STRINGS
# https://docs.python.org/3/whatsnew/3.11.html#string
# https://docs.python.org/3/library/stdtypes.html#str.endswith
# strings are immutable, so you can't change them
# you can only create new ones

'single quoted'
"double quoted"
'''
  multi-line
  string
'''
'single'.find('g') # 3 index position
'single'.find('d') # -1 not in string
'single'.replace('g', 'd') # 'dindle'
"TeSTING".lower() # 'testing'
print("Tab\tDelimited") # Tab    Delimited
print("New\nLine") # New
                  # Line
print("Back\\Slash") # Back\Slash
print(r"Raw\String") # Raw\String
print("Concat" + "enation") # Concatenation
print("Repeat" * 3) # RepeatRepeatRepeat
print(len("Length")) # 6
print('"Double" quotes') # "Double" quotes
print('\'Double\' quotes') # 'Double' quotes

#---------------------------------------------------------

# TODO: NUMBERS: int, float, complex numbers (rarely used) - conversion strings to numbers
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
2 + 2 # 4
10 - 4 # 6
3 * 9 # 27
5 / 3 # 1.6666666666666667
5 // 3 # 1 integer division
5 % 3 # 2 modulus
5 % 2 # 1 (odd)
4 % 2 # 0 (even)
# fizz buzz python function
def fizz_buzz(n):
  if n % 3 == 0 and n % 5 == 0:
    return 'FizzBuzz'
  if n % 3 == 0:
    return 'Fizz'
  if n % 5 == 0:
    return 'Buzz'
  return n
print(fizz_buzz(3)) # Fizz
print(fizz_buzz(5)) # Buzz
print(fizz_buzz(15)) # FizzBuzz

2 ** 3 # 8
pow(2, 3) # 8
1.1 + 3 # 4.1
4.0 + 3 # 7.0

str(7.0) # '7.0' convert number to string
float('7.0') # 7.0 convert string to number
int('7') # 7 convert string to number
# int('7.0') # ValueError: invalid literal for int() with base 10: '7.0'
int(7.0) # 7 convert float to int
int(5.6666) # 5 convert float to int (truncates)
-5.5 + 4 # -1.5

#---------------------------------------------------------

# TODO: BOOLEANS: True, False, None
None # None
True # True
False # False
bool(0) # False
bool(1) # True
bool(0.0) # False
bool(0.1) # True
bool('') # False
bool(' ') # True
bool('False') # True
bool('False' == False) # False
bool('False' == 'False') # True
bool('False' == 'True') # False
bool('False' != 'True') # True
bool('False' != False) # True
bool('False' != 'False') # False
bool(1.0) # True
bool(0.0) # False

#---------------------------------------------------------

# TODO: VARIABLES: snake_case, start with letter or underscore, case sensitive
my_name = "Frank"
print(my_name) # Frank
my_name + 'Carvajal' # FrankOther
my_name += ' Carvajal' # Frank Carvajal shorthand for takes itself and adds itself back into itself different spot in memory
my_age = 32 # If I reassign to another type it's not locked
# Not going to run into pointer issues thankfully.

#---------------------------------------------------------

# TODO: LISTS: ordered, mutable, allows duplicates
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types

my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(my_list[3]) # 4 - using subscript operation by index
len(my_list) # 5
my_list[len(my_list) - 1] # 5 - last element)]
my_list[0:2]  # [1, 2] - slicing
my_list[2:4] # [3, 4] slicing from middle of the list
my_list[:4] # [1, 2, 3, 4] - slicing from beginning
my_list[::2] # [1, 3, 5] - slicing with step
my_list[::-1] # [5, 4, 3, 2, 1] - slicing with negative step reverse the list
my_list[0] = "a" # ['a', 2, 3, 4, 5] - mutable
print(my_list) # ['a', 2, 3, 4, 5] , lists can be modified in memory, not redeclaring and defining back, modifying going on. occassionally you have to use immutable values and you'll know you shouldn't use a list for that. Discernment is key.
my_list[0:2] = 'a' # ['a', 3, 4, 5] - slicing and replacing
my_list[0:2] = [1, 2, 3] # [1, 2, 3, 4, 5] - slicing and replacing
my_list[0:2] = [] # [3, 4, 5] - slicing and replacing with empty list aka removal
# power of lists is calling various methods on them
# .pop, .append, .insert, .remove, .clear, .copy, .count, .extend, .index, .reverse, .sort
# my_list.remove(6) # ValueError: list.remove(x): x not in list
my_list.remove(4) # [3, 5] - remove by value prefer calling a method doing the exact same thing
my_list.pop() # 5 - remove last element
my_list.pop() # 3 - remove last element
# can use list as a datastructure of stack, last item to go in is first to come out, slowly take things off
# if wanting to use a que
my_list = [1, 2, 3, 4]
my_list.pop(0) # 1 - remove first element
my_list # [2, 3, 4, 5]
my_list.append(5) # [2, 3, 4, 5] - add to end of list
my_list.insert(0, 1) # [1, 2, 3, 4, 5] - insert at index  
my_list.clear() # [] - clear list

#---------------------------------------------------------

# TODO: TUPLES & RANGES
# https://docs.python.org/3/library/stdtypes.html#tuple
# https://docs.python.org/3/library/stdtypes.html#ranges

# TUPLES: ordered, immutable, allows duplicates more simple thab ranges, powerful but less useful
# RANGES: calculate a list thats all sequential and less memory

point = (2.0, 3.0) # tuple - immutable, can't be modified which is handied in case where list since mutable is undesired.
point_3d = point + (4.0,) # (2.0, 3.0, 4.0) - tuple concatenation
# Group together multiple things and package as one items, return multiple items from a function and that works because can unpack them into variables.
x, y, z = point_3d # unpacking
x # 2.0
y # 3.0
z # 4.0
# Working with python 2 and 3 code that need to work together
print("My name is: %s %s" % ("Frank", "Carvajal")) # My name is: Frank Carvajal
# Length is determined by how many substitutions as a use for tuples, can't change lenth or items in them, but can easily unpack and pack them into multiple variables in specific order and represented

range(10) # range(0, 10) - 0 to 9 start stop step
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(0, 10000)
list (range(10000)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ... 9999]
# handy when need to do something a certain number of times which is when to use ranges, step
list(range(1, 12, 2)) # [1, 3, 5, 7, 9, 11] - start, stop, step

#---------------------------------------------------------

# TODO: DICTIONARIES: key-value pairs, unordered, mutable, no duplicates
# https://docs.python.org/3/library/stdtypes.html#dict
# known as hashes, maps, objects, associative arrays, key-value pairs, unordered, mutable, no duplicates

ages = { 'frank': 32, 'kristen': 31, "hope": 10 } # dictionary
ages['frank'] # 32 - using subscript operation by key
# keys can be immutable data types
# Dictionaries kinda work like databases a bit as the keys need to be immutable even if the values are mutable
# ages['keith'] # KeyError: 'keith' - key not found
ages['keith'] = 29 # add key-value pair
ages # {'frank': 32, 'kristen': 31, 'hope': 10, 'keith': 29}

del ages['keith'] # remove key-value pair
ages # {'frank': 32, 'kristen': 31, 'hope': 10}
ages.pop('kristen') # 31 - remove key-value pair
# {}.pop('frank') # KeyError: 'frank' - remove key-value pair
ages.get('frank') # 32 - get value by key
ages.keys() # dict_keys(['frank', 'hope']) - get keys
ages.values() # dict_values([32, 10]) - get values
list(ages.values()) # [32, 10] - convert to list

weights = dict(frank=330, kristen=120, eli=50) # {'frank': 330, 'kristen': 120, 'eli': 50} - dictionary
colors = dict([('frank', ' blue'), ('kristen', 'green'), ('eli', 'red')]) # {'frank': 'blue', 'kristen': 'green', 'eli': 'red'} - dictionary
# We will use dictonaries to hold on to information you know the shape of or need to be able to put a bunch of things on something andlook up by key later on, dictionaries will be useful to use.

#---------------------------------------------------------

# TODO: CONTROL FLOW: if, elif, else, for, while, break, continue, pass
# https://docs.python.org/3/tutorial/controlflow.html
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# 6 comparison types: <, >, <=, >=, ==, !=
# COMPARISONS & CONDITIONALS:
# https://docs.python.org/3/library/stdtypes.html#comparisons

1 < 2 # True
1 > 2 # False
1 <= 2 # True
1 >= 2 # False
1 == 2 # False
1 == 1 # True
1 == 1.0 # True
'a' == 'A' # False
'a' == 'a' # True
3.1 == 'this' # False
'a' > 'b' # False
'b' > 'a' # True
'a' != 'b' # True
3.1 != 'this' # True
'abc' < 'b' # True
'bac' < 'b' # False
2 in [1, 2, 3] # True
4 in [1, 2, 3] # False
2 not in [1, 2, 3] # False
4 not in [1, 2, 3] # True
# if elif else
if 1 < 2:
  print('True') # True
elif 1 > 2:
  print('False') # False
else:
  print('Neither') # Neither
name = 'Frank'
if len(name)>= 6:
  print('The name is long') # Long
elif len(name) == 5:
  print('The name is medium') # Medium
elif len(name)>= 3:
  print('The name is short') # Short
else:
  print('The name is very short') # very short

# and, or, not
# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
  
not "" # True
not " " # False
not 1 > 2 # True
if not 1 > 2:
  print("no it isn't") # no it isn't
'a' or 'b'  # 'a'
'' or 'Frank' # 'Frank'
'' or [] # [] since last item since no truthy value
first = ""
last = "Carvajal"
if first or last:
  print("The user has a part of a name") # The user has a part of a name
first_name = first or "Franklin"
print(first_name) # Franklin
if first and last:
  print("The user has a full name") # nothing
"Frank" and "" # ''
"Frank" and "A" and '' # ''
(1 > 2) and print("hello") # False
(1 < 2) and print("hello") # hello
(first and last) and print("The user has a full name") # nothing
(first or last) and print("The user has a part of a name") # The user has a part of a name

#---------------------------------------------------------

# TODO: WHILE LOOPS
# https://docs.python.org/3/reference/compound_stmts.html#while
# while True:
#   print("Looping"); # infinite Loop. ACCIDENT, not good. Infinite loop as event loop checking for new events in like a game, take an action based on that, handle it, then go back to listening in the event loop, but in this, we don't as it has no break case.
count = 1
while count <= 4:
  print(count)
  count += 1

count = 0
while count < 10:
  if count % 2 == 0: # check if even
    count += 1
    continue
  print(f"We're counting odd numbers: {count}") # kind of like template literals in JavaScript in python3.6 to have access to that feature
  # print("We're counting odd numbers: %s" % count) # old way
  count += 1

count = 1
while count < 10:
  if count % 2 == 0: # check if even
    break
  print(f"We're counting odd numbers: {count}") # kind of like template literals in JavaScript in python3.6 to have access to that feature
  # print("We're counting odd numbers: %s" % count) # old way
  count += 1

#---------------------------------------------------------
  
  # TODO: FOR LOOP or FOR STATEMENT
# https://docs.python.org/3/reference/compound_stmts.html#for
  
  colors = ['red', 'green', 'blue']
  for color in colors:
    print(color)

  for color in colors:
    if color == 'red':
      continue
    elif color == 'blue':
      break
    print(color)

    point = (2.1, 3.0, 7) # tuple
    for value in point:
      print(value)

    ages = { 'frank': 32, 'kristen': 31, "hope": 10 } # dictionary
    for key in ages:
      # print(key)
      # print(ages[key])
      print(f"{key} is {ages[key]} years old")

for letter in "my_string": # iterate over string
  print(letter)

list_of_points = [(1, 2), (2, 3), (3, 4)]
for x, y in list_of_points: # unpacking tuple in the for statement itself
  print(f"x: {x}, y: {y}")

x, y, z = (1, 2, 3) # unpacking tuple
for x, y, z in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
  print(f"x: {x}, y: {y}, z: {z}")

for name, age in ages.items(): # dictionary
  print(f"Person named: {name}")
  print(f"Age of: {age}")

ages.items() # dict_items([('frank', 32), ('kristen', 31), ('hope', 10)])

#---------------------------------------------------------

# TODO: FUNCTIONS
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/library/stdtypes.html#function-objects

# CREATE ENCAPSULATED LOGIC TO REUSE WITH FUNCTIONS
def greet_person(name):
  print(f"Hello, {name}!")
greet_person("Frank") # Hello, Frank!
output = greet_person("Kristen") # Hello, Kristen!
output # None, but default functions have no return value
def add_two(number):
  return number + 2 # return value
result = add_two(5) # 7
print(result) # 7

def add(num1, num2):
  return num1 + num2
print(add(5, 5)) # 10

def contact_card(name, age, car_model):
  return f"{name} is {age} and drives a {car_model}"
print(contact_card("Frank", 32, "Toyota Tundra")) # Frank is 32 and drives a Toyota Tundra
print(contact_card(age=31, name="Kristen", car_model="Toyota Sienna")) # Kristen is 31 and drives a Toyota Sienna
print(contact_card("Hope", car_model="Toyota Highlander", age=10)) # Hope is 10 and drives a Toyota Highlander
# print(contact_card(car_model="Toyota Highlander", "Hope", age=10)) # SyntaxError: positional argument follows keyword argument

def can_drive(age, driving_age=16): # default parameter for function
  return age >= driving_age
print(can_drive(16)) # True
print(can_drive(10)) # False
print(can_drive(16, 18)) # False

import math

#---------------------------------------------------------

# TODO: CLASSES
# https://docs.python.org/3/tutorial/classes.html
# https://docs.python.org/3/library/stdtypes.html#class-objects
# define types and modeling concepts from our world to use in our program
# classes are blueprints for objects
# objects are instances of classes
# share functionality that isn't tightly coupled and fragile
# methods are functions attached to classes

class Car:
  """
  Docstring describing the class
  Car models a car w/tires and an engine
  """

  def __init__(self, engine, tires): # this is the thing that happens when create a new instance of the class that we are defining. constructor, dundar method, double underscore
    """
    Docstring describing the method
    """
    self.engine = engine
    self.tires = tires

  def description(self):
    """
    Docstring describing the method
    """
    return f"A car with an {self.engine} engine, and {self.tires} tires"
  
  def wheel_circumference(self):
    if len(self.tires) > 0:
      return self.tires[0].circumference()
    else:
      return 0
  

  

my_car = Car('8-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']) # instance of the class
print(my_car) # <__main__.Car object at 0x7f8e3e3e3d60>
print(my_car.engine) # 8-cylinder
print(my_car.tires) # ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']
# attributes are variables attached to objects
my_car.lincense_plate = "ABC123" # add attribute to object
print(my_car.lincense_plate) # ABC123
print(my_car.description()) # A car with an 8-cylinder engine, and ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'] tires

#---------------------------------------------------------

# TODO: COMPOSITION
# https://docs.python.org/3/tutorial/classes.html#inheritance
# building up classes by passing in other instances of classes

class Tire:
  """
  Tire represents a tire w/ a automobile
  """

  def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
    self.tire_type = tire_type
    self.width = width
    self.ratio = ratio
    self.diameter = diameter
    self.brand = brand
    self.construction = construction

  def circumference(self):
    """
    The circumference of the tire in inches
    >>> tire = Tire('P', 205, 55, 15, 'Michelin')
    >>> tire.circumference()
    75.0
    """
    total_diameter = self._side_wall_inches() * 2 + self.diameter
    return round(total_diameter * math.pi, 1)
  
  def __repr__(self):
    """
    Represents the tires information in the standard notation present on the side of the tire Exx: P215/65R15 Michelin
    """
    return (f"{self.tire_type}{self.width}/{self.ratio}"
            + f"{self.construction}{self.diameter} {self.brand}")
  
  def _side_wall_inches(self): # private method as a helper method
    return (self.width * (self.ratio / 100)) / 25.4

  
my_tire = Tire('P', 205, 55, 15, 'Michelin')
print(my_tire) # <__main__.Tire object at 0x7f8e3e3e3d60>
print(my_tire.tire_type) # P
print(my_tire.width) # 205
print(my_tire.ratio) # 55
print(my_tire.diameter) # 15
print(my_tire.brand) # Michelin
tires = [my_tire, my_tire, my_tire, my_tire]
toyota = Car('8-cylinder', tires)
print(toyota.description()) # A car with an 8-cylinder engine, and [<__main__.Tire object at 0x7f8e3e3e3d60>, <__main__.Tire object at 0x7f8e3e3e3d60>, <__main__.Tire object at 0x7f8e3e3e3d60>, <__main__.Tire object at 0x7f8e3e3e3d60>] tires
print(toyota.wheel_circumference()) # 78.5
# python3.8 -m doctest -v sandbox.py

#---------------------------------------------------------

# TODO: INHERITANCE
# https://docs.python.org/3/tutorial/classes.html#inheritance
# building up classes by passing in other instances of classes
# composition over inheritance is a statement, two diff things both serve their own purposes, know when to use it
# idea is that you can create a class that is based off of another class, slight tweaks, subdivision of that object, base class is the super class, derived class is the sub class
# general class but need some more specific create a subclass of that type and already have access to the class functions without having to redefine repr. 

class SnowTire(Tire): # multiple inheritance is almost always a bad idea, since you can pass many - dangerous
  def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
    super().__init__(tire_type, width, ratio, diameter, brand, construction)
    # Tire.__init__(self, tire_type, width, ratio, diameter, brand, construction) # might see in python2 code
    self.chain_thickness = chain_thickness

  def circumference(self):
    """
    The circumference of a tire w/ snow chains in inches

    >>> tire = SnowTire('P', 205, 55, 15, 2, 'Michelin')
    >>> tire.circumference()
    87.6
    """
    total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
    return round(total_diameter * math.pi, 1)
  
  def __repr__(self):
    return super().__repr__() + " (Snow)"

snow_tire = SnowTire('P', 205, 55, 15, 2, 'Michelin')
print(snow_tire) # P205/55R15 Michelin (Snow)

#---------------------------------------------------------

# TODO: POLYMORPHISM
# https://docs.python.org/3/tutorial/classes.html#inheritance
# weird sounding, it is the idea that is regarded to if it walks like a duck sounds like a duck it's probably a duck. As long as you implement the right methods on something you have a polymorphic relationship.

tire = SnowTire('P', 205, 65, 15, 2, 'Michelin')
tires = [tire, tire, tire, tire]
honda = Car(tires=tires, engine='4-cylinder')
honda.wheel_circumference() # 83.8
honda.description() # A car with an 4-cylinder engine, and [P205/65R15 Michelin (Snow), P205/65R15 Michelin (Snow), P205/65R15 Michelin (Snow), P205/65R15 Michelin (Snow)] tires

# Polymorphism is very powerful to not hardcode our dependencies but classes allow us to make changes on the fly. Something that goes off and runs and codes based on a dependency it gets,
# for ex a notification system, a Notifier class that could be < Email, SMS, Push notification, just need to know the interface of the class, the methods that are available to it, and the class can be swapped out for another class that has the same methods and the code will still work. Polymorphic relationship with one another.

#---------------------------------------------------------

# TODO: Using Packages
# https://docs.python.org/3/tutorial/modules.html#packages
# python module index: https://docs.python.org/3/py-modindex.html
# pip install <package-name>
# pip uninstall <package-name>
# pip list
# import <package-name>
# from <package-name> import <module-name>
# from <package-name> import <module-name> as <alias>
# from <package-name>.<module-name> import <function-name>
# from <package-name>.<module-name> import <function-name> as <alias>
# from <package-name> import *

# from math import * # can end up with some really weird situations of getting everything from the math module, not recommended
# import math
# from math import pi, ceil # BEST as it's most EXPLICIT!
from math import pi as p, ceil as c # aliases can be nice in addition to the explicitness

print(p) # 3.141592653589793
print(c(3.1)) # 4

# pip for installing packages
# pip uninstall package-name
# pip3 list or pip3 freeze > requirements.txt to create file that has all those requirements in them
# then do pip3 install -r requirements.txt will try to install everything in there
# mkdir ~/venvs
# python3 -m venv ~/venvs/myenv
# source ~/venvs/myenv/bin/activate
# source ~/venvs/myenv/bin/deactivate or just `deactivate` in terminal
# pipenv project https://pipenv.readthedocs.io/en/latest/
# pipenv --python python3.9
# cat Pipfile , after install will be Pipfile.lock
# pipenv shell
# pipenv install psycopg2 for example

#---------------------------------------------------------

# Interacting with Files
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/functions.html#open
# TODO: GOING TO USE OPEN, WRITE, & READ WITH FILES A LOT
# open(<filename>, <mode>)
# with open('xmen.txt', 'r') as my_file: then block and it will automatically close file after it's done
# my_file = open('xmen.txt', 'w+')
# my_file.write('Beast\n')
# my_file.write('Wolverine\n')
# my_file.writelines(['Cyclops\n', 'Pheonix\n', 'Nightcrawler\n'])
# my_file.close() # this also calls flush and dont want to hold onto file so this will terminate and release the file
# my_file = open('xmen.txt', 'r')
# print(my_file.read())
# print("I'm reading again")
# print(my_file.read())
# my_file.seek(0) # go to the beginning of the file
# my_file.close()

# python3 using_files.py
# cat xmen.txt

#---------------------------------------------------------

# TODO: ENVIRONMENT VARIABLES
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.html#os.environ
# os.environ['key'] # value
# os.environ['key'] = 'value'

# import os
# stage = os.environ['STAGE'].upper()
# output = f"We're running in {stage}"
# if stage.startswith('PROD'):
#   output = "DANGER! - " + output
# print(output)

# STAGE=staging python3 env_vars.py

#---------------------------------------------------------

# TODO: ERROR HANDLING
# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/exceptions.html#Exception
# https://docs.python.org/3/library/exceptions.html#BaseException
# https://docs.python.org/3/library/exceptions.html#SystemExit
# https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt
# https://docs.python.org/3/library/exceptions.html#GeneratorExit
# https://docs.python.org/3/library/exceptions.html#SystemError
# https://docs.python.org/3/library/exceptions.html#ArithmeticError
# https://docs.python.org/3/library/exceptions.html#FloatingPointError
# https://docs.python.org/3/library/exceptions.html#OverflowError
# https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
# https://docs.python.org/3/library/exceptions.html#AssertionError
# https://docs.python.org/3/library/exceptions.html#AttributeError
# https://docs.python.org/3/library/exceptions.html#EOFError
# https://docs.python.org/3/library/exceptions.html#ImportError
# https://docs.python.org/3/library/exceptions.html#LookupError
# https://docs.python.org/3/library/exceptions.html#IndexError
# https://docs.python.org/3/library/exceptions.html#KeyError
# https://docs.python.org/3/library/exceptions.html#MemoryError
# https://docs.python.org/3/library/exceptions.html#NameError
# https://docs.python.org/3/library/exceptions.html#

# MAKE SURE TO PUT THEM IN ORDER BECAUSE IT WILL RUN THEM IN ORDER

# import sys

# file_name = 'recipes.txt'

# try:
#         my_file = open('recipes.txt', 'x')
#         my_file.write(b'Meatballs\n')
#         my_file.close()
# except FileExistsError as err:
#         print(f"The {file_name} already exists.")
# except:
#         print(f"Unable to write to the file")
# else:
#         print(f"Wrote to {file_name}")
# finally:
#         print("Execution completed")

# python3 error_handling.py # The recipes.txt already exists.

#---------------------------------------------------------

# TODO: DECORATORS
# https://docs.python.org/3/glossary.html#term-decorator
# property decorator
# https://docs.python.org/3/library/functions.html#property
# class decorator
# https://docs.python.org/3/library/functions.html#classmethod
# static method decorator
# https://docs.python.org/3/library/functions.html#staticmethod

# function decorator
# method decorator
# class method decorator

# https://docs.python.org/3/library/functools.html
# https://docs.python.org/3/library/functools.html#functools.wraps
# https://docs.python.org/3/library/functools.html#functools.total_ordering
# https://docs.python.org/3/library/functools.html#functools.lru_cache
# https://docs.python.org/3/library/functools.html#functools.cached_property
# https://docs.python.org/3/library/functools.html#functools.lru_cache
# https://docs.python.org/3/library/functools.html#functools.cached_property

# extend functions we write with more functionality by decorating them - Learn a bit about functional programming with decorators
# really wonderful code reuse, use functions to compose other functions without adding anything to the original function

# def inspect(func, *args): # creating a variatic function, any number of args still valid
def inspect(func):
  def wrapped_func(*args, **kwargs):
    print(f"Running {func.__name__}")
    val = func(*args)
    print(f"Result: {val}")
    return val
  return wrapped_func

# inspect(combine)
@inspect
def combine(a, b):
  return a + b

class User:
  base_url = 'https://example.com/api'

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  @classmethod
  def query(cls, query_string):
    return cls.base_url + '?' + query_string
  
  @staticmethod
  def name():
    return 'Frank Carvajal'
  
  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

# ➜ python3 -i decorators.py
# >>> User.name
# <function User.name at 0x103bbb0d0>
# >>> User.name()
# 'Frank Carvajal'
# >>> User.query('name=test')
# 'https://example.com/api?name=test'
# >>> user = User('Frank', 'Carvajal')
# >>> user.base_url
# 'https://example.com/api'
# >>> user.full_name
# 'Frank Carvajal'
# >>> user.first_name = 'Franklin'
# >>> user.full_name
# 'Franklin Carvajal'
# >>>

#---------------------------------------------------------
  
# TODO: BREAKPOINT DEBUGGING
# https://docs.python.org/3/library/pdb.html
# https://docs.python.org/3/library/pdb.html#debugger-commands

import pdb  
def map(func, values):
  output_values = []
  index = 0
  while index < len(values):
    pdb.set_trace()
    output_values = func(values[index])
    index += 1
  return output_values

def add_one(val):
  return val + 1

print(map(add_one, list(range(10))))

# ➜ python3 debugger.py
# > /Users/Home/debugger.py(7)map()
# -> output_values = func(values[index])
# (Pdb) values
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (Pdb) index
# 0
# (Pdb) output_values
# []
# (Pdb) h

# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where

# Miscellaneous help topics:
# ==========================
# exec  pdb
# (Pdb) help cont
# c(ont(inue))
#         Continue execution, only stop when a breakpoint is encountered.
# (Pdb) help next
# n(ext)
#         Continue execution until the next line in the current function
#         is reached or it returns.
# (Pdb)
# (Pdb) n
# > /Users/Home/debugger.py(8)map()
# -> index += 1
# (Pdb) output_values
# 1
# (Pdb) list
#   3  		output_values = []
#   4  		index = 0
#   5  		while index < len(values):
#   6  			pdb.set_trace()
#   7  			output_values = func(values[index])
#   8  ->			index += 1
#   9  		return output_values
#  10
#  11  	def add_one(val):
#  12  		return val + 1
#  13
# (Pdb) q

# quits, then go fix code : output_values.append(func(values[index])) is the change to make

# also a breakpoint function
# https://docs.python.org/3/library/pdb.html#module-pdb

# python3 -m pdb <filename>.py

# ➜ python3 -m pdb debugger.py
# > /Users/Home/debugger.py(1)<module>()
# -> def map(func, values):
# (Pdb) ll
#   1  ->	def map(func, values):
#   2  		output_values = []
#   3  		index = 0
#   4  		while index < len(values):
#   5  			output_values.append(func(values[index]))
#   6  			index += 1
#   7  		return output_values
#   8
#   9  	def add_one(val):
#  10  		return val + 1
#  11
#  12  	print(map(add_one, list(range(10))))
# (Pdb) break 5, index == 5
# Breakpoint 1 at /Users/Home/debugger.py:5
# (Pdb) ll
#   1  ->	def map(func, values):
#   2  		output_values = []
#   3  		index = 0
#   4  		while index < len(values):
#   5 B			output_values.append(func(values[index]))
#   6  			index += 1
#   7  		return output_values
#   8
#   9  	def add_one(val):
#  10  		return val + 1
#  11
#  12  	print(map(add_one, list(range(10))))
# (Pdb) c
# > /Users/Home/debugger.py(5)map()
# -> output_values.append(func(values[index]))
# (Pdb) l
#   1  	def map(func, values):
#   2  		output_values = []
#   3  		index = 0
#   4  		while index < len(values):
#   5 B->			output_values.append(func(values[index]))
#   6  			index += 1
#   7  		return output_values
#   8
#   9  	def add_one(val):
#  10  		return val + 1
#  11
# (Pdb) values
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (Pdb) output_values
# [1, 2, 3, 4, 5]
# (Pdb) q
