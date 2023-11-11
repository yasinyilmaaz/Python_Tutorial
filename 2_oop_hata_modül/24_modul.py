# Modüller
# Modüller, Python programlarını organize etmek, kodu yeniden kullanmak ve projeleri daha yönetilebilir hale getirmek için kullanılır.
# Pythonda gömülü gelen modüllerde vardır
# mesela: math, random, re

# Bazı hazır modülleri hazır olarakta indirebiliriz
# pip sitesinden gerekli olan modülü indirebiliriz
# pip install modül_adı

# içinde matematiksel olarak tüm işlemer vardır
# üstüne gelip sağtık yapıp "go to definition" basarsak
# içinde hangi fonksiyonların bulunduğuna bakabiliriz
import math 
# modüle kendimizde bir isim verebiliriz
import math as islem

print(islem.factorial(5))
print(islem.sqrt(9))

# Kendimiz bir modül yazabiliriz
import mod

result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]
result = mod.func(10)

p = mod.Person()
p.speak()

print(result)