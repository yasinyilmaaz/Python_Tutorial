# Koşullu ifadeler
# Yapacağımız işlemde iki durum varsa 
#  koşul kullanmamız gerekebilir
# if else
# if:eğer bu koşul doğru ise yapacağımız işlem
# else:değilse yapacağımız işlem
# if koşul yazılır
# else koşul yazılmaz(en kötü seneryo)
# if tek başına da kullanabiliriz
# if in içindeki koşul true dönerse if çalışır değilse else çalışır

open = True

if(open):
    print("Açık")
else:
    print("Kapalı")




# kullanıcı kiriş örneği
username = 'yasinyılmaz'
password = '1234'

if (username == 'yasinyılmaz'):

    if (password == '12345'):
        print('Hoş geldiniz')
    else:
        print('parola yanlış')
        
else:
    print('username yanlış')