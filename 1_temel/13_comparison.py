# Karşılaştırma Operatörü
# İki veya daha fazla değerin eşitsizliğini buluyoruz

a, b, c, d = 5, 5, 10, 4

password = '1234'
username = 'yasinyılmaz'

# eşitse True döndürür
result = (a == b) # True
result = (a == c) # False
result = ('ssss'== username)
result = ('yasinyılmaz'== username) #True
# Eşit değilse True döndürür
result = (a != b)
result = (a != c)
# Büyük ise True döndürür
result = (a > c)
# Küçükse True döndürür
result = (a < c)
# Büyük yada eşit ise True döndürür
result = (a >= b)
# Küçük yada eşit ise True döndürür
result = (c <= b)
# 1 = True
# 0 = False
result = (True == 1)
result = (False == 0)
result = False + True + 40

print(result)
