from ursina import *
from ursina.prefabs.grid_editor import PixelEditor
from PIL import Image

point = Ursina()
window.title = "Paint"

canvas = Texture(Image.new(mode="RGBA", size=(32, 32)))
PixelEditor(texture=canvas)

point.run()