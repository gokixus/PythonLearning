def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello(name):
    print("Hello", name)
sayHello("Ahmet")

def sayGreeting():
    print("greeting")
    
# sayGreeting  = my_decorator(sayGreeting)
# sayGreeting()


import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " +str(finish-start)+ " saniye sürdü.")
    return inner

@calculate_time
def usAlma(a, b):
    # start = time.time()
    # time.sleep(1)
    print(math.pow(a, b))
    # finish = time.time()
    # print("Fonksiyon " + str(finish-start) + " saniye sürdü.")
    
@calculate_time
def faktoriyel(number):
    # start = time.time()
    # time.sleep(1)
    print(math.factorial(number))
    # finish = time.time()
    # print("Fonksiyon " + str(finish-start) + " saniye sürdü.")

@calculate_time
def toplama(a, b):
    print(a+b)

usAlma(2, 3)
faktoriyel(6)
toplama(6,10)