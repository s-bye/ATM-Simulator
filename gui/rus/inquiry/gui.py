from pathlib import Path
from classes.dao.userDAO import UserDAO
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    from ..menu.gui import show_window_screen as show_menu_screen

    for widget in window.winfo_children():
        widget.destroy()

    user_dao = UserDAO()
    card = window.card_number
    user = user_dao.get_user_by_card(card)
    balance = user_dao.get_balance(card) if user else "N/A"

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
        bg="#FFFFFF",
        height=600,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        512.0,  # Center horizontally (1024 / 2)
        171.0,
        anchor="center",
        text="Доступные средства",
        fill="#000000",
        font=("Merriweather Bold", 24 * -1)
    )

    # Display the balance in the center of the window
    canvas.create_text(
        512.0,  # Center horizontally (1024 / 2)
        300.0,  # Center vertically (600 / 2)
        anchor="center",
        text=f"{balance:.1f} сом" if balance != "N/A" else "N/A",
        fill="#000000",
        font=("Merriweather Bold", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        515.0,
        302.7626953125,
        image=image_image_1
    )

    canvas.image_1 = image_image_1