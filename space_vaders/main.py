from spaceship import Spaceship
from ursina import *

app = Ursina()

window.title = "Space Vaders"
#window.icon = "data/modular_ships.png"
window.borderless = False
window.exit_button.visible = False
window.cursor = False

bg = Entity(parent=scene, model='quad', z=10, scale=(16, 9),
            texture='data/space_bg.png')
bg.scale *= 2

player = Spaceship('data/modular_ships.png', move_speed=2)

app.run()
