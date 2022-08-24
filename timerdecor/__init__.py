from codecs import xmlcharrefreplace_errors
from re import L, M
import time
from multiprocessing import Pool
from tkinter import N
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"[Ran in {(end - start)}] s") 
    return wrapper

def tryexcept(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught '{e}'")
    return wrapper

def perftimer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[Ran in {(end - start)} s]")
    return wrapper



class MyClass:
    x = None
    y = None
    z = None
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return str((self.x, self.y, self.z))
    
    def __add__(self, other):
        L = self.x + other.x
        M = self.y + other.y
        N = self.z + other.z
        f = MyClass(L, M, N)
        return f

    def __


y = MyClass(10, 10, "Hi")
z = MyClass(10, 10, "Hi")
print(y + z)