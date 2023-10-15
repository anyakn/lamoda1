import pandas as pd
import requests
import math

query = input('Введите запрос: ')
query = query.replace(' ', '+')
query = query.lower()

url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'
r = requests.get(url)
text = r.text

num_in = text.find('</h2><span class="d-catalog-header__product-counter">')
text = text[num_in+53:]
num_out = text.find('товар')
num = int(text[:num_out])

pages = math.ceil(num/60)

all_urls = []
for page in range(1, pages+1):
    url = url + '&page=' + str(page)
    r = requests.get(url)
    text = r.text
    for _ in range(60):
        i = text.find('<div class="x-product-card__card"><a href="')
        text = text[i + 43:]
        j = text.find('" class=')
        end_url = text[:j]
        url = 'https://www.lamoda.ru/' + end_url
        text = text[j:]
        all_urls.append(url)
print(all_urls)



# Создаем словарь с данными
data = {"Ссылки на товары": all_urls, "Название": all_names, "Артикул": all_articuls}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)


