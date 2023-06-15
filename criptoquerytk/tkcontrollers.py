import tkinter as tk
import requests
from criptoquerytk.tkview import Desplegable
from criptoquerytk.tkmodel import get_rate




class Converter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.criptos = Desplegable(self, "CRIPTO", "BTC", "ETH", "USDT", "BNB", "USDC")
        self.criptos.grid(column=0, row=0)
        self.criptos.selected_option.trace("w", self.validate_button)

        self.fiats = Desplegable (self, "FIAT", "EUR", "USD", "JPY")
        self.fiats.grid(column=1, row=0) 
        self.fiats.selected_option.trace("w", self.validate_button)

        self.result = tk.Label(self)

        self.result.grid(row=1, column=0)

        tk.Button(self, text="Consultar", command=self.get_rate).grid(row=1, column=1)
    '''
    def validate_button(self, *args):
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

        status = cripto != "CRIPTO" and fiat != "FIAT"
    '''
        

    def get_rate(self):
        cripto = self.criptos.selected_option.get()
        fiat = self.fiats.selected_option.get()

    

        if cripto != "CRIPTO" and fiat != "FIAT":
            is_ok, data = get_rate(cripto, fiat)
            if is_ok:
                self.result.config(text=data)
            else:
                self.result.config(text="Se ha producido un error en la consulta")
        else:
            self.result.config(text="Debes seleccionar ambos valores")
    



























        '''
        self.title("Variables de control")

        self.numero = tk.DoubleVar() # almacena flotantes
        self.numero.set(23)
        self.entero = tk.IntVar() # almacena enteros
        self.text = tk.StringVar() # almacena strings
        self.booleano = tk.BooleanVar() # Almacena booleanos


        self.label = tk.Label(self, width=30)
        self.label.pack(side=tk.TOP)
        

        tk.Button(self, text='Numero', command=lambda: self.label.config(text=self.numero.get())).pack(side=tk.TOP)
        tk.Entry(self, textvariable=self.numero).pack(side=tk.TOP)# tk.entry esta enganchandose a self.numero con lo cual lo modifica

        self.numero.trace("w", lambda: print(self.numero.get()))
        '''