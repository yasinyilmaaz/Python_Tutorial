# Döngüler 
# Döngüler bizi tekrarlı işllemlerden kurtarır
# kod yükünü azaltır
# alan tasarufu ve maliyeti azaltır
# mesela 10 kere ekrana merhaba yazdırcaksak bunu
# print ile 10 satır yazmamız gerekir
# ama döngü ile 3 satır ile hallederiz

numbers = [1,2,3,4,5]

# for değer atayacağımız değişken in liste:
#   her döngüde yapılacak işlemler

 
  
for a in numbers:
    print(a + 'Hello')

tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a,b)

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.items():
    print(key, value)