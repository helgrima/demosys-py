from .shaders import shaders
from .textures import textures
from .tracks import tracks
from .scenes import scenes


def load():
    scenes.load()
    shaders.load()
    textures.load()
    tracks.load()


def count():
    return shaders.count + textures.count
