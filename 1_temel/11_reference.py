#  iki değerleri farklı integer değişkenimiz olsun
# bunları birbirine atadığımızda içindeki değer atanır
# değişkenin adresinde bir değişiklik olmaz

x = 5
y = 25

x = y

y = 10

print(x,y)

# iki listeyi arasında değer ataması yaptığımızda bunların
# bellekdeki adresleride aynı olur
# atamayı yaptıktan sonra değişiklik yaparsak her ikisinde de
# değişiklik oluşacak
#  

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a, b)