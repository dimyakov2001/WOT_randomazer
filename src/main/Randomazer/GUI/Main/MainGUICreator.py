from src.main.Randomazer.GUI.GUICreator import GUICreator
from src.main.Randomazer.GUI.Main.MainGUISpecification import MAIN_GUI_SPECIFICATION


class MainGUICreator(GUICreator):

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(MAIN_GUI_SPECIFICATION)

    def create_and_register_gui(self):
        super().create_and_register_gui()
