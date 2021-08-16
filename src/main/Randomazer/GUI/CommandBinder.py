from src.main.Randomazer import Utils
from src.main.Randomazer.GUI.SimpleCommandBinder import SimpleCommandBinder


class CommandBinder(SimpleCommandBinder):

    def bind_command_to_dependency(self, dependency_name, command):
        if Utils.is_list(dependency_name) or Utils.is_set(dependency_name):
            self.__bind_command_to_many_dependencies(dependency_name, command)
        else:
            self.__bind_command_to_one_dependency(dependency_name, command)

    def __bind_command_to_many_dependencies(self, dependencies_names, command):
        for dependency_name in dependencies_names:
            self.__bind_command_to_one_dependency(dependency_name, command)

    def __bind_command_to_one_dependency(self, dependency_name, command):
        super().bind_command_to_dependency(dependency_name, command)
