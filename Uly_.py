import requests

query = "носки"
query = query.replace(' ', '+')
query = query.lower()

url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'

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



all_prices = []
for n in range(60):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    price_in = text.find('"price":"')
    text = text[price_in + 9:]
    price_out = text.find('"},"original"')
    price = text[:price_out]
    all_prices.append(price)
print(all_prices)

all_brands = []
for n in range(60):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    brand_in = text.find(':"Другие товары ')
    text = text[brand_in + 16:]
    brand_out = text.find('","type":"brand"')
    brand = text[:brand_out]
    all_brands.append(brand)
print(all_brands)





