

def test_input(arrays, mensaje):
    arrays = list(map(lambda x : x.upper(), arrays))
    respuesta = input(mensaje).upper()
    while respuesta not in arrays:
        print("Debe ser una de las siguientes opciones ", arrays)
        respuesta = input(mensaje)
    return respuesta

def output(is_ok, cripto, data, fiat):
    if is_ok:
        print(f"1 {cripto} vale {data:.2f}{fiat}")
    else:
        print(f"Se ha producido el error: {data}")

