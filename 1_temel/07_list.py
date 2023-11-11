# listeler 
# içine istediğimiz kadar veriyi depoladığımız veri türü
# içinde ekleyeceğimiz verilerin türü aynı olmak zorunda değildir
# kare parantezler arasında virgül ile ayırarak oluştururuz

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

new_list= [1, 3,"dddd","yasin",10]

#  list metodlar


# en küçük değer 
val = min(numbers)
# en büyük değer verir
val = max(numbers)

# alfabeye sırasına göre en büyük ve en küçük değer
val = max(letters)
val = min(letters)

#  aralık alma
val = numbers[3:]
val = numbers[:2]

# listedeki bir değeri değiştirme
numbers[3] = 20

# listeye değer ekleme
# en sona ekler
numbers.append(50)

# belli bir indexse değer ekleme
numbers.insert(4,70)
numbers.insert(-1,22)

# index değerine göre yada default olarak en sondaki değeri siler
numbers.pop()
numbers.pop(3)

# veri değereine göre silen metod
numbers.remove(22)

# listedeki elemanların büyüklük değerine göre sıralama yapar
# sort()
numbers.sort()

# listedeki verileri büyüklüklerine göre terten sıralar
numbers.reverse()

# listenin uzunluğu
print(len(numbers))

# liste içinde bir veriden kaç tane var olduğunu sayar
# count()

print(numbers.count(10))

# listenin içindei tüm verileri siler
numbers.clear()


print(numbers)
print(val)