from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.GUI.GUIObjectUtils import GUIObjectUtils
from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class LevelPriorityCheckboxClickCommand(Command):
    __level_priority_elements_state = False

    def execute(self):
        self.__get_level_priority_elements_state()
        self.__set_scales_state()
        self.__set_scales_labels_state()

    def __get_level_priority_elements_state(self):
        level_priority_checkbox = IOCContainer.resolve_dependency(Settings.LEVEL_PRIORITY_CHECKBOX_NAME)
        self.__level_priority_elements_state = level_priority_checkbox.get_value()

    def __set_scales_state(self):
        mean_level_scale = IOCContainer.resolve_dependency(Settings.MEAN_LEVEL_SCALE_NAME)
        dispersion_level_scale = IOCContainer.resolve_dependency(Settings.SCATTER_LEVEL_SCALE_NAME)
        GUIObjectUtils.set_gui_object_state(mean_level_scale, self.__level_priority_elements_state)
        GUIObjectUtils.set_gui_object_state(dispersion_level_scale, self.__level_priority_elements_state)

    def __set_scales_labels_state(self):
        mean_level_scale_label = IOCContainer.resolve_dependency(Settings.MEAN_LEVEL_SCALE_LABEL_NAME)
        dispersion_level_scale_label = IOCContainer.resolve_dependency(
            Settings.SCATTER_LEVEL_SCALE_LABEL_NAME)
        GUIObjectUtils.set_gui_object_state(mean_level_scale_label, self.__level_priority_elements_state)
        GUIObjectUtils.set_gui_object_state(dispersion_level_scale_label, self.__level_priority_elements_state)
