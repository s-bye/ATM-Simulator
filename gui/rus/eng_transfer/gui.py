from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from model import Model

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_window_screen(window):
    from ..eng_transaction_ok.gui import show_window_screen as show_transaction_ok_screen
    from ..eng_transaction_denied.gui import show_window_screen as show_transaction_denied
    from classes.dao.userDAO import UserDAO
    from classes.dao.transactionsDAO import TransactionDAO
    from classes.dao.loggingDAO import LoggingDAO
    from ..eng_menu.gui import show_window_screen as show_menu_screen


    for widget in window.winfo_children():
        widget.destroy()

    model = Model()

    sender_card = window.card_number
    sender = model.get_user_by_card(sender_card)

    def escape_button(event):
        window.unbind("<Escape>")
        show_menu_screen(window)
        print("Menu screen showed")

    def enter_button(event):
        window.unbind("<Return>")

        receive_card = entry_1.get()
        amount_text = entry_2.get()


        try:
            amount = float(amount_text)

            if amount < 0:
                raise ValueError("Amount must be positive")

            if receive_card == sender_card:
                raise ValueError("You cannot send yourself")

            result = model.transfer_funds(sender_card, receive_card, amount)

            if 'successful' in result:
                model.add_log(sender.user_id, f"transfer to {receive_card} - {amount}")
                show_transaction_ok_screen(window)
                print("Transfer is successful")
            else:
                model.add_log(sender.user_id, f"transfer FAILED to {receive_card} - {amount}")
                show_transaction_denied(window)
                print('Transfer is NOT successful')

        except Exception as e:
            print(f" Error of transfer: {e}")
            show_transaction_ok_screen(window)

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
        475.0,
        166.0,
        anchor="nw",
        text="Enter data",
        fill="#000000",
        font=("Merriweather Bold", 24 * -1)
    )

    canvas.create_text(
        355.0,
        232.0,
        anchor="nw",
        text="Card Number:",
        fill="#000000",
        font=("Merriweather Regular", 16 * -1)
    )

    canvas.create_text(
        352.0,
        374.0,
        anchor="nw",
        text="Transfer Amount:",
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
