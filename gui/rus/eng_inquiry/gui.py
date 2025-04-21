from pathlib import Path
from classes.dao.userDAO import UserDAO
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from model import Model

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    from ..eng_menu.gui import show_window_screen as show_menu_screen

    for widget in window.winfo_children():
        widget.destroy()

    model = Model()
    card = window.card_number
    user = model.get_user_by_card(card)
    balance = model.get_balance(card) if user else "N/A"

    def escape_button(event):
        window.unbind("<Escape>")
        show_menu_screen(window)
        print("Menu screen showed")

    def enter_button(event):
        window.unbind("<Return>")
        show_menu_screen(window)
        print("Menu screen showed")

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
    canvas.create_text(
        431.0,
        171.0,
        anchor="nw",
        text="Available means",
        fill="#000000",
        font=("Merriweather Bold", 24 * -1)
    )

    canvas.create_text(
        518.0,
        253.0,
        anchor="nw",
        text=" ",
        fill="#000000",
        font=("Merriweather Bold", 24 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        515.0,
        302.7626953125,
        image=image_image_1
    )
    canvas.image_1 = image_image_1
