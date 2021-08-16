import tkinter as tk
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject


class Frame(GUIObject):

    def __init__(self, master, properties_dict):
        self._create_object_by_type(tk.Frame, master)
        self._set_properties_to_object(properties_dict)
