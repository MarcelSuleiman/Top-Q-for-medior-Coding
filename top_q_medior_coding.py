# #Code involving questions
'''
Q: What will be the output of the following code?

>>> list = ['a', 'b', 'c', 'd', 'e']
>>> print(list[10:])
'''

Output: []

'''
Q: How can I reload a previously imported module? (we assume that the module is a file module.py)
'''

from importlib import reload
reload(module)


'''
Q: What will be the output of the following code?

>>> a = [[]]*3
>>> a[1].append(1)
>>> print(a)
'''

Output: [[1], [1], [1]]

'''
Q: What's wrong with the following code?

def foo():
    from .module import *
    print(f"{bar()}")
'''

import or from module import * should be on top - alias "SyntaxError: import * only allowed at module level"

'''
Q: The file is located in /usr/lib/python/person.py. The program is run with python /usr/lib/python/person.py. What will the output be?

class Person:
    def __init__(self, name):
        __name__ = name

    def getAge(self):
        print(__name__)

p = Person("John")
p.getAge()
'''

Output: __main__

'''
Q: Write a timeit decorator to measure the time of function execution.
'''

from time import time
from time import sleep
from random import randint

run_time = {}

def timeit_decorator(func):
    def wrapper():
        
        start_time = time()
        func()
        end_time = time()

        lap_time = end_time - start_time
        
        run_time[func.__name__] = lap_time
        
    return wrapper

@timeit_decorator
def test_func():
    for i in range(3):
        sleep_time = randint(1,3)
        print('Hi, I am row no: {} and I will sleep for {} sec...'.format(i, sleep_time))
        sleep(sleep_time)
        
@timeit_decorator
def play_movie():
    print('prehravam video')
    
@timeit_decorator
def show_picture():
    for i in range(200):
        print(f'ukazujem ti fotku c.: {i}')
        
test_func()
play_movie()
show_picture()

print(run_time)

'''
Q: Write a decorator that will catch errors and repeat the function a maximum of 3 times (configurable).
'''

e_data = {}

def error_decorator(func, n):
    def wrapper(*args):
        for i in range(n):
            try:
                value = func(*args)
                
            except Exception as E:
                temp_data = []
                temp_data.append(E.__class__.__name__)
                temp_data.append(str(E))
            
                e_data[func.__name__] = temp_data
               
        if 'value' in locals():
            return value
            
    return wrapper

def add(a, b):
    return a+b
    
n = 3
add = error_decorator(add, n)

print(add(10,20))
print(add('Marcel','Suleimnan'))
print(add('Marcel',300))

print(e_data)

'''
Q: What's the output of the following code?

class parent:
    def __init__(self, param):
        self.v1 = param

class child:
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print(obj.v1 + " " + obj.v2)
'''

Output: obj does not have attribute v1

Output: error mixing str and int


'''
Q: Fix the following code to make it work.

class Repeater:
    ...
class RepeaterIterator:
    ...

repeater = Repeater("Hello")
for i in repeater:
    print(i)  # hello

'''

class Repeater:
    def __init__(self, value):
        self.value = value
        
    def __iter__(self):
        return RepeaterIterator(self)
        
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
        
    def __next__(self):
        return self.source.value
        
repeater = Repeater("Hello")
for i in repeater:
    print(i)



'''
Q: Write code to get unique values from a list of complex types (custom classes). Example: [A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab)] -> [A(1, "ab"), A(2, "ab"), A(2, "aa")].
'''
class A:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        
    def __eq__(self, other): 
        if not isinstance(other, A):
            return NotImplemented

        return self.num == other.num and self.name == other.name

dataset = [A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab")]
#dataset = [A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab"), A(2, "ab"), A(1, "ab"),A(2, "ab"), A(1, "ab")]
#dataset = [A(1, "ab"), A(2, "ab"), A(2, "ab"), A(2, "ab"), A(2, "ab"), A(2, "ab"), A(2, "ab"), A(2, "ab")]
clean_dataset = []


def get_clean_dataset():
    return clean_dataset

def return_unique(dataset):
    
    for element in dataset:
        clean_dataset = get_clean_dataset()
        
        if clean_dataset == []:
            clean_dataset.append(element)
        else:
            clean_dataset = get_clean_dataset()
            count = 0
            for unique in clean_dataset:
                if unique != element:
                    count += 1
                else:
                    pass
                
            if count == len(clean_dataset):
                clean_dataset.append(element)

return_unique(dataset)
print('-'*30)
print(dataset)
print(clean_dataset)

'''
Q: We have the following code with the unknown function f(). In f(), we do not want to use a return, instead, we may want to use a generator.

for x in f(5):
    print(x,)
The output looks like this:

0 1 8 27 64
Write a function f() so that we can have the output above.
'''
def f(num):
    for i in range(num):
        yield i ** 3


for x in f(5):
    print(x, end=' ')


'''
Q: What's the output of the following code?

x = [[0], [1]]
print(len(' '.join(list(map(str, x)))))
'''

Output: 7
