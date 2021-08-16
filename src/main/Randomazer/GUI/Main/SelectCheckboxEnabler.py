from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class SelectCheckboxEnabler:
    __checkboxes_names_to_enable = set()

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def enable_select_checkboxes_from_ioc(self):
        self.__find_checkboxes_variables_to_enable()
        self.__enable_checkboxes_from_names_set()

    def __find_checkboxes_variables_to_enable(self):
        self.__checkboxes_names_to_enable = IOCContainer.find_dependency_names_by_regular(
            Settings.CHECKBOX_POSTFIX_PATTERN)

    def __enable_checkboxes_from_names_set(self):
        for variable_name in self.__checkboxes_names_to_enable:
            checkbox_variable = IOCContainer.resolve_dependency(variable_name)
            checkbox_variable.set_value(True)
