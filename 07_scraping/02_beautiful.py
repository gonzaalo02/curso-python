
from bs4 import BeautifulSoup
import requests

url ="https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
    print("La peticion fue existosa")

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    title_tag = soup.title
    print("El título de la página es:", title_tag.string)

    metas = soup.title.parent.find_all('meta')
    print(metas)

    ## find price using bs
    #price_span = soup.find('span', class_='rc-prices-fullprice')
    #print("El precio es:", price_span.string)

    ## find all the prices
    #price_span = soup.find_all(class_='rc-prices-fullprice') # el span es opcional, si no sabes lo que es lo puedes quitar. Es mas rapido buscar por clase
    #for price in price_span:
    #    print("El precio es:", price.string)

    # find each product and get the name and the price
    products = soup.find_all(class_='rc-productselection-item')
    for product in products:
        name = product.find(class_="list-title").text
        price = product.find(class_="rc-prices-fullprice").text
        print(f"El producto con las características:\n {name}\nPrecio de {price}\n\n")
