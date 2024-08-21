import  requests
from bs4 import  BeautifulSoup

url = "https://"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.passer")

rows = soup.find_all("tr") # поиск всех рядов в таблице
data = []
for row in rows:            # перебор всех колонок в ряде
    cols = row.find-all("td")
#    cleaned_cols = [col.text.strip('xy') for col in cols]
    cleaned_cols = [col.text.strip() for col in cols]
    data.append(cleaned_cols)

print(data)

