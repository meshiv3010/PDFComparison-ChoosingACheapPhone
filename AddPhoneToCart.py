from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "automatedUser26@example.com"
password = "4r4nd0mp4ssw0rd"

driver = webdriver.Chrome()
url = "https://www.demoblaze.com/"
driver.get(url)

driver.find_element(By.ID,"login2").click()
time.sleep(2)
driver.find_element(By.ID,"loginusername").send_keys(username)
driver.find_element(By.ID,"loginpassword").send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[contains(text(),'Phones')]").click()
time.sleep(3)

h5_elements = driver.find_elements(By.XPATH, "//h5")

lowest_price = 999999999
lowest_price_index = 0

filtered_prices_strings = []

for price_text in h5_elements:
    if price_text.text.startswith('$'):
        filtered_prices_strings.append(price_text.text)

for i, price_string in enumerate(filtered_prices_strings, start=1):
    price = float(price_string.replace('$', ''))
    if price < lowest_price:
        lowest_price = price
        lowest_price_index = i

xpath_of_phone = f"/html/body/div[5]/div/div[2]/div/div[{lowest_price_index}]/div/div/h4/a"
link_element = driver.find_element(By.XPATH, xpath_of_phone)
link_element.click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Add to cart')]").click()
time.sleep(2)

driver.quit()
