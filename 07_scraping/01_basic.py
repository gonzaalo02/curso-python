
# pip3 install requests - instala la dependecia para hacer peticiones

import requests
import re

# con el request no puedes saltarte los paywalls y los captchas de las webs. La ventaja es que es muy rapido y sencillo de implementar. Muy manueal para encontrar lo que te interesa


url ="https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
    print("Conexión exitosa")
    html = response.text
    # print(html)

    # regular expression para guardar el precio del macbook air
    precio_pattern = r"<span class=\"rc-prices-fullprice\">(.*?)</span>"
    match = re.search(precio_pattern, html)
    if match:
        print("El precio del MacBook Air es:", match.group(1))

    # get the title if the pattern is found
    title_pattern = r"<title>(.*?)</title>"
    match_title = re.search(title_pattern, html)

    if match_title:
        print("El título de la página es:", match_title.group(1))