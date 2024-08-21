import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Firefox()

# Открытие CSV файла для записи
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'зарплата', 'ссылка на вакансию'])

    for page in range(40):  # Цикл по страницам от 0 до 39
        url = f'https://hh.ru/vacancies/programmist?customDomain=1&page={page}'
        driver.get(url)
        time.sleep(3)  # Ожидание загрузки страницы

        vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')
        print(f"Парсинг страницы {page}")

        parsed_data = []

        for vacancy in vacancies:
            try:
                title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
                company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
                salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
                link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
            except Exception as e:
                print(f"Произошла ошибка при парсинге: {e}")
                continue

            parsed_data.append([title, company, salary, link])

        # Запись данных в CSV файл после обработки каждой страницы
        writer.writerows(parsed_data)

# Закрытие веб-драйвера
driver.quit()
