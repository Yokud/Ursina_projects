from entities import Spaceship, Enemy, Spawner
from ursina import *
import random as rnd
import os


app = Ursina()

window.title = "Space Vaders"
window.icon = "data/SV_ico.ico"
window.borderless = False
window.exit_button.visible = False
window.cursor = False

bg = Entity(parent=scene, model='quad', z=10, scale=(16, 9),
            texture='data/space_bg.png')
bg.scale *= 2

player = Spaceship('data/modular_ships.png', move_speed=4)
alien_textures = os.listdir('data/enemies')

Spawner(alien_textures)

app.run()
