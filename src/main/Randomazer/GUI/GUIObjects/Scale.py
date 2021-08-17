from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable
from abc import ABCMeta


class Scale(GUIObject, GUIVariable):
    __metaclass__ = ABCMeta

    _SET_ITEM_DICT = {}

    def _init_set_item_dict(self):
        self._SET_ITEM_DICT = {
            "start_position": self._set_start_position
        }

    def _set_start_position(self, value):
        self._variable.set(value)

    def _set_properties_to_object(self, properties_dict):
        for property_to_set in properties_dict.keys():
            self.__setitem__(property_to_set, properties_dict[property_to_set])

    def __setitem__(self, key, value):
        if key in self._SET_ITEM_DICT.keys():
            set_item_func = self._SET_ITEM_DICT[key]
            set_item_func.__call__(value)
        else:
            super().__setitem__(key, value)
