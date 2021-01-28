import math
import random as rnd
from ursina import *
from Boid import Boid
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


window.borderless = False
app = Ursina()
window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

ground = Entity(
    model='cube',
    color=color.olive.tint(-.4),
    z=-.1,
    y=-1,
    origin_y=.5,
    scale=(1000, 100, 10),
    collider='box',
    ignore=True,
)

player = PlatformerController2d()
player.x = 1
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))
player.collider = 'box'

boids = []
for i in range(20):
    boids.append(Boid(maxspeed=1, position=(rnd.uniform(-15, 15), rnd.uniform(1, 10), 0), maxforce=0.01))


def update():
    for boid in boids:
        curpos = Vec3(player.position[0], player.position[1] + 1, 0)
        boid.seek(curpos)
        boid.separate(boids)
        boid.update()
        boid.rotation_z = math.atan2(boid.velocity[1], boid.velocity[0]) * 180 / math.pi


input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')

app.run()
