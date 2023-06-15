import requests


apikey = "858A97FA-0E48-4922-BDEC-E464C918B842"


def get_rate(desplegable1, desplegable2):
    url = f"https://rest.coinapi.io/v1/exchangerate/{desplegable1}/{desplegable2}?apikey={apikey}"
    try: # Este try except es un print para el programador por si la url es equivoca.
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return True, data['rate']           
        else:
            return False, data['error']       
        
    except requests.exceptions.RequestException as e:
        return False, str(e)
        

    