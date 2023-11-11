# break
# döngüyü durdurmak içindir


# while x < 5:    
#     x+=1
#     if x == 2:
#         break
#     print(x)

# continue
# o anki döngüyü atlar ve kaldığı yerden devam eder
# döngü durmaz

# while x < 5:    
#     x+=1
#     if x == 2:
#         continue
#     print(x)

#   ÖRNEK
'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

sayi = int(input('sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')