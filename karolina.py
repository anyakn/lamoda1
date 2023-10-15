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

data = {"Ссылки на товары": all_urls, "Название": all_names, "Артикул": all_articuls}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)

import requests
url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D1%88%D1%82%D0%B0%D0%BD%D1%8B+%D0%BA%D0%B0%D1%80%D0%B3%D0%BE&submit=y&gender_section=women&sort=price_asc'
r = requests.get(url)
text = r.text

n_in = text.find('</h2><span class="d-catalog-header__product-counter">')
text = text[n_in+53:]

n_out = text.find('товар')
number = str(text[:n_out])
print(number)