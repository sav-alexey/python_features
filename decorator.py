import functools
def decorator(func):
     @functools.wraps(func)
     def wrapper(*args):
          result = func(*args)
          print("wrapped")
          return result
     return wrapper

@decorator
def func(a, b):
    c = a + b
    print(c)
    return c


func(5, 6)
print(func.__name__)