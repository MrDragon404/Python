
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()
Sky(
    texture='As'
)

ground = Entity(
    model='plane',
    collider='mesh',
    scale=(1000, 1, 1000),
    texture='sky'
)
player = FirstPersonController(collider='box')
player.speed=100


window.fullscreen = True
blocks = []
directions = []

for n in range(60):
    randomNumber = uniform(-2, 2)
    block = Entity(
        model='cube',
        texture='fff',
        scale=(3, 0.5, 3),
        collider='box',
        position=(randomNumber, n, 5*n+5)
    )
    blocks.append(block)
    if randomNumber < 0:
        directions.append(1)
    else:
        directions.append(-1)

def input(key):
    if key == 'escape':
        quit()

def update():
    i = 0
    for b in blocks:
        b.x -= directions[i] * time.dt
        if abs(b.x) > 5:
            directions[i] *= -1
        if b.intersects().hit:
            player.x -= directions[i] * time.dt
        i += 1


app.run()
