from entities import Spaceship, Enemy
from ursina import *
import random

app = Ursina()

window.title = "Space Vaders"
#window.icon = "data/modular_ships.png"
window.borderless = False
window.exit_button.visible = False
window.cursor = False

bg = Entity(parent=scene, model='quad', z=10, scale=(16, 9),
            texture='data/space_bg.png')
bg.scale *= 2

player = Spaceship('data/modular_ships.png', move_speed=4)

invoke(Enemy, move_speed=1,
       start_position=Vec2(random.randrange(-5, 5), 2 * window.aspect_ratio),
       delay=0.5)
invoke(Enemy, move_speed=1,
       start_position=Vec2(random.randrange(-5, 5), 2 * window.aspect_ratio),
       delay=0.5)
invoke(Enemy, move_speed=1,
       start_position=Vec2(random.randrange(-5, 5), 2 * window.aspect_ratio),
       delay=0.5)
invoke(Enemy, move_speed=1,
       start_position=Vec2(random.randrange(-5, 5), 2 * window.aspect_ratio),
       delay=0.5)
invoke(Enemy, move_speed=1,
       start_position=Vec2(random.randrange(-5, 5), 2 * window.aspect_ratio),
       delay=0.5)

app.run()
