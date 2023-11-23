# encapsulation
# eğer içerdeki fonksiyonu dışardaki fonksiyon içinde çağırmazsak
# içerdeki fonksiyon çalışmaz
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)
# içerdeki fonksiyonu direk olarak çalıştırısak direk hata alırız
# inner_increment(10)

# Dıştaki fonksiyon ile girilen değerin uygun olup olmadığına baktık 
# içteki fonksiyon ile bir azaltarak tekrarlı çarpım yaptık


# def factorial(number):
#     #Sayı olup olmadığını kontrol ettik
#     if not isinstance(number, int):
#         raise TypeError("number must be an integer")
#     # SAYININ SIFIRDAN BÜYÜK OLUP OLMADIĞNA BAKTIK
#     if not number >=0:
#         raise ValueError("number must be zero or positive")

#     def inner_factorial(number):
#         if number <= 1:
#             return 1

#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)
# try:
#     print(factorial("4"))
# except Exception as ex:
#     print(ex)


# FONKSİYON İÇİNDE FONKSİYON GERİ DÖNDÜRME
# Eğer bir fonksiyonda fonksiyon geri döndürüyorsak
# Dıştaki fonksiyona atama yaptıktan sora içtekinide atamayapmamız gerekir
def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

# Dıştaki fonksiyonu çalıştırdık
toplama = islem("toplama")
# sonraiçteki fonksiyona veri gönderdik
print(toplama(1,3,5,6,7))

carpma = islem("carpma")
print(carpma(1,2,3,6,4))