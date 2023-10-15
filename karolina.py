import requests
from lxml import html

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
    print(articul)
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
    print(name)
    all_names.append(name)
print(all_names)




'<div class="x-premium-product-title__model-name">'
'<div class="x-premium-product-title-new__model-name">'

'</div></h1><div class="x-premium-product-page__prices-info">'
'</div></h1><div class="x-product-page__prices-info">'

'''