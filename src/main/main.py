from src.main.Randomazer import GUI
from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplier import SpecificationSupplier
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.Engine.DataLoader.DataLoader import DataLoader


class Main:

    __data_loader = None
    __specification_supplier = None
    __main_gui = None

    def start(self):
        self.__init_modules()
        self.__add_checkboxes_descriptions()
        self.__init_gui()
        self.__start_mainloop()

    def __init_modules(self):
        self.__data_loader = DataLoader()
        self.__specification_supplier = SpecificationSupplier()
        self.__main_gui = GUI.MainGUI()

    def __add_checkboxes_descriptions(self):
        self.__data_loader.load_data()
        self.__specification_supplier.supply_main_specification_from_data()

    def __init_gui(self):
        self.__main_gui.create_and_register_gui()

    def __start_mainloop(self):
        window = IOCContainer.resolve_dependency(Settings.MAIN_WINDOW_NAME)
        window.mainloop()


if __name__ == "__main__":
    program = Main()
    program.start()
