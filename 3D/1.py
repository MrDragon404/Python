# Импортировать ursina
from ursina import *
# Импорт 3d камера
from ursina.prefabs.first_person_controller import FirstPersonController

# Создать экземпляр класса Ursina
app = Ursina()
# Создаем класс Voxel
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.green,
            highlight_color=color.white
        )

    def input(self, key):
        if(self.hovered):
            if(key == "left mouse down"):
                voxel = Voxel(position=self.position + mouse.normal)
                voxel.color = color.orange

            if held_keys["1"]:
                voxel = Voxel(position=self.position + mouse.normal)
                voxel.color = color.white66

            if held_keys["2"]:
                voxel = Voxel(position=self.position + mouse.normal)
                voxel.color = color.black50


            if(key == "right mouse down"):
                destroy(self)



# Создать методы построить и разрушить
# Построить 30 x 30 voxel площадку

for x in range(30):
    for z in range(30):
        voxel = Voxel(position=(x,0,z))


# Создать игрока
player = FirstPersonController()

app.run()

