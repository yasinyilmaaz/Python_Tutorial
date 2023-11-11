# sözlük gibi düşünebiliriz
#  içinde birden fazla değişken var ve bnlara karşılık
# gelen bir veri var 
# Mesela sözlük açtığımızda
# hello: "merhaba"
# buna benzer bir yapı taşır
# key - value yapısıda denir

# süslü parantezler arasına yazılır

direction ={
    "Hello":"merhaba","name":"isim"
}

print(direction["Hello"])
print(direction["name"])

users = {
    'yasinyilmaz': {
        'age': 18,        
        'roles': ['user'],
        'email': 'yasin@gmail.com',
        'address': 'Eskişehir',
        'phone': '1230001'
    }
}
# birden fazla böyle değerler barındırabilir

print(users['yasinyilmaz']['email'])