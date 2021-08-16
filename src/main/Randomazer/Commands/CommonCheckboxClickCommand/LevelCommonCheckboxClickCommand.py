from src.main.Randomazer.Commands.CommonCheckboxClickCommand.CommonCheckboxClickCommand import \
    CommonCheckboxClickCommand
from src.main.Randomazer.Settings import Settings


class LevelCommonCheckboxClickCommand(CommonCheckboxClickCommand):

    def __init__(self):
        super().__init__(Settings.LEVEL_PREFIX)

    def execute(self):
        super().execute()
