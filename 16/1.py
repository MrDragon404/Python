from ursina import *

from ursina.prefabs.first_person_controller \
    import FirstPersonController

app = Ursina()
Sky()
player = FirstPersonController()
window.fullscreen = True

arm = Entity(
    parent=camera.ui,
    model="cube",
    color=color.red,
    position=(0.75, -0.6),
    rotation=(150,-10.6),
    scale=(0.2, 0.2, 1.5)
)

boxes = []
for i in range(30):
    for j in range(30):
        box = Button(
            position=(i, 0, j),
            color=color.gray,
            highlight_color=color.white,
            model="cube",
            texture=load_texture("grow"),
            parent=scene
        )
        boxes.append(box)

def input(key):
    if held_keys["escape"]:
        quit()
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.olive,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("wood"),
                    parent=scene
                )
                boxes.append(newBox)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

            if held_keys["1"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("blon"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["2"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("metal"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["3"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("spacce"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["4"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("sky"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["5"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("sss"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["6"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("aaa"),
                    parent=scene
                )
                boxes.append(newBox)

            if held_keys["7"]:
                newBox = Button(
                    position=box.position+mouse.normal,
                    color=color.gray,
                    highlight_color=color.white50,
                    model="cube",
                    texture=load_texture("3d"),
                    parent=scene
                )
                boxes.append(newBox)
app.run() 
