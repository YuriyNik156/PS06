import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--n77Dj8TY8VIUF0yM")

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, "[data-qa='serp-item__title']").text
        company = vacancy.find_element(By.CSS_SELECTOR, "[data-qa='vacancy-serp__vacancy-employer']").text
        salary = vacancy.find_element(By.CSS_SELECTOR, "div.narrow-container--HaV4hduxPuElpx0V").text
        link = vacancy.find_element(By.CSS_SELECTOR, "a.magritte-link___b4rEM_5-0-10").get_attribute("href")
    except:
        print("Произошла ошибка при парсинге")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline = '', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название вакансии', 'Название компании', 'Заработная плата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)