# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 

# açma yöntemleri
# file = open("newfile.txt","w")
# file = open("C:\Users\Yasin\Desktop\Python\Python_Tutorial/3_Dosya_Yönetimi/newfile.txt","w")
# file.close() #kapatma işlemini yaptık

# Türkçe karakter yaptı
# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Yasin Yılmaz") # Dosyanın içine yazdı
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# Eski bilgilerle birlikte tutar. Kısaca ekler
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nHalil Yılmaz")
# file.write("Halil Yılmaz\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x",encoding='utf-8')


# "r": (Read) okuma. dosya konumda yoksa hata verir.
# Varsayılan olarak atanır. Eğer komut belirtmezsek bu atanır