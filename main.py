print("Hi,Hello! these are my Python Essential 2 - codes!")

# 1 Importing a module
from math import sin, pi
print(sin(pi / 2))
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))


# 2 Selected functions
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


# 3 Exponential Functions
from math import e, exp, log
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))



# 4 general-purpose functions
from math import ceil, floor, trunc
x = 1.4
y = 2.6
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))


# 5 random module
from random import random
for i in range(5):
    print(random())


# 6 The randrange and randint functions
from random import randrange, randint
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
# The platform function
from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))
# The machine function
from platform import machine
print(machine())
# The processor function
from platform import processor
print(processor())
# The system function
from platform import system
print(system())
# The version function
from platform import version
print(version())


# 7 python_version_tuple functions
from platform import python_implementation, python_version_tuple
print(python_implementation())
for atr in python_version_tuple():
    print(atr)


# 8 Modules
counter = 0
if _name_ == "_main_":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")
# Example of a python module
""" module.py - an example of a Python module """
__counter = 0
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum
def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod
if _name_ == "_main_":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)


# 9 module named sys.
import sys
for p in sys.path:
    print(p)


# 10 Strings
# Example 1
word = 'by'
print(len(word))
# Example 2
empty = ''
print(len(empty))
# Example 3
i_am = 'I\'m'
print(len(i_am))
# Multiline strings
multiline = '''Line #1
Line #2'''
print(len(multiline))


# 11 Operations on strings
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


# 12 Operations on strings: ord()
char_1 = 'a'
char_2 = ' '
print(ord(char_1))
print(ord(char_2))


# 13 Slices
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


# 14 The in and not in operators
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


# 15 Operations on strings
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)
# Demonstrating min()
print(min("aAbByYzZ"))
# Demonstrating min()
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))
# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))


# 16 index() method
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


# 17 list() function
print(list("abcabc"))
# count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
# capitalize() method:
print('aBcD'.capitalize())
# center() method
print('[' + 'alpha'.center(10) + ']')
# endswith() method
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
# find() method
print("Eta".find("ta"))
print("Eta".find("mma"))
# isalnum() method
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# The join() method
# join() method:
print(",".join(["omicron", "pi", "rho"]))
# lower() method
print("SiGmA=60".lower())
# lstrip() method
print("[" + " tau ".lstrip() + "]")
# replace() method
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
# rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
# rstrip() method
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
# split() method
print("phi       chi\npsi".split())
# startswith() method
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
# strip() method:
print("[" + "   aleph   ".strip() + "]")
# swapcase() method
print("I know that I know nothing.".swapcase())
print()
# title() method:
print("I know that I know nothing. Part 1.".title())
print()
# upper() method:
print("I know that I know nothing. Part 2.".upper())


# 18 Sorting:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()
#sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)


# 19  Caesar cipher-Encrypting a message
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)



# 20 Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)



# 21 Numbers Processor
line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")


# 22 IBAN Validator.
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ', '')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


# 23 Exceptions
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")
print("THE END.")


# Exceptions: continued
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")
print("3")
# Exceptions: continued
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")
print("THE END.")
# The anatomy of exceptions
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")
print("THE END.")


# 24 stack
stack = []
def push(val):
    stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())


# 25 stack-the object approach
class Stack:
    def _init_(self):
        print("Hlo!")
stack_object = Stack()
# The object approach: a stack from scratch
class Stack:
    def _init_(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
# The object approach
class Stack:
    def _init_(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
class AddingStack(Stack):
    def _init_(self):
        Stack._init_(self)
        self.__sum = 0


# 26 instance variables
class ExampleClass:
    def _init_(self, val=1):
        self.__first = val
    def set_second(self, val=2):
        self.__second = val
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.__third = 5
print(example_object_1._dict_)
print(example_object_2._dict_)
print(example_object_3._dict_)


# 27 Class variables:
class ExampleClass:
    __counter = 0
    def _init_(self, val=1):
        self.__first = val
        ExampleClass.__counter += 1
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
print(example_object_1._dict, example_object_1._ExampleClass_counter)
print(example_object_2._dict, example_object_2._ExampleClass_counter)
print(example_object_3._dict, example_object_3._ExampleClass_counter)


# 28 Methods
class Classy:
    def method(self):
        print("method")
obj = Classy()
obj.method()
# Methods in detail
class Classy:
    def _init_(self, value):
        self.var = value
obj_1 = Classy("object")
print(obj_1.var)
# 30 classes and objects:
class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass
def printBases(cls):
    print('( ', end='')
    for x in cls._bases_:
        print(x._name_, end=' ')
    print(')')
printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)


# 28 Investigating classes
class MyClass:
    pass
obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5
def incIntsI(obj):
    for name in obj._dict_.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
print(obj._dict_)
incIntsI(obj)
print(obj._dict_)
# Inheritance: issubclass()
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
# Inheritance: isinstance()
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()
for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
# Inheritance: the is operator
class SampleClass:
    def _init_(self, val):
        self.val = val
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)
string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"
print(string_1 == string_2, string_1 is string_2)


# 29 Hierarchy of classes:
import time
class TrackedVehicle:
    def control_track(left, stop):
        pass
    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)
class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass
    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)


# 30 Generator
class Fib:
    def _init_(self, nn):
        print("_init_")
        self.__n = nn
        self.__i = 0
        self._p1 = self._p2 = 1

    def _iter_(self):
        print("_iter_")
        return self

    def _next_(self):
        print("_next_")
        self.__i += 1
        if self._i > self._n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self._p1 + self._p2
        self._p1, self.p2 = self._p2, ret
        return ret

print("Thank, you!")