# error => hata

# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

# error handling => hata yönetimi

# gelecek hatayı belirttik
# (ZeroDivisionError,ValueError) 
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz')
#     print(e)


# Tüm oluşacak hatalar için çalışr
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz', ex)
    else: # except olmazsa çalışacak durum
        break
    finally: # hata olsun veya olmasın en son çalışacak kısımdır
        print('try except sonlandı.')
