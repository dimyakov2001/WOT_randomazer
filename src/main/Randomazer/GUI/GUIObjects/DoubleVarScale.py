import tkinter as tk
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable


class DoubleVarScale(GUIObject, GUIVariable):

    def __init__(self, master, properties_dict):
        self._create_object_by_type(tk.Scale, master)
        self._set_properties_to_object(properties_dict)
        self._variable = tk.DoubleVar()
        self._object[self.GUI_OBJECT_VARIABLE_FIELD] = self._variable
