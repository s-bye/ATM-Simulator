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
    from ..menu.gui import show_window_screen as show_menu_screen
    from ..transaction_ok.gui import show_window_screen as show_transaction_ok_screen
    from ..transaction_denied.gui import show_window_screen as show_transaction_denied_screen
    from classes.dao.userDAO import UserDAO
    from classes.dao.loggingDAO import LoggingDAO
    from classes.dao.transactionsDAO import TransactionDAO

    for widget in window.winfo_children():
        widget.destroy()

    model = Model()

    card = window.card_number
    user = model.get_user_by_card(card)

    def escape_button(event):
        window.unbind("<Escape>")
        show_menu_screen(window)
        print("Menu screen showed")

    def enter_button(event):
        window.unbind("<Return>")
        new_pin = entry_1.get().strip()

        try:
            if not new_pin.isdigit():
                raise ValueError("PIN must be a digit")

            if len(new_pin) != 4:
                raise ValueError("New PIN must contain 4 numbers")

            model.update_pin(user.user_id, int(new_pin))
            model.add_log(user.user_id, f"PIN changed")
         ##TODO: must be changed to show_pin_changed_ok_screen()
            show_transaction_ok_screen(window)
        except Exception as e:
            print("Error of changing PIN: ", e)
            model.add_log(user.user_id, f"PIN changed failed")
            ##TODO: must be changed to show_pin_changed_denied_screen()
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
    canvas.create_text(
        298.0,
        310.0,
        anchor="nw",
        text="Введите Ваш новый PIN",
        fill="#000000",
        font=("Merriweather Black", 32 * -1)
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
        510.73681640625,
        302.762451171875,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        512.5,
        423.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6D6D6",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=372.0,
        y=373.0,
        width=281.0,
        height=98.0
    )
    canvas.image_1 = image_image_1