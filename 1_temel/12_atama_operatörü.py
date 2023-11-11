# ATAMA OPERATÖRLERİ

# x= 5
# y=10

x, y, z = 5,16,20

# x, y = y, x

# x'i 5 arttırdık
# x += 5          # x = x + 5 # bu iki şekilde de aynı işlemi yapıyoruz
# Çıkartma işlemi
# x -= 5          # x = x - 5
# Çarpma İşlemi
# x *= 5          # x = x * 5
# Bölme işlemei
# x /= 5          # x = x / 5
# mod alıyruz. Yani bölümden kalan değer
# x %= 5          # x = x % 5
# Bölümd kısmını veriyor
# y //= 5         # y = y // 5
# Kare alma işlemi
# y **= z         # y = y ** z 

# tuple atamanın farklı yöntemi
values = 1, 2, 3, 4, 5

print(values)
print(type(values)) 

# Burdaki bu yıldız kalanların hepsini al demek
# Bu yıldızı önce koyup sondaki değeri ayrıda alabiliriz
x, y, *z = values

print(x, y, z)
print(x, y, z[1])