
from src.main.Randomazer.GUI.Main.MainGUICreator import MainGUICreator
from src.main.Randomazer.GUI.Main.MainGUICommandBinder import MainGUICommandBinder
from src.main.Randomazer.GUI.Main.SelectCheckboxEnabler import SelectCheckboxEnabler


class MainGUI:

    gui_creator = None
    command_binder = None
    checkbox_enabler = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.gui_creator = MainGUICreator()
        self.command_binder = MainGUICommandBinder()
        self.checkbox_enabler = SelectCheckboxEnabler()

    def create_and_register_gui(self):
        self._init_gui()
        self._bind_commands()
        self._enable_select_checkboxes()

    def _init_gui(self):
        self.gui_creator.create_and_register_gui()

    def _bind_commands(self):
        self.command_binder.init_basic_commands()
        self.command_binder.init_start_processing_command()

    def _enable_select_checkboxes(self):
        self.checkbox_enabler.enable_select_checkboxes_from_ioc()
