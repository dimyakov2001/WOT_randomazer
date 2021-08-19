from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class LevelPriorityScaleClickCommand(Command):

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    # scale_value is needed for correct gui working. Because tkinter gives 2 arguments calling scale command
    def execute(self, scale_value=None):
        plot = IOCContainer.resolve_dependency(Settings.PRIORITY_INDICATOR_NAME)
        values_to_set = self.__get_list_to_set_up_level_indicator()
        plot.set_value(values_to_set)

    @staticmethod
    def __get_list_to_set_up_level_indicator():
        mean_value = IOCContainer.resolve_dependency(Settings.MEAN_LEVEL_SCALE_NAME).get_value()
        std_value = IOCContainer.resolve_dependency(Settings.STD_LEVEL_SCALE_NAME).get_value()
        limits = IOCContainer.resolve_dependency(Settings.LIMITS_LEVEL_SCALE_NAME).get_value()
        return [mean_value, std_value, limits]
