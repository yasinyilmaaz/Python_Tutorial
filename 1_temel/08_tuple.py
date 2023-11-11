# tuple
# list benzer yapısı vardır ama list değildir
# normal parantezler arasına yazılır
# tek bir değer varsa souna virgül konunması gereki
# iki tuple veriyi toplayabiliriz

fruit = ("elma",2,"armut","armut")

print(type(fruit))

print(fruit[2])

print(len(fruit))

# değer ekleme işlemi list dek gibi değildir

# verdiğimiz değeri kaç tane olduğunu aratma
print(fruit.count("armut"))

print(fruit.index("armut"))