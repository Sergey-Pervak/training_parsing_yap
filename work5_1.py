# Импортируйте библиотеку BeautifulSoup.
from bs4 import BeautifulSoup

card_html = """
<div class="price sale" data-behavior="product-price" itemprop="offers"> 
  <meta itemprop="price" content="3490"> 
  <div class="title" data-behavior="price-title">
    <span class="text">Богатырские доспехи, шт.</span>
  </div>
  <div class="old-price">
    <span class="price" value="3490" data-behavior="price-old">3 490 рублей</span>
  </div>
  <div class="nameplate color-green" data-behavior="price-discount">Скидка 700 рублей</div> 
  <span class="price" value="2790" data-behavior="price-now">2 790 рублей</span>  
</div>
"""

# Сварите богатырский «суп» из HTML-кода.
soup = BeautifulSoup(card_html, features='lxml')

# Найдите в «супе» актуальную стоимость богатырских доспехов.

# result = soup.find_all('span', attrs={'data-behavior': 'price-now'})
result = soup.find('span', attrs={'data-behavior': 'price-now'})

# Посчитайте, сколько будет стоить пять комплектов богатырских доспехов.

# total_sum = 5 * int(result[0]['value'])
total_sum = 5 * int(result['value'])

print('В казну полагается принести:', total_sum, 'рублей')
