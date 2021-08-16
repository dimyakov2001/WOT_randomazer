from abc import ABCMeta


class GUIVariable:
    __metaclass__ = ABCMeta

    GUI_OBJECT_VARIABLE_FIELD = "variable"

    _variable = None

    def get_value(self):
        return self._variable.get()

    def set_value(self, value):
        self._variable.set(value)
