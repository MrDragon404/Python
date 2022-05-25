from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

ground = Entity(model="plane",
                texture="heightmap_1",
                collider="mesh",
                scale=(10, 1, 10)
                )

window.fullscreen= True

for i in range(150):
    randomNumber = random.uniform(-2, 2)
    block = Entity(model="cube",
                   color=color.random_color(),
                   collider="box",
                   texture="white_block",
                   position=(randomNumber, i+1, 3+i*5),
                   scale=(3,1,3)
                   )

def input(key):
    if key == "escape":
        quit()

player = FirstPersonController()
Sky()
app.run()

