from criptoquery.view import test_input, output
from criptoquery.models import criptos, fiats, get_rate

class Controller:
    def mainloop(self):
        while True:
            # Usando la vista para entrada de datos por parte de usuario
            cripto = test_input(criptos, "Que criptomoneda quieres saber? ")
            fiat = test_input(fiats, "Que moneda quieres? ")

            # Usar el modelo para obtener un dato de internet
            is_ok, data = get_rate(cripto, fiat)

            # Tendria que ir a la vista, pero todavia no
            output(is_ok, cripto, data, fiat)

            # Preguntar si seguimos, la pregunta la delegamos en la vista
            more_conversions = test_input(('S', 'N'), "¿Quieres introducir más mondeas? ")
            if more_conversions != "S":
                break