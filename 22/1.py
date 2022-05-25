from ursina import *
from ursina.prefabs.first_person_controller \
      import FirstPersonController

app = Ursina()
Sky(
    texture="The"
)

player = FirstPersonController()
window.fullscreen = True

boxes = []

for i in range(50):
    for k in range(50):
        box = Button(
            position=(i, 0, k),
            color=color.white,
            hightlight_color=color.white66,
            model="cube",
            parent=scene,
            texture=load_texture("Snak")
        )
        boxes.append(box)

def input(key):
    if key == "escape":
        quit()


    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "right mouse down":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("metall")
                )
                boxes.append(newBox)
            if key == "1":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("Fair")
                )
                boxes.append(newBox)
            if key == "2":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("GG")
                )
                boxes.append(newBox)
            if key == "3":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("FW")
                )
                boxes.append(newBox)
            if key == "4":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("JO")
                )
                boxes.append(newBox)
            if key == "5":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("QO")
                )
                boxes.append(newBox)
            if key == "6":
                newBox = Button(
                    position=box.position + mouse.normal,
                    color=color.white,
                    model="cube",
                    hightlight_color=color.white,
                    parent=scene,
                    texture=load_texture("fff")
                )
                boxes.append(newBox)


app.run()