# NUMPY
# Bir Python kütüphanesi olan numpy ile diziler üzerinde çok farklı işlemleri çok kolaylıkla, gayet pratik bir şekilde gerçekleştirebiliriz.

# Numpy dizi özellikleri:

# Numpy dizilerinin veri türü ndarray dir. 
# Numpy dizileri tek boyutlu olabildiği gibi, çok boyutlu matrisler de olabilir.
# Python dizilerinden numpy dizileri oluştururken türü (int, float) belirlenebilir.
# Eğer elle girilmezse değerlerin türüne göre otomatik oluşturulur.

import numpy as np # numpy kütüphanesi eklendi 

# result = np.array([1,3,5,7,9]) # Tek boyutlu bir dizi(vektör)
# print(result.size) # dizi uzunluğu
# print(type(result)) # türü
# print(result.dtype)

result = np.arange(1,10) # 1-10 arası tek boyutlu dizi oluşturur
result = np.arange(1,100,4) # 1-100 arası 4 artarak tek boyutlu dizi oluşturur
result = np.zeros(10) # sıfırlardan oluşan tek boyutlu dizi
result = np.ones(10) #birlerden oluşan tek boyutlu dizi
# np.linspace(dizi başlangıç,dizi bitiş,alınacak değer sayısı)
result = np.linspace(0,100,5)
# result = np.linspace(0,5,5)
result = np.random.randint(0,10) # 0-10 arası random tam sayı
# result = np.random.randint(20)
result = np.random.rand(5) # 0-1 arasında random istenen değerde dizi oluşturur
result = np.random.randn(5) # rand benzer ama eksi değerlerde var
np_aray = np.arange(50)
result = np_aray.reshape(5,10) # (5,10) iki boyutlu dizi oluşturur
# yani 5 satır 10 sütündan oluşacak
print(result.sum(axis=1)) #her satırın toplamını dizi olarak verir
print(result.sum(axis=0)) # her sütunu toplar ve dizi olarak verir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() # en büyük 
result = rnd_numbers.min() # en küçük
result = rnd_numbers.mean() # ortalama
result = rnd_numbers.argmax() # en büyük değerin index i
result = rnd_numbers.argmin() # en küçük değerin index i
result = np.full((2,2),7) # dizinin boyutları , dizi veri değeri
result = np.eye(3) # verilen boyutlarda dizi oluşturur



print(result)
# print(np_aray)




