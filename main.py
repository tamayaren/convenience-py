from json import *

import pyautogui as gui
import tkinter as tk

from classes import window as core
config = load(open("./definitions/config.json"))

main_class = core.Window("Convenience", config['resolution']).create("Convenience")

print(main_class)
#
main_window = main_class.window
main_container = main_class.container

main_window.mainloop()



