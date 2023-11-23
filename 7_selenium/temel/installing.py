# https://selenium-python.readthedocs.io/ selenium kütüphanesi
# Sayfa Etkileşimi
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page
from selenium import webdriver
# Daha önceden tarayıcının driverini buraya indirip ekklemek gerekir

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = "https://karmayazilim.pythonanywhere.com/"
driver.get(url) # verdiğimiz urlyi açar

