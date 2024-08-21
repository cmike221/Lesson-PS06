import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Firefox()

# Открытие CSV файла для записи
with open("all_lights.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'ссылка'])

#    print("Начало теста")
    for page in range(8):  # Цикл по страницам от 0 до 7
        if page == 0:
            url = 'https://www.divan.ru/category/svet'
        else:
            url = f'https://www.divan.ru/category/svet/page-{page}'

        driver.get(url)
        time.sleep(3)  # Ожидание загрузки страницы
        items = driver.find_elements(By.CLASS_NAME, 'lsooF')
        print(f"Парсинг страницы {page}")

        parsed_data = []

        for item in items:
            try:
                name = item.find_element(By.CSS_SELECTOR, 'a.ProductName span[itemprop="name"]').text
                price = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
                link = item.find_element(By.CSS_SELECTOR, 'link[itemprop="url').get_attribute('href')
            except Exception as e:
                print(f"Произошла ошибка при парсинге: {e}")
                continue

            parsed_data.append([name, price, link])

        # Запись данных в CSV файл после обработки каждой страницы
        writer.writerows(parsed_data)

# Закрытие веб-драйвера
driver.quit()
