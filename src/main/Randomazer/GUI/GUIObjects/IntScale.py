import tkinter as tk
from src.main.Randomazer.GUI.GUIObjects.Scale import Scale


class IntScale(Scale):

    def __init__(self, master, properties_dict):
        self._init_set_item_dict()
        self._create_object_by_type(tk.Scale, master)
        self._variable = tk.IntVar()
        self._object[self.GUI_OBJECT_VARIABLE_FIELD] = self._variable
        self._set_properties_to_object(properties_dict)
