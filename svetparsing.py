import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(3)

luminaires = driver.find_elements(By.CLASS_NAME, "_Ud0k")

parsed_data = []

for luminaire in luminaires:
    try:
        name = luminaire.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text
        price = luminaire.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH").text
        link = luminaire.find_element(By.CSS_SELECTOR, "a.ui-GPFV8").get_attribute("href")
    except:
        print("Произошла ошибка при парсинге")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("divanlamp.csv", "w", newline = '', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow(['Название товара', 'Цена товара', 'Ссылка на товар'])
    writer.writerows(parsed_data)
