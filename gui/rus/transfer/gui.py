# TODO Exceptions
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

    def escape_button(event):
        window.unbind("<Escape>")
        from ..menu.gui import show_window_screen as show_menu_screen
        show_menu_screen(window)
        print("Menu screen showed")

    def enter_button(event):
        window.unbind("<Return>")
        from ..transaction_ok.gui import show_window_screen as show_transaction_ok_screen
        # TODO implement functionality for transfer with DB
        show_transaction_ok_screen(window)
        print("Transaction OK screen showed")

    window.bind("<Escape>", escape_button)
    window.bind("<Return>", enter_button)

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
        511.73681640625,
        302.7626953125,
        image=image_image_1
    )

    canvas.create_text(
        430.0,
        166.0,
        anchor="nw",
        text="Введите данные",
        fill="#000000",
        font=("Merriweather Bold", 24 * -1)
    )

    canvas.create_text(
        351.0,
        232.0,
        anchor="nw",
        text="Номер карты:",
        fill="#000000",
        font=("Merriweather Regular", 16 * -1)
    )

    canvas.create_text(
        351.0,
        374.0,
        anchor="nw",
        text="Сумма перевода:",
        fill="#000000",
        font=("Merriweather Regular", 16 * -1)
    )

    canvas.create_rectangle(
        1.0,
        99.0,
        1028.0018310546875,
        100.0,
        fill="#000000",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        533.5,
        303.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=357.0,
        y=261.0,
        width=353.0,
        height=82.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        533.5,
        442.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=357.0,
        y=400.0,
        width=353.0,
        height=82.0
    )

    canvas.image_1 = image_image_1