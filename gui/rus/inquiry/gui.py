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
    396.0,
    171.0,
    anchor="nw",
    text="Доступные средства",
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
window.resizable(False, False)
window.mainloop()
