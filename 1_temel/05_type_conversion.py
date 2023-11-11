# tip dönüşümleri bir değişkeni vaya veriyi farlı bir veri türünde kullanmamız gerektiğinde 
# kullanabiiriz

# type() komutu le bir değerin hangi veri türünde olduğunu öğreniriz

x = 5               #int
y = 2.5             #float
name = 'Yasin'      #str
isOnline = True     #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))


# int to float

x = float(x)
print(x)


# float to int

y = int(y)
print(y)

result = str(x) + str(y)
print(result)
print(type(result))

# bool to str

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

# bool to int

isOnline = False

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))