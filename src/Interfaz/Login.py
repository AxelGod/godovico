import os
import tkinter as tk
from PIL import ImageTk, Image
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry
import src.Procesado.confirmarpass as confirmacion

c_negro = '#010101'
c_rojo = '#8A1111'
c_amarillo = '#FEB142'
c_azult = '#0C2737'
c_azule = '#556A73'
c_blanco = '#F0F0EF'
width_root = 600
height_root = 500

class Login(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, fg_color=c_blanco, bg_color=c_blanco, corner_radius=24)
        self.grid(column=0, row=0, sticky='news', padx=80, pady=80)
        self.widgets()
        self.place_widgets()

    def widgets(self):
        self.title_sub1 = CTkLabel(self, text="INICIO", font=('Lovelo Black', 32), width=80, height=20, text_color=c_azult)
        self.user_label = CTkLabel(self, text="Usuario", width=20, height=10, font=('Advent Pro Bold', 18), text_color=c_rojo)
        self.user_entry = CTkEntry(self, placeholder_text="Ej: Rana...", font=('Advent Pro Thin', 14.7), placeholder_text_color=(c_blanco, c_azult), border_color=c_azule, fg_color=c_azule, bg_color=c_blanco, width=220, height=40, corner_radius=24)
        self.password_label = CTkLabel(self, text="Contraseña", width=20, height=10, font=('Advent Pro Bold', 18), text_color=c_rojo)
        self.password_entry = CTkEntry(self, placeholder_text="Ej: 123kfvfkdl", font=('Advent Pro Thin', 14.7), placeholder_text_color=(c_blanco, c_azult), border_color=c_azule, fg_color=c_azule, bg_color=c_blanco, width=220, height=40, corner_radius=24)
        self.bt_load = CTkButton(self, text="Ingresar", font=('LeagueSpartan-Bold', 14), border_color=c_amarillo, bg_color=c_blanco, fg_color=c_blanco, hover_color=c_amarillo, corner_radius=24, border_width=2, height=40, text_color=c_azult, command=self.show_login_info)

    def place_widgets(self):
        self.title_sub1.grid(column=0, row=0, padx=20, pady=23)
        self.user_label.grid(columnspan=2, column=0, row=1, padx=50, pady=5)
        self.user_entry.grid(columnspan=2, row=2, sticky="news", padx=105, pady=4)
        self.password_label.grid(column=0, row=3, padx=50, pady=5)
        self.password_entry.grid(columnspan=2, row=4, sticky="news", padx=105, pady=4)
        self.bt_load.grid(column=0, row=8, padx=150, pady=10)

    def show_login_info(self):
        username = self.user_entry.get()
        password = self.password_entry.get()
        id=confirmacion.confir(username, password)
        if id:
            print(id)
        else:
            print("nonas")

root = tk.Tk()
root.config(bg=c_negro)
root.title("Inicio de Sesion")
root.resizable(False, False)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
c_x = int((width/2) - (width_root/2)) + 100
c_y = int((height/2) - (height_root/2))
root.geometry("{}x{}+{}+{}".format(width_root, height_root, c_x, c_y))
carpeta_p = os.path.dirname(__file__)
carpeta_img = os.path.join(carpeta_p, "imgs")
bg = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_img, "fondoo_o.jpg")))
show_bg = tk.Label(root, image=bg, border=0)
show_bg.place(bordermode="inside")
log = Login(master=root)

