# Inheritance (Kalıtım): Miras alma
# Üst class özelliklerinin yanında kendine özel özellikleride olan class yapısı
# Mesela bir canlıya hayvan diyebilmemiz için beli özellikleri taşır bu genel class olsun 
# hayvanlarda kendi içinde belli kısımlara ayrılır. Mesela omurgalı, omurgasız. Bu ikisi 
# Hayvanlar class'ından kalıtım alır ve kendi içindede kendi özellikleride vardır. 
# bir alta geldiğimizde gene ayrılır.Mesela omurgalılar Memeliler, sürüngenler, kuşlar, 
# Aynı şekil bunlar içinde geçerlidir.


# Tüm kişiler için geçerli olan kısmı person class da belirtik
# Onlardan kalıtım alarak students ve teacher sınıflarını oluşturduk
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')

    # override
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self,fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Ali','Yılmaz')
s1 = Student('Çınar','Turan', 1256)
t1 = Teacher('Serkan','Yılmaz','Math')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName+ ' '+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()