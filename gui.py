import tkinter
from tkinter import *
from PIL import ImageTk, Image
# -------------------------------------------------------------------------------------------------------------------------------
#                                           Main Gui Class to set the foundation
# -------------------------------------------------------------------------------------------------------------------------------
class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('COFFEE PLEASE')
        self.geometry('800x600')

        menubar = FileMenu(self)
        self.config(menu=menubar)

        mainImage = Image.open("coffee_pic.jpg")
        imageLabel = ImageTk.PhotoImage(mainImage)

        mainLabel = tkinter.Label(image=imageLabel)
        mainLabel.image = imageLabel

        mainLabel.place(x=0.5, y=0.5)

# -------------------------------------------------------------------------------------------------------------------------------
#                                           Menu Class used for the file menu
# -------------------------------------------------------------------------------------------------------------------------------
class FileMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        fileMenu = Menu(self, tearoff=False, background='white', fg='black', activeforeground='black')
        self.add_cascade(label="Main Menu", underline=0, menu=fileMenu)

# -------------------------------------------------------------------------------------------------------------------------------
#                                           Executes Main Program, starts with Gui()
# -------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = Gui()
    app.mainloop()