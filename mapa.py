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
braganca_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "foto_pro_projeto.jpg")).resize((40, 40)))

# Atualizar as coordenadas para Bragança
bragranca_imagem = map_widget.set_marker(41.9925, -6.9545, text="Bragança", icon=braganca_image)
map_widget.set_zoom(8)

# Porto
porto_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "porto.jpg")).resize((40, 40)))
porto_imagem = map_widget.set_marker(41.15, -8.61024, text="Porto", icon=porto_image)

# Lisboa
lisboa_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "lisboa.jpg")).resize((40, 40)))
lisboa_imagem = map_widget.set_marker(38.7071, -9.13549 , text="Lisboa", icon=lisboa_image)

# Leiria
leiria_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "leiria.jpg")).resize((40, 40)))
leiria_imagem = map_widget.set_marker(39.7443, -8.80725 , text="Leiria", icon=leiria_image)

# Beja
beja_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "beja.jpg")).resize((40, 40)))
beja_imagem = map_widget.set_marker(38.0156, -7.86523, text="Beja", icon=beja_image)

# Covilhã
covilha_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "covilha.jpg")).resize((40, 40)))
covilha_imagem = map_widget.set_marker(40.2826, -7.50326, text="Covilhã", icon=covilha_image)

# Ponte de Sor
ponte_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "imagens", "ponte.jpg")).resize((40, 40)))
ponte_imagem = map_widget.set_marker(39.2478, -8.00964 , text="Ponte de Sor", icon=ponte_image)

def polygon_click(polygon):
    print(f"polygon clicked - text: {polygon.name}")

# Coordenadas do perímetro do distrito de Bragança
braganca_polygon_coordinates = [
    (41.8057, -6.7572),  # Bragança (ponto central)
    (41.9500, -6.7500),  # Norte, Parque Natural de Montesinho
    (42.0000, -6.7000),  # Norte, perto de Rio de Onor
    (42.0500, -6.7500),  # Norte, fronteira com Espanha
    (42.0800, -6.8500),  # Noroeste, Vinhais, fronteira
    (42.1000, -6.9500),  # Noroeste, limite superior
    (42.0800, -7.0500),  # Noroeste, transição para Espanha
    (42.0500, -7.1500),  # Noroeste, Serra da Coroa
    (42.0000, -7.2500),  # Oeste, perto de Carrazeda de Ansiães
    (41.9500, -7.3500),  # Oeste, limite com Vila Real
    (41.9000, -7.4000),  # Oeste, Serra de Bornes
    (41.8500, -7.4500),  # Sudoeste, perto de Alfândega da Fé
    (41.7500, -7.5000),  # Sudoeste, limite com Guarda
    (41.6500, -7.4500),  # Sul, transição para Macedo de Cavaleiros
    (41.6000, -7.4000),  # Sul, limite inferior com Guarda
    (41.5500, -7.3000),  # Sul, perto de Vila Flor
    (41.5000, -7.2000),  # Sul, Torre de Moncorvo
    (41.4500, -7.1000),  # Sul, transição para Mogadouro
    (41.4000, -7.0000),  # Sul, limite com o Douro
    (41.4200, -6.9000),  # Sudeste, Mogadouro
    (41.4800, -6.8000),  # Sudeste, interior
    (41.5500, -6.7000),  # Sudeste, Parque Natural do Douro Internacional
    (41.6000, -6.6000),  # Sudeste, Miranda do Douro
    (41.6500, -6.5500),  # Leste, fronteira com Espanha
    (41.7000, -6.5000),  # Leste, perto de Sendim
    (41.8000, -6.4500),  # Leste, limite oriental
    (41.8500, -6.5000),  # Nordeste, transição para Vinhais
    (41.9000, -6.6000),  # Nordeste, interior
    (41.9500, -6.6500),  # Nordeste, Montesinho
    (41.8057, -6.7572)   # Fechando o polígono em Bragança
]

# Criar o polígono com as coordenadas do perímetro do distrito de Bragança
polygon_1 = map_widget.set_polygon(braganca_polygon_coordinates,
                                   command=polygon_click,
                                   name="Perímetro de Bragança")

# Atualizar coordenadas para a região de Bragança
map_widget.set_position(41.9925, -6.9545)

# Definir zoom
map_widget.set_zoom(7)

map_widget.pack()

root.mainloop()
