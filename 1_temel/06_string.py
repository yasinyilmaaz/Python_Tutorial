# string veriler üstünde matematiksel işlemler yapamadığımız veri türüdür
# " " veya '' tırnakların arasına yazabiliriz
# ''' '''' bu çoklu satırda yazmamızı sağlar ve boşluklarıda ekler


# print("Yasin")
# print('Yılmaz')
# print('''Yasin
#     Yılmaz
#     19''')

# String verilere değişken atayıp bunları yazdırırken toplayadabiliriz
name ="Yasin"
surname="Yılmaz"
age=18
print("My name is " + name + " " + surname + '. I am ' + str(age) + " years old")

# Bunu format işlemi ile daha kolay birşekilde yapabiliriz
# Format işleminde verimizin başına f işareti koyarak süslü parantezler içine verilerimizi koyabiliriz

print(f"My name is {name} {surname}. I am {age} years old")

# Str metodlar
# yazılımda yüksek oranda ilk değer 0 olur bu yüzden sıfırdan başlayarak saymalıyız!!!!!!
uni = "Sakarya Uygulamalı Biimler Üniversitesi 5. yılı"

# 5 indexteki değeri verir
result = uni[5]

# 0-5 arasındaki değerleri verir
result = uni[0:5]
result = uni[:5] # eğer ilk değere hiçbir şey yazmaksak o en baştan başlatır

# 10 indexten son indexse kadar alır
result = uni[10:]

# son değeri almak için
result = uni[-1]

# tamamını almak için
result = uni[::]

# tamamını tersten almak için 
result = uni[::-1]

# ikişerli atlayarak tüm değerleri alır
result = uni[::2]

# str uzunluğunu bulmak için
# print(len(uni))

# Hepsini büyük harf yapma
result = uni.upper()

# Hepsini küçük harf yapma
result = uni.lower()

# Her kelimenin baş harfini büyük yapma
result = uni.title()

# İlk kelimenin baş harfini büyütme
result = uni.capitalize()

# split()
# Veriyi default olarak boşluktan yada verdiğiniz değerden ayıran metod
# liste oluşturu
result = uni.split()

# join
# liste olarak verilmiş bir veriyi verdiğimiz karakteri araya koyarak birleştiren metod

result = "---".join(result)

news = "     Akşam Haberi         "

# sol tarafındaki verilen karakteri veya default olarak boşluğu kaldırır
result = news.strip()

# Hangi karakter ile başladığına baktığımız metod
result = name.startswith("Y")

# Hangi karakter ile bittiğine baktığımız metod
result = name.endswith("n")

#  veride arar ve ilk index değerini verir
result = news.find("Akşam")

# replace()
# İlk verdiğimiz veri ile ikinci verdiğimiz veriyle değiştirir

result = news.replace("Akşam","Sabah")

# center()
# ilk verdiğimiz değer verimizin uzunluğu
# ikinci değer ise boş kalan alanlara gelecek karakter
# ortalar
selam = "selam"

result = selam.center(50,"*")

print(result)


# Daha fazla metodu tarayıcıdan aratarak buraya ekleyebiliriz