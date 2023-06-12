import requests

apikey = "858A97FA-0E48-4922-BDEC-E464C918B842"

url = f"https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apikey}"

response = requests.get(url)

print(response.status_code)
print(response.text)