from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.GUI.CommandBinder import CommandBinder

from src.main.Randomazer.Commands.PublicCheckboxClickCommand.LevelPublicCheckboxClickCommands import \
    LevelPublicCheckboxClickCommand
from src.main.Randomazer.Commands.PublicCheckboxClickCommand.TypePublicCheckboxClickCommands import \
    TypePublicCheckboxClickCommand
from src.main.Randomazer.Commands.PublicCheckboxClickCommand.NationPublicCheckboxClickCommands import \
    NationPublicCheckboxClickCommand
from src.main.Randomazer.Commands.CommonCheckboxClickCommand.LevelCommonCheckboxClickCommand import \
    LevelCommonCheckboxClickCommand
from src.main.Randomazer.Commands.CommonCheckboxClickCommand.TypeCommonCheckboxClickCommand import \
    TypeCommonCheckboxClickCommand
from src.main.Randomazer.Commands.CommonCheckboxClickCommand.NationCommonCheckboxClickCommand import \
    NationCommonCheckboxClickCommand
from src.main.Randomazer.Commands.LevelPriorityCheckboxClickCommand import LevelPriorityCheckboxClickCommand
from src.main.Randomazer.Commands.StartButtonClickCommand import StartButtonClickCommand
from src.main.Randomazer.Commands.LevelPriorityScaleClickCommand import LevelPriorityScaleClickCommand


class MainGUICommandBinder:
    __LEVEL_PUBLIC_CHECKBOX_NAME = Settings.get_public_checkbox_name_by_group(Settings.LEVEL_PREFIX)
    __TYPE_PUBLIC_CHECKBOX_NAME = Settings.get_public_checkbox_name_by_group(Settings.TYPE_PREFIX)
    __NATION_PUBLIC_CHECKBOX_NAME = Settings.get_public_checkbox_name_by_group(Settings.NATION_PREFIX)

    __COMMON_LEVEL_CHECKBOXES_PATTERN = Settings.get_common_checkbox_pattern_by_group(Settings.LEVEL_PREFIX)
    __COMMON_TYPE_CHECKBOXES_PATTERN = Settings.get_common_checkbox_pattern_by_group(Settings.TYPE_PREFIX)
    __COMMON_NATION_CHECKBOXES_PATTERN = Settings.get_common_checkbox_pattern_by_group(Settings.NATION_PREFIX)

    __command_binder = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.__command_binder = CommandBinder()

    def init_basic_commands(self):
        self.__init_public_checkboxes_commands()
        self.__init_common_checkboxes_commands()
        self.__init_level_priority_checkbox_command()
        self.__init_level_priority_scales_command()

    def __init_public_checkboxes_commands(self):
        level_public_checkbox_command = LevelPublicCheckboxClickCommand()
        self.__command_binder.bind_command_to_dependency(MainGUICommandBinder.__LEVEL_PUBLIC_CHECKBOX_NAME,
                                                         level_public_checkbox_command)

        type_public_checkbox_command = TypePublicCheckboxClickCommand()
        self.__command_binder.bind_command_to_dependency(MainGUICommandBinder.__TYPE_PUBLIC_CHECKBOX_NAME,
                                                         type_public_checkbox_command)

        nation_public_checkbox_command = NationPublicCheckboxClickCommand()
        self.__command_binder.bind_command_to_dependency(MainGUICommandBinder.__NATION_PUBLIC_CHECKBOX_NAME,
                                                         nation_public_checkbox_command)

    def __init_common_checkboxes_commands(self):
        self.__bind_command_to_level_common_checkboxes()
        self.__bind_command_to_type_common_checkboxes()
        self.__bind_command_to_nation_common_checkboxes()

    def __init_level_priority_checkbox_command(self):
        level_priority_checkbox_command = LevelPriorityCheckboxClickCommand()
        self.__command_binder.bind_command_to_dependency(Settings.LEVEL_PRIORITY_CHECKBOX_NAME,
                                                         level_priority_checkbox_command)

    def __bind_command_to_level_common_checkboxes(self):
        level_common_checkbox_command = LevelCommonCheckboxClickCommand()
        level_common_checkboxes_names = IOCContainer.find_dependency_names_by_regular(
            self.__COMMON_LEVEL_CHECKBOXES_PATTERN)
        self.__command_binder.bind_command_to_dependency(level_common_checkboxes_names, level_common_checkbox_command)

    def __bind_command_to_type_common_checkboxes(self):
        type_common_checkbox_command = TypeCommonCheckboxClickCommand()
        type_common_checkboxes_names = IOCContainer.find_dependency_names_by_regular(
            self.__COMMON_TYPE_CHECKBOXES_PATTERN)
        self.__command_binder.bind_command_to_dependency(type_common_checkboxes_names, type_common_checkbox_command)

    def __bind_command_to_nation_common_checkboxes(self):
        nation_common_checkbox_command = NationCommonCheckboxClickCommand()
        nation_common_checkboxes_names = IOCContainer.find_dependency_names_by_regular(
            self.__COMMON_NATION_CHECKBOXES_PATTERN)
        self.__command_binder.bind_command_to_dependency(nation_common_checkboxes_names, nation_common_checkbox_command)

    def __init_level_priority_scales_command(self):
        level_scales_command = LevelPriorityScaleClickCommand()
        self.__command_binder.bind_command_to_dependency(Settings.MEAN_LEVEL_SCALE_NAME, level_scales_command)
        self.__command_binder.bind_command_to_dependency(Settings.STD_LEVEL_SCALE_NAME, level_scales_command)
        self.__command_binder.bind_command_to_dependency(Settings.LIMITS_LEVEL_SCALE_NAME, level_scales_command)

    def init_start_processing_command(self):
        start_button_command = StartButtonClickCommand()
        self.__command_binder.bind_command_to_dependency(Settings.START_BUTTON_NAME, start_button_command)
