from src.main.Randomazer.Engine.SpecificationSupplier import SpecificationSupplementListCreator as ListCreator
from src.main.Randomazer.GUI.Main.MainGUISpecification import MainGUISpecificationSupplement
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class SpecificationSupplier:
    __main_gui_specification_supplier = None
    __level_list_creator = None
    __type_list_creator = None
    __nation_list_creator = None
    __data = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.__main_gui_specification_supplier = MainGUISpecificationSupplement()
        self.__init_list_creators()

    def __init_list_creators(self):
        self.__level_list_creator = ListCreator.LevelSupplementListCreator()
        self.__type_list_creator = ListCreator.TypeSupplementListCreator()
        self.__nation_list_creator = ListCreator.NationSupplementListCreator()

    def supply_main_specification_from_data(self):
        self.__load_data_from_ioc()
        self.__add_levels()
        self.__add_types()
        self.__add_nations()

    def __load_data_from_ioc(self):
        self.__data = IOCContainer.resolve_dependency(Settings.DATA_OBJECT_NAME)

    def __add_levels(self):
        levels_list = self.__level_list_creator.create_supplement_list(self.__data)
        self.__main_gui_specification_supplier.add_levels_to_specification(levels_list)

    def __add_types(self):
        types_list = self.__type_list_creator.create_supplement_list(self.__data)
        self.__main_gui_specification_supplier.add_types_to_specification(types_list)

    def __add_nations(self):
        nations_list = self.__nation_list_creator.create_supplement_list(self.__data)
        self.__main_gui_specification_supplier.add_nations_to_specification(nations_list)
