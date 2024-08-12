import subprocess
from tkinter import Tk, Frame, Canvas, Scrollbar, Button, PhotoImage, NW
from pathlib import Path
from PIL import Image, ImageTk


def read_kreasi_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.readlines()
            titles = [line.strip() for line in content]
            return titles
    except FileNotFoundError:
        print(f"File not found: {'listKreasi.txt'}")
        return []
    
def clear_listKreasi():
    file_path = "listKreasi.txt"
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)  # This line truncates the file, effectively clearing its content
        print(f"Successfully cleared {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while clearing {file_path}: {e}")



#Berhasil coyyyyyy -rul
# def load_images(judul_now, images_path, container, window):
#     y_position = 0 
#     loaded_images = {}

#     # Create a vertical scrollbar for the container
#     scrollbar = Scrollbar(container, orient="vertical", command=container.yview)
#     scrollbar.pack(side="right", fill="y")

#     # Configure the container to use the scrollbar
#     container.config(yscrollcommand=scrollbar.set)

#     for judul in judul_now:
#         file_name = judul + '.png'
#         image_path = images_path / file_name
#         if image_path.is_file():
#             loaded_images[judul] = PhotoImage(file=image_path)
#             container.create_image(360, y_position, image=loaded_images[judul], anchor=NW)
#             y_position += loaded_images[judul].height() + 10
#         else:
#             print(f"File tidak ditemukan: {image_path}")

#     window.update_idletasks()
#     return loaded_images


def load_images(judul_now, images_path, container, window):
    y_position_left = 0
    y_position_right = 0
    loaded_images = {}

    # Create a vertical scrollbar for the container
    scrollbar = Scrollbar(container, orient="vertical", command=container.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the container to use the scrollbar
    container.config(yscrollcommand=scrollbar.set)

    # Determine half of the total number of images
    half_index = len(judul_now) // 2

    for index, judul in enumerate(judul_now):
        file_name = judul + '.png'
        image_path = images_path / file_name
        if image_path.is_file():
            loaded_images[judul] = PhotoImage(file=image_path)
            
            # Determine if the image should be on the left or right
            if index < half_index:
                # Place on the left
                container.create_image(180, y_position_left, image=loaded_images[judul], anchor=NW)
                y_position_left += loaded_images[judul].height() + 10
            else:
                # Place on the right
                container.create_image(830, y_position_right, image=loaded_images[judul], anchor=NW)
                y_position_right += loaded_images[judul].height() + 10
        else:
            print(f"File tidak ditemukan: {image_path}")

    # Update the container size based on the bounding box
    container.update_idletasks()
    bbox = container.bbox("all")
    container.config(scrollregion=bbox)
    container.config(width=bbox[2] - bbox[0], height=bbox[3] - bbox[1])

    window.update_idletasks()
    return loaded_images


def on_main():
    clear_listKreasi()
    window.destroy()
    subprocess.run(["python", path_to_main])

def on_us():
    clear_listKreasi()
    window.destroy()
    subprocess.run(["python", path_to_us])

def on_kret():
    clear_listKreasi()
    window.destroy()
    subprocess.run(["python", path_to_kret])

root_path = Path(__file__).parent.parent.parent
ASSETS_PATH = root_path / "produk"
KREASI_JUDUL_FILE = root_path / "listKreasi.txt"
judul_now = read_kreasi_file(KREASI_JUDUL_FILE)
BASE_PATH = Path(__file__).parent
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_us = BASE_PATH / "assets/frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH_us / Path(path)

tulung = Path(__file__).parent.parent.parent
path_to_us = tulung / "us/build/us.py"
path_to_main = tulung / "utama/build/main.py"
path_to_kret = tulung / "kreate/build/kret.py"

window = Tk()
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

top_frame = Frame(window, bg="#FFFFFF", height=200)
top_frame.pack(side="top", fill="x")
top_frame.pack_propagate(False)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))

# image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = Image.open(relative_to_assets("image_2.png"))
image_image_2 = ImageTk.PhotoImage(image_2.resize((300, 50), Image.ANTIALIAS))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))

image_1 = Button(top_frame, image=image_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("image_1 clicked"), relief="flat")
image_2 = Button(top_frame, image=image_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("image_2 clicked"), relief="flat",bg="#FFFFFF", activebackground="#FFFFFF")

button_1 = Button(top_frame, image=button_image_1, borderwidth=0, highlightthickness=0, command=on_main, relief="flat",bg="#CBD5C0", activebackground="#CBD5C0")
button_2 = Button(top_frame, image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat",bg="#CBD5C0", activebackground="#CBD5C0")
button_3 = Button(top_frame, image=button_image_3, borderwidth=0, highlightthickness=0,command=on_kret, relief="flat",bg="#CBD5C0", activebackground="#CBD5C0")
button_4 = Button(top_frame, image=button_image_4, borderwidth=0, highlightthickness=0, command=on_us, relief="flat",bg="#CBD5C0", activebackground="#CBD5C0")

image_1.place(x=640, y=68, anchor="center")
image_2.place(x=640, y=174, anchor="center")
button_1.place(x=519, y=13, width=241, height=89)
button_2.place(x=230, y=29, width=217, height=73)
button_3.place(x=230, y=29, width=217, height=73)
button_4.place(x=832, y=29, width=217, height=73)


bottom_frame = Canvas(window, bg="#FFFFFF", scrollregion=(0, 0, 1000, 1000))
bottom_frame.pack(side="bottom", fill="both", expand=True)

##TEMPAT SCROLL
# scrollbar = Scrollbar(window, orient="vertical", command=bottom_frame.yview)
# scrollbar.pack(side="right", fill="y")
# bottom_frame.config(yscrollcommand=scrollbar.set)

images = load_images(judul_now, ASSETS_PATH, bottom_frame, window)

window.resizable(False, False)
window.mainloop()

# sekedar saran, inget minum jus aer
# makasih karan atas sarannya