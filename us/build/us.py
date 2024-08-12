from pathlib import Path
import subprocess

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# mencari path utama
BASE_PATH = Path(__file__).parent
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_us = BASE_PATH / "assets/frame0"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH_us / Path(path)

# mencari path untuk button navigasi
tulung = Path(__file__).parent.parent.parent
path_to_kret = tulung / "kreate/build/kret.py"
path_to_main = tulung / "utama/build/main.py"

def relative_to_assets_us(path: str) -> Path:
    return ASSETS_PATH_us / Path(path)
    
def on_main():
    window.destroy()
    subprocess.run(["python", path_to_main])
def on_kret():
    window.destroy()
    subprocess.run(["python", path_to_kret])

window = Tk()

window_width = 1280
window_height = 720
window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets_us("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    68.0,
    image=image_image_1
)

button_main = PhotoImage(
    file=relative_to_assets_us("button_1.png"))
button_1 = Button(
    image=button_main,
    borderwidth=0,
    highlightthickness=0,
    command=on_main,
    relief="flat",
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
button_1.place(
    x=519.0,
    y=13.0,
    width=241.0,
    height=89.0
)

# button_image_2 = PhotoImage(
#     file=relative_to_assets_us("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_2 clicked"),
#     relief="flat",
#     bg="#CBD5C0",
#     activebackground="#CBD5C0"
# )
# button_2.place(
#     x=230.0,
#     y=29.0,
#     width=217.0,
#     height=73.0
# )

button_kret = PhotoImage(
    file=relative_to_assets_us("button_3.png"))
button_3 = Button(
    image=button_kret,
    borderwidth=0,
    highlightthickness=0,
    command=on_kret,
    relief="flat",
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
button_3.place(
    x=230.0,
    y=29.0,
    width=217.0,
    height=73.0
)

button_us = PhotoImage(
    file=relative_to_assets_us("button_4.png"))
button_4 = Button(
    image=button_us,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
button_4.place(
    x=832.0,
    y=29.0,
    width=217.0,
    height=73.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets_us("image_2.png"))
image_2 = canvas.create_image(
    363.0,
    430.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets_us("image_3.png"))
image_3 = canvas.create_image(
    975.0,
    441.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
