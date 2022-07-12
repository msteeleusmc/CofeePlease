import tkinter
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

# -------------------------------------------------------------------------------------------------------------------------------
#                                           Global variable used for each GUI page
# -------------------------------------------------------------------------------------------------------------------------------
global_variable = None

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

        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        global new_frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(anchor='center')

# -------------------------------------------------------------------------------------------------------------------------------
#                                           Menu Class used for the file menu
# -------------------------------------------------------------------------------------------------------------------------------
class FileMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        fileMenu = Menu(self, tearoff=False, background='white', fg='black', activeforeground='black')
        self.add_cascade(label="Main Menu", underline=0, menu=fileMenu)

# -------------------------------------------------------------------------------------------------------------------------------
#                                               Main Page Class
# -------------------------------------------------------------------------------------------------------------------------------
class MainPage(Frame, Menu):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)

        global_variable = MainPage

        frame = Frame(self)
        frame.grid(row=1, column=0)
        title_label = ttk.Label(frame, text='COFFEE PLEASE', style='title.TLabel')
        title_label.grid(row=1, column=1)

        but1 = ttk.Button(text='Power ON/OFF', command=None)
        but2 = ttk.Button(text='Add Water', command=None)
        but3 = ttk.Button(text='Add Coffee', command=None)
        but4 = ttk.Button(text='Brew', command=None)

        but1.place(x=100, y=30)
        but2.place(x=100, y=100)
        but3.place(x=100, y=170)
        but4.place(x=100, y=240)

# -------------------------------------------------------------------------------------------------------------------------------
#                                           Executes Main Program, starts with Gui()
# -------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = Gui()
    app.mainloop()