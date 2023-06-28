import os
from PIL import ImageTk, Image
from tkinter import Label
from customtkinter import CTk, CTkFrame, CTkButton

# Directorio de imágenes
carpeta_p = os.path.dirname(__file__)
carpeta_img = os.path.join(carpeta_p, "imgs")

# Ventana principal
root = CTk()
root.title("Inicio")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)
width_root = 900
height_root = 600

# Tamaño de la pantalla
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Coordenadas
c_x = int((width / 2) - (width_root / 2)) + 100
c_y = int((height / 2) - (height_root / 2))

# Tamaño de root
root.geometry("{}x{}+{}+{}".format(width_root, height_root, c_x, c_y))

# Colores
c_amarillob = "#FFC36C"
c_amarilloL = "#FEB142"
c_vinotinto = "#641717"
c_vinotintoO = "#541414"
c_blanco = "#F0F0EF"
c_gris = "#dededc"
c_azulM = "#0C2737"
c_azulO = "#0b1f2b"

# Frame del menú
menu_frame = CTkFrame(root, fg_color=c_azulM,
                      bg_color=c_azulM, width=900, height=70)
menu_frame.place(x=0, y=0)

# Frame del inicio
win_menu = CTkFrame(root, fg_color=c_amarilloL,
                    bg_color=c_amarilloL, width=900, height=530)
win_menu.place(x=0, y=70)

# Imagen de fondo
inicio = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_img, "inicio.jpg")).resize(size=(1400, 900)))
show_inicio = Label(win_menu, image=inicio, border=0)
show_inicio.place(bordermode="inside")

# Función para el inicio


def botones_inicio():
    bt_registrar = CTkButton(win_menu, text="Registrar", font=('Lovelo Black', 45), fg_color=c_blanco,
                             hover_color=c_gris, bg_color=c_blanco, text_color=c_amarilloL, width=370, height=210)
    bt_registrar.place(x=30, y=25)
    bt_actualizar = CTkButton(win_menu, text="Actualizar", font=('Lovelo Black', 45), fg_color=c_blanco,
                              hover_color=c_gris, bg_color=c_blanco, text_color=c_amarilloL, width=370, height=210)
    bt_actualizar.place(x=500, y=25)
    bt_eliminar = CTkButton(win_menu, text="Eliminar", font=('Lovelo Black', 45), fg_color=c_vinotinto,
                            hover_color=c_vinotintoO, bg_color=c_vinotinto, text_color=c_blanco, width=370, height=210)
    bt_eliminar.place(x=30, y=295)
    bt_pago = CTkButton(win_menu, text="Pago", font=('Lovelo Black', 45), fg_color=c_blanco, hover_color=c_gris,
                        bg_color=c_blanco, text_color=c_vinotinto, width=370, height=210)
    bt_pago.place(x=500, y=295)


# Botones del menú
bt_inicio = CTkButton(menu_frame, text="inicio", font=('Advent Pro Bold', 17), fg_color=c_azulM, bg_color=c_azulM,
                      hover_color=c_azulO, border_color=c_azulM, corner_radius=24, border_width=2, width=30, height=45,
                      command=botones_inicio)
bt_inicio.place(x=15, y=13)

bt_consul = CTkButton(menu_frame, text="consultas", font=('Advent Pro Bold', 17), fg_color=c_amarillob,
                      bg_color=c_azulM, hover_color=c_amarilloL, border_color=c_amarillob, text_color=c_vinotinto,
                      corner_radius=24, border_width=2, width=30, height=45)
bt_consul.place(x=110, y=13)

bt_salir = CTkButton(menu_frame, text="salir", font=('Advent Pro Bold', 17), fg_color=c_amarillob, bg_color=c_azulM,
                     hover_color=c_amarilloL, border_color=c_amarillob, text_color=c_vinotinto, corner_radius=24,
                     border_width=2, width=30, height=45)
bt_salir.place(x=240, y=13)
