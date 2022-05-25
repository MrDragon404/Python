import time
import timeit

from ursina import *
import random as r


app = Ursina()
Sky(
  texture="Y"
)
camera.orthographic = True
camera.fov = 20



bird = Animation("img",
                collider="box",
                scale=(2, 2, 2),
                x=-8)
def input(key):
    if key =="escape":
        quit()

    if key == "space":
        bird.y += 2

def update():
    bird.y -= 4*time.dt

    for p in pipes:
        p.x -= 4 * time.dt

    touch = bird.intersects()
    if touch.hit or bird.y < - 10:
        time.sleep(2)
        quit()


pipes = []

pipe = Entity(model="quad",
              color=color.green,
              position=(20, 10),
              scale=(3, 15, 1),
              collider="box"
              )

def newPipe():
    y = r.randint(4, 12)
    up = duplicate(pipe, y=y)
    down = duplicate(pipe, y=y-22)
    pipes.extend((up, down))
    invoke(newPipe, delay=5)







newPipe()





app.run()