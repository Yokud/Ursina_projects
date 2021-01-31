from entities import Spaceship, Enemy
from ursina import *
import random as rnd
import os


def spawn_enemies(enemy_textures):
    spawner = Sequence(
        Wait(1),
        # Func(print, "spawned"),
        Enemy(enemy_texture=enemy_textures[rnd.randrange(len(enemy_textures))], move_speed=1,
              start_position=Vec2(rnd.randrange(-5, 5), 2 * window.aspect_ratio)),
        loop=True,
        auto_destroy=False,
    )
    spawner.start()


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

spawn_enemies(alien_textures)

app.run()
