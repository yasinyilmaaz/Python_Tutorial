# lambda
# kısa işlemleri yapmak için tek satırlık anonim fonksiyon

numbers = [1,3,5,9,10,4]

check_even = lambda num: num%2==0

# result = list(filter(check_even, numbers))
# result = list(filter(lambda num: num%2==0, numbers))
# result = list(filter(check_even, numbers))

result = check_even(numbers[2])


print(result)