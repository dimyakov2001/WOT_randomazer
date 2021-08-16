import pandas as pd
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class DataLoader:
    _DATA_FILE_PATH = "..\\..\\data\\RandomData.csv"
    _DATA_FILE_ENCODING = "UTF-8"
    _DATA_FILE_SEPARATOR = ";"
    _DATA_FILE_COLUMN_NUMBER = 5

    __data = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def load_data(self):
        self.__read_data()
        self.__register_data()

    def __read_data(self):
        path = self._DATA_FILE_PATH
        encoding = self._DATA_FILE_ENCODING
        separator = self._DATA_FILE_SEPARATOR

        data = pd.read_csv(path, encoding=encoding, sep=separator)
        self.__data = data.iloc[:, :self._DATA_FILE_COLUMN_NUMBER]

    def __register_data(self):
        IOCContainer.register_dependency(Settings.DATA_OBJECT_NAME, self.__data)
