# Nesne Tabanlı Programlama(OOP)
# class
# class yapısını bir fabrikaya benzetebiliriz
# Biz bilgileri veriyoruz oda bize o bilgileri işleyip bir obje oluşturuur 
# Tekrarlı kullanımı ortadan kaldırır


# daha kaılıcı bir örnek verelim
# Siz bir ustasınız ve halı dokuyorsunuz
# bir iş yapmanız gerektiğinde her seferide siz dokumalısınız
# Ama bir halı makineniz(oop class) varsa
# siz her çağırdığınızda o sizin yerine hızlıca dokuyup teslim ediyor

class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

        # methods

    # instance methods
    def intro(self):
        print('Hello There. I am '+ self.name )

    # instance methods
    def calculateAge(self):
        return 2023 - self.year
    
    def __str__(self):
        return f"My name is {self.name}"
    
    def __len__(self):
        return 2023 - self.year
    
    def __del__(self):
        print('Person silindi')


# object (instance)
p1 = Person(name='ali', year= 1990) 
p2 = Person(name ='yağmur', year = 1995)

# updating
p1.name = 'ahmet'
p1.address = 'kocaeli' 

# accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

p1.intro()
p2.intro()

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')

print(len(p1))