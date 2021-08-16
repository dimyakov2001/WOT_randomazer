from src.main.Randomazer.GUI.GUIObjectUtils import GUIObjectUtils
from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.IOCContainer import IOCContainer


class SimpleCommandBinder:

    __command_to_bind = None
    __dependency_name = ""

    def __init__(self):
        self.__command_to_bind = None
        self.__dependency_name = ""

    def bind_command_to_dependency(self, dependency_name, command):
        self.__command_to_bind = command
        self.__dependency_name = dependency_name
        self.__find_object_and_bind_command()

    def __find_object_and_bind_command(self):
        object_to_bind = IOCContainer.resolve_dependency(self.__dependency_name)
        if issubclass(self.__command_to_bind.__class__, Command):
            self.__command_to_bind = self.__command_to_bind.execute
        self.__bind_command_to_object_if_possible(object_to_bind)

    def __bind_command_to_object_if_possible(self, gui_object):
        if GUIObjectUtils.gui_object_can_contain_command(gui_object):
            GUIObjectUtils.bind_command_to_gui_object(gui_object, self.__command_to_bind)