# Bir fonksiyonu birçok diğer fonksiyon ile beraber kullanmak istiyorsak 
# decarations mantığı ile ilişkilendirebiliyoruz

# amaç daha az ve daha temiz kod yazmak

# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan önceki işlemler")
#         func()
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello():
#     print("hello")

# Bu aşşağıda yapılan işlem ile
# @my_decorator işlemi aynıdır
# sayHello = my_decorator(sayHello)
# sayHello()


import math
import time #zaman işlemlerinin yapıldığı modül
# zaman işlemleri ortak olduğu için bunları ayrı bir fonksiyonda aldık ve diğer fonksiyonlarda çağırdık(decarators)
def calculate_time(func):
    def inner(*args,**kwargs):        
        start = time.time()  # o anki zamanı kaydeder
        time.sleep(1) # Bir saniye durduruyor
        func(*args,**kwargs)        
        finish = time.time()
        print("fonksiyon "+func.__name__ +" " + str(finish-start) + " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))   

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)