from src.appDecimalBinary import *
from src.appBinaryDecimal import *

class Aplication:
    def __init__(self):
        self.root = Tk()
        self.root.title('Conversiones')
        self.root.config(bg="azure2")
        self.root.geometry("280x200")
        notebook = ttk.Notebook(self.root, padding=10)
        DecimaltoBinary(notebook)
        BinarytoDecimal(notebook)
        notebook.grid(column=0, row=0, padx=20, pady=20)
        self.root.mainloop()





