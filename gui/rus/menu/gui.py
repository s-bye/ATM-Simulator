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

    def withdraw_button():
        from ..withdraw.gui import show_window_screen as show_withdraw_screen
        show_withdraw_screen(window)
        print("Withdraw showed")

    def deposit_button():
        from ..deposit.gui import show_window_screen as show_deposit_screen
        show_deposit_screen(window)
        print("Deposit showed")

    def transfer_button():
        from ..transfer.gui import show_window_screen as show_transfer_screen
        show_transfer_screen(window)
        print("Transfer showed")

    def change_pin_button():
        from ..change_pin.gui import show_window_screen as show_change_pin_screen
        show_change_pin_screen(window)
        print("Change PIN showed")

    def inquiry_button():
        from ..inquiry.gui import show_window_screen as show_inquiry_screen
        show_inquiry_screen(window)
        print("Inquiry showed")

    def idle_button():
        from ..idle.gui import show_window_screen as show_idle_screen
        show_idle_screen(window)
        print("Idle showed")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.create_rectangle(
        1.0,
        99.0,
        1028.0018310546875,
        100.0,
        fill="#000000",
        outline="")

    canvas.place(x = 0, y = 0)

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.   create_image(
        510.73681640625,
        262.762451171875,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: withdraw_button(),
        relief="flat"
    )
    button_1.place(
        x=6.0,
        y=262.0,
        width=262.0,
        height=91.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: transfer_button(),
        relief="flat"
    )
    button_2.place(
        x=6.0,
        y=349.0,
        width=260.0,
        height=87.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_pin_button(),
        relief="flat"
    )
    button_3.place(
        x=2.0,
        y=436.0,
        width=267.0,
        height=87.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: deposit_button(),
        relief="flat"
    )
    button_4.place(
        x=768.0,
        y=262.0,
        width=271.0,
        height=91.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: idle_button(),
        relief="flat"
    )
    button_5.place(
        x=768.0,
        y=436.0,
        width=276.0,
        height=93.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: inquiry_button(),
        relief="flat"
    )
    button_6.place(
        x=768.0,
        y=349.0,
        width=273.0,
        height=94.0
    )

    canvas.image_1 = image_image_1
    canvas.button_1 = button_1
    canvas.button_2 = button_2
    canvas.button_3 = button_3
    canvas.button_4 = button_4
    canvas.button_5 = button_5
    canvas.button_6 = button_6
    canvas.button_1 = button_image_1
    canvas.button_2 = button_image_2
    canvas.button_3 = button_image_3
    canvas.button_4 = button_image_4
    canvas.button_5 = button_image_5
    canvas.button_6 = button_image_6
