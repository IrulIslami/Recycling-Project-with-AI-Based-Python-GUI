from pathlib import Path
import subprocess
import pandas as pd

from tkinter import Tk, Canvas, Button, PhotoImage, Checkbutton, IntVar

# mencari path utama
BASE_PATH = Path(__file__).parent
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_us = BASE_PATH / "assets/frame0"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH_us / Path(path)

# mencari path untuk button navigasi
tulung = Path(__file__).parent.parent.parent
path_to_us = tulung / "us/build/us.py"
path_to_main = tulung / "utama/build/main.py"
path_to_hasil = tulung / "hasil/build/hasil.py"

def on_us():
    window.destroy()
    subprocess.run(["python", path_to_us]) 
    
def on_hasil():
    read_checkbox_and_search()
    window.destroy()
    subprocess.run(["python", path_to_hasil]) 
    

def on_main():
    window.destroy()
    subprocess.run(["python", path_to_main])
def on_done():
    save_checkbox_states()
    checkbox_states = read_checkbox()
    print(checkbox_states)
    


def save_checkbox_states():
    checkbox_states = {
        "botol plastik": checkbox_value_bplas.get(),
        "kotak susu": checkbox_value_taksu.get(),
        "kain": checkbox_value_Kain.get(),
        "botol kaca": checkbox_value_boca.get(),
        "kertas": checkbox_value_kertas.get(),
        "kaleng": checkbox_value_kaleng.get(),
        "koran": checkbox_value_koran.get(),
        "kardus": checkbox_value_kardus.get(),
        "karet": checkbox_value_karet.get(),
        "sedotan": checkbox_value_sedotan.get(),
    }
    
    with open('checkbox_states.txt', 'w') as file:
        for item, state in checkbox_states.items():
            file.write(f"{item} : {'true' if state == 1 else 'false'}\n")
            

            
def read_checkbox():
    checkbox_states = {}
    try:
        with open('checkbox_states.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                item, state_str = line.strip().split(' : ')
                checkbox_states[item] = state_str.lower() == 'true'
    except FileNotFoundError:
        print("Checkbox states file not found. Returning empty dictionary.")
    
    # Filter items with value 'true'
    checkbox_states_true = {item: state for item, state in checkbox_states.items() if state}
    
    return checkbox_states_true

def write_for_title(judul_list):
    existing_titles = set()
    try:
        with open('listKreasi.txt', 'r') as file:
            existing_titles = set(file.read().splitlines())
    except FileNotFoundError:
        pass
    all_titles = existing_titles.union(set(judul_list))
    with open('listKreasi.txt', 'w') as file:
        for title in all_titles:
            file.write(f"{title}\n")    
def cari_kreasi_sampah(bahan_list):
    df_sampah = pd.read_csv(tulung / 'DatasetSAMPAH.csv', delimiter=',')


    hasil_pencarian = df_sampah.copy()
    judul_kreasi_list = []  # List untuk menyimpan judul kreasi
    
    for bahan in bahan_list:
        hasil_pencarian = hasil_pencarian[hasil_pencarian['Bahan'].str.contains(bahan, case=False, na=False, regex=False)]

    if not hasil_pencarian.empty:
        print("Informasi untuk kreasi berdasarkan bahan:")
        for _, row in hasil_pencarian.iterrows():
            judul_kreasi = row['Nama']
            judul_kreasi_list.append(judul_kreasi)  # Menambahkan judul ke dalam list
            
            print(f"Judul Kreasi: {judul_kreasi}")
            print(f"Bahan: {row['Bahan']}")
            print("Langkah-langkah:")
            steps_list = row.get('Step', '').split(' - ')
            for i, step in enumerate(steps_list, start=1):
                print(f"{i}. {step.strip()}")
            print("------------------------")
        # Menulis judul kreasi ke dalam file
        write_for_title(judul_kreasi_list)

    else:
        print(f"Tidak ditemukan kreasi untuk bahan: {', '.join(bahan_list)}")
    


def read_checkbox_and_search():
    save_checkbox_states()
    checkbox_states = read_checkbox()
    print(checkbox_states)
    # print(len(checkbox_states))
    
    # Filter items with value 'true'
    checkbox_states_true = {item: state for item, state in checkbox_states.items() if state}

    if not checkbox_states_true:
        print("No checked items. Exiting.")
        return

    bahan_list = list(checkbox_states_true.keys())
    if len(bahan_list) > 1:
        for bahan in bahan_list:
            print(f"Searching for recipes based on checked item: {bahan}")
            cari_kreasi_sampah([bahan])
        
    print(" ")
        
    print(f"Searching for recipes based on checked items: {', '.join(bahan_list)}")
    cari_kreasi_sampah(bahan_list)

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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    65.0,
    image=image_image_1
)

button_main = PhotoImage(
    file=relative_to_assets("button_1.png"))
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
    y=16.0,
    width=241.0,
    height=89.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
button_3.place(
    x=230.0,
    y=32.0,
    width=217.0,
    height=73.0
)

button_us = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_us,
    borderwidth=0,
    highlightthickness=0,
    command=on_us,
    relief="flat",
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
button_4.place(
    x=832.0,
    y=32.0,
    width=217.0,
    height=73.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    184.0,
    313.0,
    image=image_image_2
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=on_hasil,
    relief="flat"
)
button_5.place(
    x=1097.0,
    y=648.0,
    width=163.0,
    height=49.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    145.0,
    160.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    419.0,
    317.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    668.0,
    298.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    874.0,
    298.0,
    image=image_image_6
)


image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1081.0,
    298.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    184.0,
    537.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    421.0,
    523.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    668.0,
    517.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    875.0,
    517.0000076293945,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1081.0,
    508.0,
    image=image_image_12
)
##
## menampilkan check box
##
checkbox_value_sedotan = IntVar(value=0)
checkbox_sedotan = Checkbutton(
    window,
    text="sedotan",
    variable=checkbox_value_sedotan,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_sedotan.place(x=1046, y=599)
##
##
checkbox_value_karet = IntVar(value=0)
checkbox_karet = Checkbutton(
    window,
    text="karet",
    variable=checkbox_value_karet,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_karet.place(x=836, y=599)
##
##
checkbox_value_kardus = IntVar(value=0)
checkbox_kardus = Checkbutton(
    window,
    text="kardus",
    variable=checkbox_value_kardus,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_kardus.place(x=626, y=599)
##
##
checkbox_value_koran = IntVar(value=0)
checkbox_koran = Checkbutton(
    window,
    text="koran",
    variable=checkbox_value_koran,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_koran.place(x=377, y=599)
##
##
checkbox_value_kaleng = IntVar(value=0)
checkbox_kaleng = Checkbutton(
    window,
    text="kaleng",
    variable=checkbox_value_kaleng,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_kaleng.place(x=142, y=599)
##
##
checkbox_value_kertas = IntVar(value=0)
checkbox_kertas = Checkbutton(
    window,
    text="kertas",
    variable=checkbox_value_kertas,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_kertas.place(x=1046, y=399)
##
##
checkbox_value_boca = IntVar(value=0)
checkbox_boca = Checkbutton(
    window,
    text="botol kaca",
    variable=checkbox_value_boca,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_boca.place(x=836, y=399)
##
##
checkbox_value_Kain = IntVar(value=0)
checkbox_Kain = Checkbutton(
    window,
    text="Kain",
    variable=checkbox_value_Kain,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_Kain.place(x=626, y=399)
##
##
checkbox_value_taksu = IntVar(value=0)
checkbox_taksu = Checkbutton(
    window,
    text="kotak susu",
    variable=checkbox_value_taksu,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_taksu.place(x=377, y=399)
##
##
checkbox_value_bplas = IntVar(value=0)
checkbox_bplas = Checkbutton(
    window,
    text="botol plastik",
    variable=checkbox_value_bplas,  
    onvalue=1,  
    offvalue=0,   
    bg="#CBD5C0",
    activebackground="#CBD5C0"
)
checkbox_bplas.place(x=137, y=399)
##
window.resizable(False, False)
window.mainloop()
# save_checkbox_states()