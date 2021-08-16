from src.main.Randomazer.GUI.GUIObjectInitiator import GUIObjectInitiator
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings

import tkinter as tk
from copy import copy

  
class GUICreator:
    _object_initiator = None
    _gui_specification = {}

    def __init__(self, gui_specification):
        self._object_initiator = GUIObjectInitiator()
        self._gui_specification = copy(gui_specification)

    def create_and_register_gui(self):
        # todo проверка ключей в спецификации
        self._init_window()
        self._init_gui_elements()

    def _init_window(self):
        window_params = self._gui_specification[Settings.SPECIFICATION_WINDOW_PARAMS_KEY]
        window_title = window_params[Settings.SPECIFICATION_WINDOW_TITLE_KEY]
        window_size = window_params[Settings.SPECIFICATION_WINDOW_SIZE_KEY]
        window_name = window_params[Settings.SPECIFICATION_WINDOW_NAME_KEY]

        window = tk.Tk()
        window.title(window_title)
        window.geometry(window_size)
        IOCContainer.register_dependency(window_name, window)

    def _init_gui_elements(self):
        objects_description = self._gui_specification[Settings.SPECIFICATION_OBJECT_DESCRIPTION_KEY]
        object_placing_order = self._gui_specification[Settings.SPECIFICATION_OBJECTS_PLACING_ORDER_KEY]

        for objects_group_name in object_placing_order:
            objects_group_description = objects_description[objects_group_name]
            self._init_group_of_gui_elements(objects_group_description)

    def _init_group_of_gui_elements(self, gui_elements_group):
        for gui_element_description in gui_elements_group:
            self._object_initiator.create_register_and_locate_object(gui_element_description)
