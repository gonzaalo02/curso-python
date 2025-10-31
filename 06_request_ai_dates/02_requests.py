# Como hacer peticiones a APIs con python
# con y sin dependencias

# 1. Sin dependencias (dificil y sin dependencias)
import urllib.request
import json
import os
os.system("cls")

#api_post_url = "https://jsonplaceholder.typicode.com/posts/"
#
#try:
#    response = urllib.request.urlopen(api_post_url) # hace la peticion
#    data = response.read() # lee el contenido de la respuesta
#    json_data = json.loads(data.decode("utf-8"))  # decodifica el JSON
#    print(json_data)  # imprime los datos obtenidos
#    response.close()
#except urllib.error.URLError as e:
#    print(f"Error al hacer la petición: {e.reason}")


# 2. Con dependencias (hay diferentes dependencias) (requests)
import requests

print ("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"

response = requests.get(api_posts)
#print(response.json())

json = response.json()
print(json[0])

# 3. POST
print ("\nPOST:")

api_posts = "https://jsonplaceholder.typicode.com/posts/"
try:
    input={
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(api_posts, json=input) # Se puede enviar la url y el json directamente
    print(response.status_code) # info de la respuesta
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la petición: {e}")

# 4. put

print ("\nPUT:")
api_post = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.put(api_post, json={
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1
    })
    print(response.status_code) # info de la respuesta
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la petición: {e}")


# usar la API de GPT-4 o de OpenAI
# ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAPI_KEY = "sk-XXXXXX"
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAPI_KEY}"
}
data = {
    
}
