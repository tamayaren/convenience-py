from tkinter import *

class ComponentPackager:
    def __init__(self, container):
        self.container = container
        self.components = {}

    def add(self, name, component):
        self.components[name] = component