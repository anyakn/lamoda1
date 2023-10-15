import requests

query = input('Введите ваш запрос: ')
query = query.replace(' ', '+')
query = query.lower()

url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'

# url = url+'&page='+ str(number)

r = requests.get(url)
all_urls = []
text = r.text

for _ in range(60):
    i = text.find('<div class="x-product-card__card"><a href="')
    text = text[i+43:]
    j = text.find('" class=')
    url = text[:j]
    text = text[j:]
    all_urls.append(url)

print(all_urls)