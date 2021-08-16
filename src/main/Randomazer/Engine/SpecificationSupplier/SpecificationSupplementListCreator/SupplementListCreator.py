from abc import ABCMeta, abstractmethod
import pandas as pd


class SupplementListCreatorException(Exception):
    pass


class SupplementListCreator(object):
    __metaclass__ = ABCMeta
    _data = None

    def create_supplement_list(self, data):
        self._data = data
        self.__check_data_is_pandas_df()
        return self._create_specification_supplement_list()

    def __check_data_is_pandas_df(self):
        if not isinstance(self._data, pd.DataFrame):
            exception_text = "Can't read data because it is not pandas dataframe."
            raise SupplementListCreatorException(exception_text)

    @abstractmethod
    def _create_specification_supplement_list(self):
        pass
