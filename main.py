from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
block_picked = grass_texture


def update():
    global block_picked
    if held_keys['1']:
        block_picked = grass_texture

    if held_keys['2']:
        block_picked = stone_texture

    if held_keys['3']:
        block_picked = brick_texture

    if held_keys['4']:
        block_picked = dirt_texture


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.25,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=block_picked)

            if key == 'right mouse down':
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )


for z in range(20):
    for x in range(20):
        voxel = Voxel((x, 0, z))

player = FirstPersonController()
sky = Sky()

app.run()
