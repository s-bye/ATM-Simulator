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

def limit_card_number_length(value):
    return len(value) <= 16

def limit_pin_length(value):
    return len(value) <= 4

def show_window_screen(window):
    user_dao = UserDAO()
    window.login_attempts = 3

    for widget in window.winfo_children():
        widget.destroy()

    vcmd_card_number = window.register(limit_card_number_length)
    vcmd_pin = window.register(limit_pin_length)

    # Initialize warning message IDs
    window.card_warning_id = None
    window.pin_warning_id = None

    def show_card_warning(message):
        if window.card_warning_id:
            canvas.delete(window.card_warning_id)
        window.card_warning_id = canvas.create_text(
            529.5,
            437.0,
            text=message,
            font=("Merriweather", 14),
            fill="#FF0000",
            anchor="center"
        )

    def clear_card_warning(event=None):
        if window.card_warning_id:
            canvas.delete(window.card_warning_id)
            window.card_warning_id = None

    def show_pin_warning(message):
        if window.pin_warning_id:
            canvas.delete(window.pin_warning_id)
        window.pin_warning_id = canvas.create_text(
            529.5,
            580.0,
            text=message,
            font=("Merriweather", 14),
            fill="#FF0000",
            anchor="center"
        )

    def clear_pin_warning(event=None):
        if window.pin_warning_id:
            canvas.delete(window.pin_warning_id)
            window.pin_warning_id = None

    def on_enter_pressed(event=None):
        card = entry_1.get()
        pin = entry_2.get()

        # Clear previous warnings
        clear_card_warning()
        clear_pin_warning()

        # Validate card number
        if len(card) == 0:
            show_card_warning("Card number cannot be empty")
            return
        elif len(card) < 16:
            show_card_warning("Card number must be 16 digits")
            return
        else:
            entry_1.configure(bg="#D6D6D6")

        # Validate PIN
        if len(pin) == 0:
            show_pin_warning("PIN cannot be empty")
            return
        elif len(pin) < 4:
            show_pin_warning("PIN must be 4 digits")
            return
        else:
            entry_2.configure(bg="#D6D6D6")

        try:
            if user_dao.check_pin(card, int(pin)):
                window.card_number = card
                entry_2.configure(bg="#D6D6D6")
                show_menu_screen(window)
            else:
                window.login_attempts -= 1
                entry_2.configure(bg="#FF0000")
                show_pin_warning(f"Incorrect PIN ({window.login_attempts} attempts left)")
                print(f"Login attempts left: {window.login_attempts}")  # TODO add to gui
                if window.login_attempts == 0:
                    show_access_denied_screen(window)
        except Exception as e:
            entry_2.configure(bg="#FF0000")
            show_pin_warning("Invalid input")
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
        bg="#FFFFFF",
        height=600,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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
        validate="key",
        validatecommand=(vcmd_card_number, "%P"),
        highlightthickness=0
    )
    entry_1.place(
        x=353.0,
        y=342.0,
        width=353.0,
        height=82.0
    )

    entry_1.configure(
        font=("Merriweather", 24),
        justify="center"
    )
    entry_1.bind("<Key>", clear_card_warning)  # Clear warning on typing

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
        validate="key",
        validatecommand=(vcmd_pin, "%P"),
        highlightthickness=0
    )
    entry_2.place(
        x=353.0,
        y=481.0,
        width=353.0,
        height=82.0
    )

    entry_2.configure(
        font=("Merriweather", 24),
        justify="center",
    )
    entry_2.bind("<Key>", clear_pin_warning)  # Clear warning on typing

    canvas.create_rectangle(
        1.0,
        99.0,
        1028.0018310546875,
        100.0,
        fill="#000000",
        outline=""
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        513.0,
        300.0,
        image=image_image_1
    )

    canvas.image_1 = image_image_1