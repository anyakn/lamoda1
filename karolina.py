import requests

query = "кепки"
query = query.replace(' ', '+')
query = query.lower()

url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'

#  url = url+'&page='+ str(number)

r = requests.get(url)
all_urls = []
text = r.text

for _ in range(60):
    i = text.find('<div class="x-product-card__card"><a href="')
    text = text[i+43:]
    j = text.find('" class=')
    end_url = text[:j]
    url = 'https://www.lamoda.ru/' + end_url
    text = text[j:]
    all_urls.append(url)
print(all_urls)

all_articuls = [] # Найдем артикулы
for x in range(60):
    url = all_urls[x]
    html = requests.get(url)
    text = html.text
    i = text.find('[{"key":"sku","title":"Артикул","value":"')
    text = text[i + 41:]
    j = text.find('"},{"key":')
    articul = text[:j]
    all_articuls.append(articul)
print(all_articuls)


all_names = [] # Найдем названия
for x in range(60):
    url = all_urls[x]  # Найдем название
    html = requests.get(url)
    text = html.text
    i = text.find('"seo_title":"')
    text = text[i + 13:]
    j = text.find('- цвет:')
    name = text[:j]
    all_names.append(name)
print(all_names)

import pandas as pd


# Создаем словарь с данными
data = {"Ссылки на товары": all_urls, "Название": all_names, "Артикул": all_articuls}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

# Выводим DataFrame в виде таблицы
print(df)
