from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

    def show_rus_authentication_screen():
        from ..authentication.gui import show_window_screen as show_authentication_screen
        show_authentication_screen(window)
        print("Authentication RUS showed")

    def show_eng_authentication_screen():
        from ..eng_authentication.gui import show_window_screen as show_authentication_screen
        show_authentication_screen(window)
        print("Authentication ENG showed")

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
    canvas.create_rectangle(
        1.0,
        99.0,
        1028.0018310546875,
        100.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        506.73681640625,
        265.7624855041504,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_rus_authentication_screen(),
        relief="flat"
    )
    button_1.place(
        x=0.0,
        y=309.0,
        width=260.0,
        height=90.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_eng_authentication_screen(),
        relief="flat"
    )
    button_2.place(
        x=764.0,
        y=309.0,
        width=260.0,
        height=87.0
    )

    canvas.image_1 = image_image_1
    canvas.button_1 = button_1
    canvas.button_2 = button_2
    canvas.button_1 = button_image_1
    canvas.button_2 = button_image_2
