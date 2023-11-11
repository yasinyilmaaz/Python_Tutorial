# set
# Birden fazla veri depolamak için bir diğer alternatiftir
# İndexsleme sıralama yoktur
# ekleme ve çıkarma vardır

fruits = { "orange", "banana", "apple"}

for x in fruits:
    print(x)

# veri ekleme
fruits.add('cherry')
fruits.update(["Kiraz","Şeftali"])

# veri silme
fruits.remove('cherry')

fruits.discard("banana")

# en sondaki elemanı siler
fruits.pop()

# set temizleme
fruits.clear()


print(fruits)