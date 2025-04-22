from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from model import Model

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def limit_amount_length(value):
    return len(value) <= 5

def show_window_screen(window):
    from classes.dao.transactionsDAO import TransactionDAO
    from classes.dao.userDAO import UserDAO
    from classes.dao.loggingDAO import LoggingDAO

    from ..eng_menu.gui import show_window_screen as show_menu_screen
    from ..eng_withdraw.gui import show_window_screen as show_withdraw_screen
    from ..eng_transaction_ok.gui import show_window_screen as show_transaction_ok_screen
    from ..eng_transaction_denied.gui import show_window_screen as show_transaction_denied_screen

    for widget in window.winfo_children():
        widget.destroy()

    vcmd_amount = window.register(limit_amount_length)

    model = Model()

    card = window.card_number
    user = model.get_user_by_card(card)

    def escape_button(event):
        window.unbind("<Escape>")
        show_menu_screen(window)
        print("Menu screen showed")

    def enter_button(event):
        window.unbind("<Return>")
        amount_text = entry_1.get()
        try:
            amount = float(amount_text)

            if amount <= 0:
                raise ValueError("Amount must be positive")

            result = model.withdraw(card, amount)

            if "successful" in result:
                model.add_log(user.user_id, f"withdraw {amount}")
                show_transaction_ok_screen(window)
            else:
                model.add_log(user.user_id, f"Withdraw failed: {amount}")
                show_transaction_denied_screen(window)

        except Exception as e:
            print("Error in input: ", e)
            model.add_log(user.user_id, f"Withdraw failed: {amount_text}")
            show_transaction_denied_screen(window)

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
        529.5,
        300.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        font=("Merriweather", 24),
        validate="key",
        validatecommand=(vcmd_amount, '%P'),
        highlightthickness=0
    )
    entry_1.place(
        x=353.0,
        y=258.0,
        width=353.0,
        height=82.0
    )

    entry_1.configure(
        justify="center"
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        514.73681640625,
        298.7626953125,
        image=image_image_1
    )
    canvas.image_1 = image_image_1
