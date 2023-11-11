# Kendi yapacağımız bir projede kendi istediğimiz bir hata durumuda olabilir
#  mesela şifrenin özel durumları olabilir
# Bunun için kendimiz bir hata atayabiliriz
# Bunu "raise" ile yaparız

# import re (regex)
#  bir veri içinde elli şartlar verere karama yapılabilir
# nerdeyse tüm programlama dillerinde vardır
# kendine özgü komutları vardır


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw): # küçük alfabetik karakterin olup olmadığını arattık
        raise Exception("parola küçük harf içermelidir.") 
    elif not re.search("[A-Z]", psw):  # Büyük alfabetik karakterin olup olmadığını arattık
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw): #rakam olup olmadığı
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]", psw): # alpha numeric karakter var mı
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif re.search("\s",psw): # boşluk karakteri
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("geçerli parola")

password = input("Bir parola giriniz: ")

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola: else")
finally:
    print("validation tamamlandı.")