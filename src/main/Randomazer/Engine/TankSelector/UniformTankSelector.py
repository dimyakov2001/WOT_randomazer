from src.main.Randomazer.Engine.TankSelector.TankSelector import TankSelector
import random


class UniformTankSelector(TankSelector):

    def _make_choice(self):
        if len(self._data) > 0:
            index = self.__get_random_index_of_data_row()
            answer = self._get_tank_name_from_data_by_index(index)
        else:
            answer = self._EMPTY_ANSWER_STR
        return answer

    def __get_random_index_of_data_row(self):
        return random.randint(0, len(self._data) - 1)


