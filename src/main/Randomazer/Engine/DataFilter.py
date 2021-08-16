from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Engine.FilterPack.FilterLists.LevelFilterListCreator import LevelFilterListCreator
from src.main.Randomazer.Engine.FilterPack.FilterLists.TypeFilterListCreator import TypeFilterListCreator
from src.main.Randomazer.Engine.FilterPack.FilterLists.NationFilterListCreator import NationFilterListCreator
from src.main.Randomazer.Engine.FilterPack.PremiumPriorityFlagGetter import PremiumPriorityFlagGetter
import pandas as pd
from copy import copy


class DataFilterException(Exception):
    pass


class DataFilter:
    __data = None
    __level_filter_list_creator = None
    __type_filter_list_creator = None
    __nation_filter_list_creator = None
    __premium_priority_flag_getter = None

    def __init__(self):
        self.__level_filter_list_creator = LevelFilterListCreator()
        self.__type_filter_list_creator = TypeFilterListCreator()
        self.__nation_filter_list_creator = NationFilterListCreator()
        self.__premium_priority_flag_getter = PremiumPriorityFlagGetter()

    def get_filtered_data(self):
        self.__load_data_copy_from_ioc()
        self.__check_data_is_pandas_df()
        self.__filter_levels()
        self.__filter_types()
        self.__filter_nations()
        self.__filter_premium()
        return self.__data

    def __load_data_copy_from_ioc(self):
        self.__data = copy(IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME))

    def __check_data_is_pandas_df(self):
        if not isinstance(self.__data, pd.DataFrame):
            exception_text = "Can't read data because it is not pandas dataframe."
            raise DataFilterException(exception_text)

    def __filter_levels(self):
        levels_filter_list = self.__level_filter_list_creator.create_filter_list()
        self.__filter_data(Settings.DATA_LEVEL_COLUMN_NAME, levels_filter_list)

    def __filter_types(self):
        types_filter_list = self.__type_filter_list_creator.create_filter_list()
        self.__filter_data(Settings.DATA_TYPE_COLUMN_NAME, types_filter_list)

    def __filter_nations(self):
        nations_filter_list = self.__nation_filter_list_creator.create_filter_list()
        self.__filter_data(Settings.DATA_NATION_COLUMN_NAME, nations_filter_list)

    def __filter_premium(self):
        if self.__premium_priority_flag_getter.get_premium_priority_flag():
            premium_filter_list = [Settings.DATA_PREMIUM_FLAG]
            self.__filter_data(Settings.DATA_PREMIUM_COLUMN_NAME, premium_filter_list)

    def __filter_data(self, column_name, filter_list):
        self.__data = self.__data.loc[self.__data[column_name].isin(filter_list)]
