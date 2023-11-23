# try:    
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()

# file = open("newfile.txt","r", encoding = "utf-8")

# ********** for döngüsü

# for i in file:
#     print(i, end="")
# end="" aralarında bırakılan boş satırları kaldırır

# ********** read() fonksiyonu ile dosya içeriğini getirme

# content1 = file.read()

# print("içerik 1")
# print(content1)

# content2 = file.read()

# print("içerik 2")
# print(content2)

# Burda ikincisinin yazılmama sebebi
# Dosya kapanmadı ve imleç dosyanın sonunda kaldı 
# Bu yüzden okuyacak birşey bulamadı

# Her bir karakter bir byte
# content = file.read(5) # İçeriğin ilk beş karakterini alır
# content = file.read(3) #dosya kapanmadığı için imlecin kaldığı yerden sonra üç karakteri alır
# content = file.read(3)

# print(content)

# ********** readline() fonksiyonu
# Her seferinde bir satır okur


# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# ********** readlines() fonksiyonu
# satırlardan bir dizi elemanı oluşturur
# Her satırdaki bilgiyi listede bir eleman olarak ekler

# liste = file.readlines()

# print(liste[0])
# print(liste[1])
# print(liste[2])

# file.close()

# Dosya okuma fonksiyonu
# with burda bir blok oluşturur
# Bu blokta dosyayı açar ve kendi kapar

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0) # imlecin konumunu güncelledik
    print(file.tell()) # imlecin konumunu verir
    content2 = file.read(10)
    print(content2)