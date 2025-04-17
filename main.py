from tkinter import Tk
from gui.rus.idle.gui import show_window_screen

if __name__ == "__main__":
    window = Tk()
    window.geometry("1024x600")
    window.configure(bg="#FFFFFF")
    window.title("FaceIT - ATM")
    window.iconbitmap("gui/assets/icon.ico")
    window.resizable(False, False)

    show_window_screen(window)

    window.mainloop()