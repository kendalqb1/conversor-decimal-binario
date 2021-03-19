from src.logic import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class BinarytoDecimal:
    def __init__(self, notebook):
        page1 = ttk.Frame(notebook)
        notebook.add(page1, text="Binario a Decimal")

        label1 = ttk.Label(page1, text="Binario:")
        label1.grid(column=0, row=0, padx=4, pady=4)

        binary = StringVar()
        self.entryBinary1 = ttk.Entry(page1, textvariable=binary)
        self.entryBinary1.grid(column=1, row=0, padx=4, pady=4)

        label2 = ttk.Label(page1, text="Decimal:")
        label2.grid(column=0, row=1, padx=4, pady=4)

        self.decimal = StringVar()
        entryBinary1 = ttk.Entry(page1, textvariable=self.decimal, state='readonly')
        entryBinary1.grid(column=1, row=1, padx=4, pady=4)

        button1 = ttk.Button(page1, text="Convertir", command=self.printDecimal)
        button1.grid(column=1, row=2, padx=4, pady=4)


    def printDecimal(self):
        data = self.entryBinary1.get()
        try:
            int(data)
        except ValueError:
            mb.showinfo("Error","Es una cadena de string o el dato es vacio")
        else:
            self.decimal.set(binary_to_decimal(self.entryBinary1.get()))




