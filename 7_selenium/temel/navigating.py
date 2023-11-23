from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url ="http://github.com"
driver.get(url)


searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]") # x_path ile inputa ulaştık
time.sleep(1)
searchInput.send_keys("python") # içine python yazdırdık
time.sleep(2)
searchInput.send_keys(Keys.ENTER) # enter bastırdık
time.sleep(2)
# result = driver.page_source # tüm kotları alır
result = driver.find_elements_by_css_selector(".repo-list-item h3 a")

for element in result:
    print(element.text)

driver.close() #sayfayı kapattık