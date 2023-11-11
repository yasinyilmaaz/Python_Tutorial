# Mantıksal Operatör
# or
# Veya anlamındadır
# birden fazla koşullu durumda 
# biri bile true ise cevap doğrudur

# True, False => True
# True, True => True
# False, False => False

x = 10

result = (x > 0) or (x % 2 == 0)

# and (ve)
# en az koşullardan biri False dönüyorsa 
# Cevap Falsedir

# True, True => True
# True, False => False

result = (x > 5) and (x < 10)  

# not (değili)
# Koşulda çıkan değerin tam tersini alır
# False => True
# True => False

result = not(x > 0)


print(result)