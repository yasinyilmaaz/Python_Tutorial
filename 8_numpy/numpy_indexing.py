import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

# normal dizi eleman çağırma geçerlididir
result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]

# Çok boyutlu dizide veriye ulaşma
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[1]
result = numbers2[0,2] # 1. satır 3. değer
result = numbers2[:,2] # hepsinin 3. değeri
result = numbers2[:,0]
result = numbers2[:,0:2]
result = numbers2[-1,:]
result = numbers2[:2,:2]


arr1 = np.arange(0,10)
arr2= arr1.copy() # verileri kopyalar
# adresler farklı

arr2[0] = 20

print(arr1)
print(arr2)





print(result)