from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    from ..authentication.gui import show_window_screen as show_authentication_screen

    for widget in window.winfo_children():
        widget.destroy()

    def return_to_auth(event):
        window.unbind("<Escape>")
        show_authentication_screen(window)

    window.bind("<Escape>", return_to_auth)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        515.0,
        279.762451171875,
        image=image_image_1
    )

    canvas.image_1 = image_image_1