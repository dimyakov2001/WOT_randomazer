from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class CommonCheckboxClickCommand(Command):
    __group_public_checkbox_name = ""
    __checkboxes_group_names_pattern = ""

    def __init__(self, checkbox_group_name):
        self.__group_public_checkbox_name = Settings.get_public_checkbox_name_by_group(checkbox_group_name)
        self.__checkboxes_group_names_pattern = Settings.get_common_checkbox_pattern_by_group(checkbox_group_name)

    def execute(self):
        public_checkbox = IOCContainer.resolve_dependency(self.__group_public_checkbox_name)

        if self.__find_objects_and_get_values_disjunction():
            public_checkbox.set_value(True)
        if self.__find_objects_and_get_values_conjunction() is False:
            public_checkbox.set_value(False)

    def __find_objects_and_get_values_disjunction(self):
        result = False
        object_names = IOCContainer.find_dependency_names_by_regular(self.__checkboxes_group_names_pattern)

        for object_name in object_names:
            object_value = IOCContainer.resolve_dependency(object_name).get_value()
            result = result or object_value

        return result

    def __find_objects_and_get_values_conjunction(self):
        result = True
        object_names = IOCContainer.find_dependency_names_by_regular(self.__checkboxes_group_names_pattern)

        for object_name in object_names:
            object_value = IOCContainer.resolve_dependency(object_name).get_value()
            result = result and object_value

        return result
