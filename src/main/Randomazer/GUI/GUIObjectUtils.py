from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable


class GUIObjectUtils:

    @staticmethod
    def gui_object_has_variable(object_to_check):
        return isinstance(object_to_check, GUIVariable)

    @staticmethod
    def bind_command_to_gui_object(gui_object, command):
        gui_object[GUIObject.GUI_OBJECT_COMMAND_FIELD] = command

    @staticmethod
    def gui_object_can_contain_command(object_to_check):
        return GUIObject.GUI_OBJECT_COMMAND_FIELD in object_to_check.keys()

    @staticmethod
    def set_gui_object_state(object_to_change_state, boolean_state):
        state = GUIObject.GUI_OBJECT_STATE_DISABLED
        if boolean_state is True:
            state = GUIObject.GUI_OBJECT_STATE_ENABLED
        object_to_change_state[GUIObject.GUI_OBJECT_STATE_FIELD] = state

    @staticmethod
    def get_gui_object_text(gui_object):
        return gui_object[GUIObject.GUI_OBJECT_TEXT_FIELD]
