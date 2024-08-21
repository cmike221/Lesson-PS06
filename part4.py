import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://hh.ru/vacancies/programmist?customDomain=1&page=0'
#url = 'https://hh.ru/vacancies/programmist?customDomain=1&page=39'
driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

print("Старт")
print(vacancies)
for vac in vacancies:
    print(vac)

print("Стоп")
parsed_data = []

for vacancy in vacancies:
    try:
        tittle = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print("Произошла ошибка при парсинге")
        continue

    parsed_data.append([tittle, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)
