import pandas as pd
import requests
import math

all_urls = ['https://www.lamoda.ru//p/mp002xg032mz/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01y0v/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xg032lp/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xg032ms/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xc0168x/accs-mothercare-kepka/', 'https://www.lamoda.ru//p/mp002xw0tn8g/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xw00sfj/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0qezy/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0tn8p/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xm253to/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0sgri/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01z1s/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg034gm/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bp/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033az/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xtl/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01ya2/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01z1r/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb020g6/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xtt/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01y9x/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xw01ams/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xzn/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bj/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01ish/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg034gn/accs-gloriajeans-kepka/', 'https://www.lamoda.ru//p/mp002xw0iv0r/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xsl/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bu/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bi/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xsq/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xst/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb020fx/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb020g2/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xt4/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xsv/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01xty/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01z1v/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01isk/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb020g7/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01ia4/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bf/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg02eoy/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033bh/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg02fjw/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033b2/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033b3/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033b8/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg02ep4/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg034gr/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg02ep3/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xg033b9/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0iv0w/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0iv0o/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xw01alc/accs-sela-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0sgrf/accs-gloriajeans-beysbolka/', 'https://www.lamoda.ru//p/mp002xb01ikl/accs-mothercare-kepka/', 'https://www.lamoda.ru//p/mp002xw0x6d7/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xw0x6d8/accs-befree-beysbolka/', 'https://www.lamoda.ru//p/mp002xw19m9w/accs-befree-beysbolka/']

all_articuls = ['MP002XG032MZ', 'MP002XB01Y0V', 'MP002XG032LP', 'MP002XG032MS', 'MP002XC0168X', 'MP002XW0TN8G', 'MP002XW00SFJ', 'MP002XW0QEZY', 'MP002XW0TN8P', 'MP002XM253TO', 'MP002XW0SGRI', 'MP002XB01Z1S', 'MP002XG034GM', 'MP002XG033BP', 'MP002XG033AZ', 'MP002XB01XTL', 'MP002XB01YA2', 'MP002XB01Z1R', 'MP002XB020G6', 'MP002XB01XTT', 'MP002XB01Y9X', 'MP002XW01AMS', 'MP002XB01XZN', 'MP002XG033BJ', 'MP002XB01ISH', 'MP002XG034GN', 'MP002XW0IV0R', 'MP002XB01XSL', 'MP002XG033BU', 'MP002XG033BI', 'MP002XB01XSQ', 'MP002XB01XST', 'MP002XB020FX', 'MP002XB020G2', 'MP002XB01XT4', 'MP002XB01XSV', 'MP002XB01XTY', 'MP002XB01Z1V', 'MP002XB01ISK', 'MP002XB020G7', 'MP002XB01IA4', 'MP002XG033BF', 'MP002XG02EOY', 'MP002XG033BH', 'MP002XG02FJW', 'MP002XG033B2', 'MP002XG033B3', 'MP002XG033B8', 'MP002XG02EP4', 'MP002XG034GR', 'MP002XG02EP3', 'MP002XG033B9', 'MP002XW0IV0W', 'MP002XW0IV0O', 'MP002XW01ALC', 'MP002XW0SGRF', 'MP002XB01IKL', 'MP002XW0X6D7', 'MP002XW0X6D8', 'MP002XW19M9W']

all_names = ['Бейсболка Sela ', 'Бейсболка Sela ', 'Бейсболка Sela ', 'Бейсболка Sela ', 'Кепка Mothercare ', 'Бейсболка Befree ', 'Бейсболка Befree ', 'Бейсболка Befree ', 'Бейсболка Befree ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Sela ', 'Бейсболка Sela ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Кепка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Gloria Jeans ', 'Бейсболка Sela ', 'Бейсболка Gloria Jeans ', 'Кепка Mothercare ', 'Бейсболка Befree ', 'Бейсболка Befree ', 'Бейсболка Befree ']


# Создаем словарь с данными
data = {"Ссылки на товары": all_urls, "Название": all_names, "Артикул": all_articuls}

# Создаем DataFrame из словаря
df = pd.DataFrame(data)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)


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



