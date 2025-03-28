from tkinter import *
import tkintermapview

root = Tk()
root.title('teste')

root.geometry('900x700')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)

#coordenadas
map_widget.set_position(39.81222, -7.99138)

#set a zoom
map_widget.set_zoom(7)

map_widget.pack()

root.mainloop()
