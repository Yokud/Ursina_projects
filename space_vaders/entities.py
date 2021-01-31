from ursina import *


class Spaceship(Sprite):
    def __init__(self, texture=None, shot_speed=0.5, move_speed=1, scale=.125):
        super().__init__(scale=scale, texture=texture, collider='box',
                         collision=True)
        self.score = 0
        self.shot_speed = shot_speed
        self.move_speed = move_speed
        self.position = Vec2(0, -2 * window.aspect_ratio)
        self.text_score = Text(text="Score: " + str(self.score), background=True,
                               x=-0.85, y=-0.45, z=-1)
        self.floor = Sprite(color=color.green, scale_x=window.fullscreen_size[0] / 100, scale_y=0.2,
                            position=Vec2(0, -2.3 * window.aspect_ratio), collider='box', collision=True, visible=False)
        
    def update(self):
        self.x += held_keys['d'] * self.move_speed * time.dt if self.x < 6.75 else 0
        self.x -= held_keys['a'] * self.move_speed * time.dt if self.x > -6.75 else 0

        player_hit_info = self.intersects()
        floor_hit_info = self.floor.intersects()

        if player_hit_info.hit and type(player_hit_info.entity) is Enemy or\
                floor_hit_info.hit and type(floor_hit_info.entity) is Enemy:
            destroy(self)
            scene.clear()
            menu_bg = Sprite(parent=scene, z=10, scale=(16, 9), texture='data/void.jpg')
            menu_bg.scale *= 2
            self.menu()

    def input(self, key):
        if key == 'space':
            self.shot()

    def shot(self):
        Bullet(self, position=Vec2(self.x, self.y + 0.25))

    def menu(self):
        WindowPanel(
            title='You died',
            content=(
                Text("Score: " + str(self.score)),
                Button(text='Try again', color=color.azure, on_click=HotReloader(path='main.py').reload_code),
                Button(text='Exit', color=color.red, on_click=application.quit)
            ), lock_x=True, lock_y=True, lock_z=True
        )


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
            destroy(self, 0.01)
            self.player.score += 10
            self.player.text_score.text = "Score: " + str(self.player.score)
        

class Enemy(Sprite):
    def __init__(self, enemy_texture=None, move_speed=3,
                 start_position=Vec2(0, 2.5 * window.aspect_ratio)):
        super().__init__(texture=enemy_texture, scale_x=1, scale_y=1,
                         position=start_position, collider='box', collision=True)
        self.move_speed = move_speed

    def update(self):
        self.y -= self.move_speed * time.dt
