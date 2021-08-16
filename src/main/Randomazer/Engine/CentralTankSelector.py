from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.Engine.TankSelector.TankSelectionTypes import TankSelectionTypes
from src.main.Randomazer.Engine.TankSelector.UniformTankSelector import UniformTankSelector
from src.main.Randomazer.Engine.TankSelector.GaussianTankSelector import GaussianTankSelector
from src.main.Randomazer.IOCContainer import IOCContainer


class TankSelectorException(Exception):
    pass


class CentralTankTankSelector:
    __selectors = {}
    __selection_methods = {}

    __data = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.__selectors = {
            TankSelectionTypes.UNIFORM: UniformTankSelector(),
            TankSelectionTypes.GAUSSIAN: GaussianTankSelector()
        }
        self.__selection_methods = {
            TankSelectionTypes.UNIFORM: self.__select_uniform,
            TankSelectionTypes.GAUSSIAN: self.__select_gaussian
        }

    def select(self, data, selection_type):
        self.__data = data
        try:
            selection_method = self.__selection_methods[selection_type]
        except KeyError:
            TankSelectorException("Selection types should be TankSelectorTypes enum objects")
        else:
            return selection_method()

    def __select_uniform(self):
        return self.__selectors[TankSelectionTypes.UNIFORM].select(self.__data)

    def __select_gaussian(self):
        level_priority_mean = self.__get_level_priority_mean()
        level_priority_scatter = self.__get_level_priority_scatter()
        selector = self.__selectors[TankSelectionTypes.GAUSSIAN]
        selector.set_params(level_priority_mean, level_priority_scatter)
        return selector.select(self.__data)

    @staticmethod
    def __get_level_priority_mean():
        return IOCContainer.resolve_dependency(Settings.MEAN_LEVEL_SCALE_NAME).get_value()

    @staticmethod
    def __get_level_priority_scatter():
        return IOCContainer.resolve_dependency(Settings.SCATTER_LEVEL_SCALE_NAME).get_value()
