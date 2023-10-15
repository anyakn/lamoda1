import requests
url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D1%88%D1%82%D0%B0%D0%BD%D1%8B+%D0%BA%D0%B0%D1%80%D0%B3%D0%BE&submit=y&gender_section=women&sort=price_asc'
r = requests.get(url)
text = r.text

n_in = text.find('</h2><span class="d-catalog-header__product-counter">')
text = text[n_in+53:]

n_out = text.find('товар')
number = str(text[:n_out])
print(number)

url1 = 'https://www.lamoda.ru/p/rtlada204601/shoes-philippplein-sapogi/'
r1 = requests.get(url1)
text1 = r1.text
print(text1)


country_in = text1.find('"title":"Страна производства","value":')

text1 = text1[country_in+39:]

country_out = text1.find('"')
country = text1[:country_out]
print(country)
