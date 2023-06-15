from tkcriptoquery.viewtk import Display, Desplegable, Button
import tkinter as tk
from tkinter import Tk, Label, PhotoImage

HEIGHT = 800 # Constante de alto
WIDTH = 600 # Constante de ancho


class Controller(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cripto's conversor")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        #self.configure(bg='blue') <<-- aqui le decimos a la pantalla pintate de azul

        # Subir la imagen de fondo de pantalla
        self.background_image = PhotoImage(file=r"C:\users\alejandro\downloads\dollar.png")
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Dividimos la pantalla en 8 filas y 8 columnas previamente para no tener problemas a la hora de colocar los buttons/display en el grid.
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        ''' OPCION ALTERNATIVA A LA DIVISION DEL GRID
        for row in range(8):
            self.grid_rowconfigure(i, weight=1)
        for column in range(7):
            self.grid_columnconfigure(i, weight=1)
        '''

        # Mostramos el 1 desplegable en pantalla y le introducimos los datos que tiene que contener ademas de fijar el resultado en el buttom
        opciones_desplegable1 = ["BTC", "ETH", "USDT", "BNB", "USDC"]
        self.desplegable1 = Desplegable(self,"Criptos", *opciones_desplegable1)
        self.desplegable1.grid(column=1, row=2)

        # Mostramos el 2 desplegable en pantalla y le introducimos los datos que tiene que contener ademas de fijar el resultado en el buttom
        opciones_desplegable2 = ["EUR", "USD", "JYP"]
        self.desplegable2 = Desplegable(self,"FIAT", *opciones_desplegable2)
        self.desplegable2.grid(column=3, row=2)
        

        # Mostramos el boton en pantalla
        self.boton = Button(self, 'CONVERT')
        self.boton.grid(column=5, row=2)

        # Mostramos el Display en pantalla
        self.display = Display(self)
        self.display.grid(column=1, row=6, columnspan=6, sticky='WE')



     

        




    