from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class PublicCheckboxClickCommand(Command):
    __public_checkbox_name = ""
    __common_checkboxes_names_pattern = ""
    __public_checkbox_value = None

    def __init__(self, checkbox_group_name):
        self.__public_checkbox_name = Settings.get_public_checkbox_name_by_group(checkbox_group_name)
        self.__common_checkboxes_names_pattern = Settings.get_common_checkbox_pattern_by_group(checkbox_group_name)
        self.__checkbox_group_name = checkbox_group_name

    def execute(self):
        self.__public_checkbox_value = IOCContainer.resolve_dependency(self.__public_checkbox_name).get_value()
        self.__set_public_checkbox_value_to_group()

    def __set_public_checkbox_value_to_group(self):
        common_checkboxes_names_to_change_value = self.__find_common_checkboxes_names()
        self.__set_public_checkbox_value_to_objects(common_checkboxes_names_to_change_value)

    def __find_common_checkboxes_names(self):
        object_to_change_value = IOCContainer.find_dependency_names_by_regular(self.__common_checkboxes_names_pattern)
        return object_to_change_value

    def __set_public_checkbox_value_to_objects(self, objects_names):
        for object_name in objects_names:
            object_to_change_value = IOCContainer.resolve_dependency(object_name)
            object_to_change_value.set_value(self.__public_checkbox_value)
