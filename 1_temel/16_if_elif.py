# if - elif
#  eğer koşulumuzda birden fazla durum varsa
# Örnek vermek gerekiyorsa:
# sayının pozitif mi negatif mi olması
# Burda bir durumda sıfır olabilir
# Bu durumda çoklu koşul kullanmaıyız

# input bize kullanıcıdan değer girmemizi sağlar
num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')