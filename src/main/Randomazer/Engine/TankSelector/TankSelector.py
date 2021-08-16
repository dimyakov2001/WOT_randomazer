from abc import ABCMeta, abstractmethod
from src.main.Randomazer.Settings import Settings


class TankSelector:
    __metaclass__ = ABCMeta

    _EMPTY_ANSWER_STR = "None"
    _data = None

    def select(self, data):
        self._data = data
        return self._make_choice()

    @abstractmethod
    def _make_choice(self):
        pass

    def _get_tank_name_from_data_by_index(self, index):
        return self._data.iloc[index][Settings.DATA_TANK_COLUMN_NAME]
