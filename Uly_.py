import requests

url = 'https://www.lamoda.ru/p/mp002xw0k8sc/clothes-calzedonia-bryuki/'
r = requests.get(url)
text = r.text
print(text)

#Бренд и категория
#< / div > < / div > < / a >
#< a
#href = "/b/29606/brand-calzedonia/"
#class ="x-link x-link__label x-link__underline x-premium-product-links__link"