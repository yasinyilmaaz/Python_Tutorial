# generator
# bir diziyi anlık olarak kullancaksak yani bir kereden fazla kullanacaksak generatorus kullanabiliriz
# Bellekte yer kaplamayan bir iterators oluşturur
# generator içinde direk itterators olarak çalışır 


# def cube():
#     for i in range(5):
#         yield i ** 3
#           yield ile bir değer alıyoruz ve bu değer bir yerde saklanmaz ve ulaşılmaz

# for i in cube():
#     print(i)

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator))