from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now() # anlık tarih ve saat
simdi = datetime.today() # anlık tarih ve saat


result = datetime.now()
result = simdi.year # yıl
result = simdi.month # ay 
result = simdi.day # gün
result = simdi.hour # saat
result = simdi.minute # dakika
result = simdi.second # saniye



result = datetime.ctime(simdi) # ay ve gün yazı şeklinde 
result = datetime.strftime(simdi,'%Y') #yıl
result = datetime.strftime(simdi,'%X') # saat tamamı
result = datetime.strftime(simdi,'%d') # gün sayı
result = datetime.strftime(simdi,'%A') #gün yazı
result = datetime.strftime(simdi,'%B') # ay yazı 
result = datetime.strftime(simdi,'%Y %B %A') #yıl ay gün

# print(result)

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0) # sıfırlar ilk tarih

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

print(result)
