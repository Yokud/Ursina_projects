from ursina import *

class Spaceship(Sprite):
    def __init__(self, texture=None, shot_speed=0.5, move_speed=1, scale=.125):
        super().__init__(scale=scale, texture=texture, collider='box',
                         collision=True)
        self.score = 0
        self.shot_speed = shot_speed
        self.move_speed = move_speed
        self.position = Vec2(0, -2 * window.aspect_ratio)
        
    def update(self):
        self.x += held_keys['d'] * self.move_speed * time.dt if self.x < 6.75 else 0
        self.x -= held_keys['a'] * self.move_speed * time.dt if self.x > -6.75 else 0

    def input(self, key):
        if key == 'space':
            self.shot()

    def shot(self):
        Bullet(self, position=Vec2(self.x, self.y + 0.25))


class Bullet(Sprite):
    def __init__(self, player, move_speed=5, position=Vec2(0, 0)):
        super().__init__(color=color.orange, scale_x=.03, scale_y=.25,
                         position=position, collider='box', collision=True)
        self.move_speed = move_speed
        self.player = player

    def update(self):
        self.y += self.move_speed * time.dt

        hit_info = self.intersects()

        if self.y >= 2.5 * window.aspect_ratio:
            destroy(self)
        elif hit_info.hit and type(hit_info.entity) is Enemy:
            destroy(hit_info.entity)
            destroy(self, 0.1)
            self.player.score += 10
        

class Enemy(Sprite):
    def __init__(self, move_speed=3,
                 start_position=Vec2(0, 2 * window.aspect_ratio)):
        super().__init__(color=color.red, scale_x=.5, scale_y=.5,
                         position=start_position, collider='box', collision=True)
        self.move_speed = move_speed


    def update(self):
        self.y -= self.move_speed * time.dt

        hit_info = self.intersects()

        if self.y <= -2 * window.aspect_ratio:
            destroy(self)
            print("You died")
            #application.pause()
            
