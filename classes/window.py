from tkinter import *
from json import *

config = load(open("./definitions/config.json"))

class Window:
    def __init__(self, name, resolution):
        self.name = name
        self.defaultResolution = resolution

    def create(self, defTitle):
        self.name = defTitle

        self.window = Tk()
        self.window.title(self.name)
        self.window.geometry(self.defaultResolution)

        self.container = Frame(self.window)
        self.container.pack(fill= BOTH, expand= True, padx=config['inner-window']['margin']['x'], pady=config['inner-window']['margin']['y'])

        return self