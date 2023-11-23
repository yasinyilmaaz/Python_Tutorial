from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2) # iki saniye uyutma
driver.maximize_window() # tam ekran haline getirilir
# driver.save_screenshot("github.com-homepage.png") # ekran görüntüsü alır

url = "https://github.com/yasinyilmaaz"
driver.get(url)

print(driver.title) #sayfanın başlığını yazdırdık

if "yasinyilmaaz" in driver.title:
    driver.save_screenshot("github-yasinyilmaaz.png")

time.sleep(2)

driver.back() # bir geri sekmeye gider
# driver.forward() # bir ileri sekmeye gitmek için

time.sleep(2)

driver.close() # ekranı kapattık

