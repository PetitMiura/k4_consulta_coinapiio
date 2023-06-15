import tkinter as tk
from tkinter.font import Font
from tkcriptoquery.modeltk import get_rate



class Display(tk. Frame):
    def __init__(self,location):
        
        super().__init__(location, width=600, height=50)
        self.pack_propagate = False
        
        self.label = tk.Label(self, background="#000000", text= "", foreground="#ffffff",
                              anchor=tk.E, padx=8, 
                              font=Font(family="Arial", size="40"))
        self.label.pack(side= tk.TOP, fill =tk.BOTH, expand=True)
    
    def typing(self, text):
        self.label.config(text=text)

class Desplegable(tk. Frame):
    def __init__(self, location, title, *options):

        super().__init__(location, width=200, height=50)
      
        
        # Variable para almacenar la opción seleccionada
        selected_option = tk.StringVar(self)
        selected_option.set(title)  # Opción seleccionada por defecto

        # Función que se ejecuta cuando se selecciona una opción
        def on_option_selected(*args):
            print("Opción seleccionada:", selected_option.get())

        # Crear el menú desplegable
        option_menu = tk.OptionMenu(self, selected_option, *options)
        option_menu.pack()

        # Asociar la función on_option_selected al cambio de opción
        selected_option.trace("w", on_option_selected)

class Button(tk. Frame):
    def __init__(self, location, text):
        super().__init__(location, width=200, height=50)

        self.button = tk.Button(self, text=text, command=get_rate)
        self.text = text

        
        self.button.pack()
        

        
        