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
print(num)

pages = math.ceil(num/60)
print(pages)

all_urls = []
for page in range(1, pages):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc' + '&page=' + str(page)
    print(url)
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
print(len(all_urls))

all_brands = []
all_articuls = []
all_countries = []
all_prices = []
all_discounts = []
all_names = []

for n in range(len(all_urls)):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    brand_in = text.find(':"Другие товары ')
    text = text[brand_in + 16:]
    brand_out = text.find('","type":"brand"')
    brand = text[:brand_out]
    all_brands.append(brand)

    articul_in = text.find('[{"key":"sku","title":"Артикул","value":"')
    text = text[articul_in + 41:]
    articul_out = text.find('"},{"key":')
    articul = text[:articul_out]
    all_articuls.append(articul)

    country_in = text.find('"title":"Страна производства","value":')
    text1 = text[country_in + 39:]
    country_out = text.find('"')
    country = text[:country_out]
    all_countries.append(country)

    price_in = text.find('"price":"')
    text = text[price_in + 9:]
    price_out = text.find('"},"original"')
    price = text[:price_out]
    all_prices.append(price)

    discount_in = text.find('"discount_lamoda_and_loyalty_and_action"')
    if discount_in != -1:
        text = text[discount_in + 41:]
        discount_out = text.find(',')
        discount = text[:discount_out]
    else:
        discount = 0
    all_discounts.append(discount)

    names_in = text.find('"seo_title":"')
    text = text[names_in + 13:]
    names_out = text.find('- цвет:')
    name = text[:names_out]
    all_names.append(name)

print(all_brands)
print('')
print(all_articuls)
print('')
print(all_countries)
print('')
print(all_prices)
print('')
print(all_discounts)
print('')
print(all_names)
print('')

data = {"Ссылки на товары": all_urls, "Название": all_names, "Артикул": all_articuls, "Цена": all_prices, "Скидка": all_discounts, "Бренд":all_brands, "Страна": all_countries}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)
