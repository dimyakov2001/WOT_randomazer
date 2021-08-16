from src.main.Randomazer.Commands.CommonCheckboxClickCommand.CommonCheckboxClickCommand import \
    CommonCheckboxClickCommand
from src.main.Randomazer.Settings import Settings


class NationCommonCheckboxClickCommand(CommonCheckboxClickCommand):

    def __init__(self):
        super().__init__(Settings.NATION_PREFIX)

    def execute(self):
        super().execute()
