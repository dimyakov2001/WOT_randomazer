from src.main.Randomazer.Engine.DataFilter import DataFilter
from src.main.Randomazer.Commands.Command import Command
from src.main.Randomazer.GUI.Main.AnswerIndicator import AnswerIndicator
from src.main.Randomazer.Engine.CentralTankSelector import CentralTankTankSelector
from src.main.Randomazer.Engine.TankSelector.TankSelectionTypes import TankSelectionTypes
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class StartButtonClickCommand(Command):

    __data_filter = None
    __answer_indicator = None
    __selector = None

    def __init__(self):
        self.__data_filter = DataFilter()
        self.__answer_indicator = AnswerIndicator()
        self.__selector = CentralTankTankSelector()

    def execute(self):
        data = self.__data_filter.get_filtered_data()
        if IOCContainer.resolve_dependency(Settings.LEVEL_PRIORITY_CHECKBOX_NAME).get_value():
            answer = self.__selector.select(data, TankSelectionTypes.GAUSSIAN)
        else:
            answer = self.__selector.select(data, TankSelectionTypes.UNIFORM)
        self.__answer_indicator.indicate_answer(answer)
