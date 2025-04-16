from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from classes.dao.userDAO import UserDAO
from ..menu.gui import show_window_screen as show_menu_screen
from ..access_denied.gui import show_window_screen as show_access_denied_screen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    user_dao = UserDAO()
    window.login_attempts = 3

    for widget in window.winfo_children():
        widget.destroy()

    def on_enter_pressed(event=None):
        card = entry_1.get()
        pin = entry_2.get()
        try:
            if user_dao.check_pin(card, int(pin)):
                window.card_number = card
                show_menu_screen(window)
            else:
                window.login_attempts -= 1
                print(f"Login attempts left: {window.login_attempts}")  # TODO add to gui
                if window.login_attempts == 0:
                    show_access_denied_screen(window)
        except Exception as e:
            show_access_denied_screen(window)
    def escape_button(event):
        window.unbind("<Escape>")
        from ..idle.gui import show_window_screen as show_idle_screen
        show_idle_screen(window)
        print("IDLE screen showed")

    window.bind("<Escape>", escape_button)
    window.bind("<Return>", on_enter_pressed)

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
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        529.5,
        384.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=353.0,
        y=342.0,
        width=353.0,
        height=82.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        529.5,
        523.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=353.0,
        y=481.0,
        width=353.0,
        height=82.0
    )

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
        513.0,
        300.0,
        image=image_image_1
    )

    canvas.image_1 = image_image_1