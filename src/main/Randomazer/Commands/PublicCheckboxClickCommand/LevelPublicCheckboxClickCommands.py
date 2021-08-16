from src.main.Randomazer.Commands.PublicCheckboxClickCommand.PublicCheckboxClickCommand import \
    PublicCheckboxClickCommand
from src.main.Randomazer.Settings import Settings


class LevelPublicCheckboxClickCommand(PublicCheckboxClickCommand):

    def __init__(self):
        super().__init__(Settings.LEVEL_PREFIX)

    def execute(self):
        super().execute()
