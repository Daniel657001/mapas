from tkinter import *
import tkintermapview
import os
from PIL import Image, ImageTk

root = Tk()
root.title('teste')

root.geometry('900x700')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)

# load images
current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
braganca_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "foto_pro_projeto.jpg")).resize((40, 40)))

bragranca_imagem = map_widget.set_marker(41.8060, -6.7567, text="brangança", icon=braganca_image, command=marker_callback)

 #coordenadas
map_widget.set_position(39.81222, -7.99138)

#set a zoom
map_widget.set_zoom(7)

braganca_marker = map_widget.set_marker(41.8060, -6.7567)

map_widget.pack()

root.mainloop()
