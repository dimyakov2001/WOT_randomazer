from abc import ABCMeta

from src.main.Randomazer.GUI.GUIObjectUtils import GUIObjectUtils
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class FilterListCreator:
    __metaclass__ = ABCMeta

    __checkbox_group_find_regular = ""
    __checkbox_group_prefix = ""

    __checkboxes = []

    def __init__(self, checkbox_group_name):
        self.__checkbox_group_find_regular = checkbox_group_name + Settings.COMMON_CHECKBOX_POSTFIX_PATTERN
        self.__checkbox_group_prefix = checkbox_group_name + Settings.COMMON_CHECKBOX_POSTFIX
        self.__checkboxes = []

    def create_filter_list(self):
        self.__get_checkboxes_names_from_ioc()
        self.__delete_unchecked_checkboxes_names_from_list()
        return self.__make_filter_list_from_checkboxes_texts()

    def __get_checkboxes_names_from_ioc(self):
        checkboxes_names_set = IOCContainer.find_dependency_names_by_regular(self.__checkbox_group_find_regular)
        for checkbox_name in checkboxes_names_set:
            checkbox_object = IOCContainer.resolve_dependency(checkbox_name)
            self.__checkboxes.append(checkbox_object)

    def __delete_unchecked_checkboxes_names_from_list(self):
        reversed_checkboxes_indices_list = self.__get_reversed_checkboxes_indices_list()
        for i in reversed_checkboxes_indices_list:
            checkbox_value = self.__checkboxes[i].get_value()
            if not checkbox_value:
                self.__delete_checkbox_from_list(i)

    def __make_filter_list_from_checkboxes_texts(self):
        filter_list = []
        for checkbox in self.__checkboxes:
            checkbox_text = GUIObjectUtils.get_gui_object_text(checkbox)
            filter_list_elem = self._make_filter_elem_from_checkbox_text(checkbox_text)
            filter_list.append(filter_list_elem)
        return filter_list

    def __get_reversed_checkboxes_indices_list(self):
        checkboxes_indices_list = range(len(self.__checkboxes))
        reversed_checkboxes_indices_list = checkboxes_indices_list[::-1]
        return reversed_checkboxes_indices_list

    def __delete_checkbox_from_list(self, checkbox_index):
        self.__checkboxes.pop(checkbox_index)

    @staticmethod
    def _make_filter_elem_from_checkbox_text(checkbox_text):
        return checkbox_text
