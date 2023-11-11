# Hatırlarsanız str veya list işlerken methoslar kullanmıştık
# Bunlar aslında birer fonksiyon yapıda 
# pythonda gömülü olarak gelen kütüphanelerde

# Fonksiyon nedir?
# Fonksiyon bir veri alıp yada almadan işleyip sana çıktı veren bir kod bloğudur

# Bu fonksiyon geri bir değer döndürmüyor
# Çağrıyı alıyor ve çalışıyor
def seyHello():
    print("hello")

seyHello()

# iki tane girdi alıyor
# Bunları toplayıp geri gönderir
def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)


# *params (params değişkenin ismi)
# istediğimiz kadar değer girmemizi sağlıyor
# istersek sonuna yada başına başka değişken koyup kalanları *paramsa bırakabiliriz
def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(add(10, 20, 50))

# **kwargs
# key -> value tanımlamada ismi olmayan ama isimlendirilmiş değerleri alır
def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')


# SCOPE

# global scope
x = 'global x'

def function(): 
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)

# ##########################

name = 'global string'

def greeting():
    # name = 'Çınar'

    def hello():
        # name = 'Ada'
        print('hello '+ name)

    hello()

greeting()
