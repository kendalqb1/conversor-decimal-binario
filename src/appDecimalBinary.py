from src.logic import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class DecimaltoBinary:
    def __init__(self, notebook):
        page1 = ttk.Frame(notebook)
        notebook.add(page1, text="Decimal a Binario", padding=10)

        label1 = ttk.Label(page1, text="Decimal:")
        label1.grid(column=0, row=0, padx=4, pady=4)

        decimal = StringVar()
        self.entryDecimal1 = ttk.Entry(page1, textvariable=decimal)
        self.entryDecimal1.grid(column=1, row=0, padx=4, pady=4)

        label2 = ttk.Label(page1, text="Binario:")
        label2.grid(column=0, row=1, padx=4, pady=4)

        self.binary = StringVar()
        entryBinary1 = ttk.Entry(page1, textvariable=self.binary, state='readonly')
        entryBinary1.grid(column=1, row=1, padx=4, pady=4)

        button1 = ttk.Button(page1, text="Convertir", command=self.printBinary)
        button1.grid(column=1, row=2, padx=4, pady=4)



    def printBinary(self):
        data = self.entryDecimal1.get()
        try:
            int(data)
        except ValueError:
            mb.showinfo('Error', 'El dato esta vacio o es una cadena de texto')
        else:
            self.binary.set(decimal_to_binary(int(self.entryDecimal1.get())))