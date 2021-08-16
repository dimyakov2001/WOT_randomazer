import tkinter as tk
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject


class Button(GUIObject):

    def __init__(self, master, properties_dict):
        self._create_object_by_type(tk.Button, master)
        self._set_properties_to_object(properties_dict)
