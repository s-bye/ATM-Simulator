from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x600")
window.configure(bg = "#FFFFFF")


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
window.resizable(False, False)
window.mainloop()
