# TODO button functions withdraw with DB
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

    def som_2000():
        print("2000 som withdraw")

    def som_1000():
        print("1000 som withdraw")

    def som_500():
        print("500 som withdraw")

    def som_200():
        print("200 som withdraw")

    def som_5000():
        print("5000 som withdraw")

    def som_8000():
        print("8000 som withdraw")

    def som_10000():
        print("10000 som withdraw")

    def another_amount_button():
        from ..another_amount.gui import show_window_screen as show_another_amount_screen
        show_another_amount_screen(window)
        print("Another amount showed")

    def escape_button(event):
        window.unbind("<Escape>")
        from ..menu.gui import show_window_screen as show_menu_screen
        show_menu_screen(window)
        print("Menu screen showed")

    window.bind("<Escape>", escape_button)

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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_2000(),
        relief="flat"
    )
    button_1.place(
        x=7.0,
        y=231.0,
        width=258.0,
        height=60.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_1000(),
        relief="flat"
    )
    button_2.place(
        x=7.0,
        y=327.0,
        width=258.0,
        height=60.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_500(),
        relief="flat"
    )
    button_3.place(
        x=7.0,
        y=422.0,
        width=258.0,
        height=60.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_200(),
        relief="flat"
    )
    button_4.place(
        x=7.0,
        y=512.0,
        width=258.0,
        height=60.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_5000(),
        relief="flat"
    )
    button_5.place(
        x=757.0,
        y=231.0,
        width=258.0,
        height=60.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_8000(),
        relief="flat"
    )
    button_6.place(
        x=757.0,
        y=327.0,
        width=258.0,
        height=60.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: som_10000(),
        relief="flat"
    )
    button_7.place(
        x=757.0,
        y=422.0,
        width=258.0,
        height=60.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: another_amount_button(),
        relief="flat"
    )
    button_8.place(
        x=757.0,
        y=512.0,
        width=258.0,
        height=60.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        510.73681640625,
        274.762451171875,
        image=image_image_1
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
    canvas.button_7 = button_image_7
    canvas.button_8 = button_image_8

