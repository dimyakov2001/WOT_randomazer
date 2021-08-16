import unittest

from src.test.Randomazer.TestDataLoader import TestDataLoader
from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator import \
    LevelSupplementListCreator
from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.TypeSupplementListCreator import \
    TypeSupplementListCreator
from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.NationSupplementListCreator import \
    NationSupplementListCreator
from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.SupplementListCreator import \
    SupplementListCreatorException
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.Engine.TankSelector.GaussianTankSelector import GaussianTankSelector
from src.main.Randomazer.Engine.TankSelector.TankSelectionTypes import TankSelectionTypes


class DataLoaderTest(unittest.TestCase):

    def test_read_data(self):
        data_loader = TestDataLoader()
        data_loader.load_data()
        print(len(IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)))


class ListCreatorsTest(unittest.TestCase):

    def test_levels_list_creator(self):
        data_loader = TestDataLoader()
        level_supplement_list_creator = LevelSupplementListCreator()

        data_loader.load_data()
        data = IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)
        levels_list = level_supplement_list_creator.create_supplement_list(data)
        self.assertEqual(levels_list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_types_list_creator(self):
        data_loader = TestDataLoader()
        type_supplement_list_creator = TypeSupplementListCreator()

        data_loader.load_data()
        data = IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)
        types_list = type_supplement_list_creator.create_supplement_list(data)
        self.assertEqual(types_list, ['ЛТ', 'СТ', 'ТТ', 'ПТ', 'САУ'])

    def test_nations_list_creator(self):
        data_loader = TestDataLoader()
        nation_supplement_list_creator = NationSupplementListCreator()

        data_loader.load_data()
        data = IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)
        nations_list = nation_supplement_list_creator.create_supplement_list(data)
        self.assertEqual(nations_list,
                         ['СССР', 'Германия', 'США', 'Франция', 'Британия', 'Китай', 'Япония', 'Швеция', 'Италия',
                          'Польша'])

    def test_list_creator_exception(self):
        data = [1, 2, 3, 4, 5]
        level_supplement_list_creator = LevelSupplementListCreator()
        with self.assertRaises(SupplementListCreatorException):
            level_supplement_list_creator.create_supplement_list(data)


class GaussianTankSelectDistributionTest(unittest.TestCase):
    __TEST_RANGE = 1000

    __LEVEL_MEAN = 2
    __LEVEL_SCATTER = 3

    __data_loader = None
    __tank_selector = None
    __data = None

    def test(self):
        self.__prepare()
        self.__data_loader.load_data()
        self.__set_selector_properties()
        self.__load_data()

        answer_stat = {}
        for i in range(self.__TEST_RANGE):
            answer = self.__tank_selector.select(self.__data)
            level = self.__get_tank_level(answer)
            if level in answer_stat.keys():
                answer_stat[level] += 1
            else:
                answer_stat[level] = 1

        print(answer_stat)

    def __prepare(self):
        self.__data_loader = TestDataLoader()
        self.__tank_selector = GaussianTankSelector()

    def __set_selector_properties(self):
        self.__tank_selector.set_params(self.__LEVEL_MEAN, self.__LEVEL_SCATTER)

    def __load_data(self):
        self.__data = IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)

    def __get_tank_level(self, tank_name):
        return self.__data.loc[self.__data[Settings.DATA_TANK_COLUMN_NAME] == tank_name, Settings.DATA_LEVEL_COLUMN_NAME].values[0]