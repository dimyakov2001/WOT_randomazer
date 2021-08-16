from src.main.Randomazer.Engine.TankSelector.TankSelector import TankSelector
from src.main.Randomazer.Engine.TankSelector.UniformTankSelector import UniformTankSelector
from src.main.Randomazer.Settings import Settings
from scipy.stats import norm
import random


class GaussianTankSelector(TankSelector):
    __SCALE_TO_SIGM_CONVERT_CONST = 3
    __LEVEL_LIST_CAPACITY = 1000

    __uniform_tank_selector = None
    __mean = 5
    __stdev = 5
    __limits = 5

    def __init__(self):
        self.__uniform_tank_selector = UniformTankSelector()

    def set_params(self, mean, stdev, scale):
        self.__mean = mean
        self.__stdev = stdev
        self.__limits = scale

    def _make_choice(self):
        level_to_chose_tank = self.__get_gaussian_level()
        one_level_data = self.__select_level_from_data(level_to_chose_tank)
        return self.__uniform_tank_selector.select(one_level_data)

    def __get_gaussian_level(self):
        level_list = norm.rvs(loc=self.__mean, scale=self.__stdev, size=self.__LEVEL_LIST_CAPACITY)
        level_list = self.__round_level_list(level_list)
        level_list = self.__filter_level_list_by_data(level_list)
        level_list = self.__filter_level_list_by_scale_thresholds(level_list)
        selected_level = random.choice(level_list)
        return selected_level

    @staticmethod
    def __round_level_list(level_list):
        return list(map(lambda level: round(level), level_list))

    def __filter_level_list_by_data(self, level_list):
        data_levels = set(self._data[Settings.DATA_LEVEL_COLUMN_NAME])
        return list(filter(lambda level: level in data_levels, level_list))

    def __filter_level_list_by_scale_thresholds(self, level_list):
        lower_threshold = self.__mean - self.__limits
        higher_threshold = self.__mean + self.__limits
        return list(filter(lambda level: lower_threshold <= level <= higher_threshold, level_list))

    def __select_level_from_data(self, level):
        return self._data.loc[self._data[Settings.DATA_LEVEL_COLUMN_NAME] == level]
