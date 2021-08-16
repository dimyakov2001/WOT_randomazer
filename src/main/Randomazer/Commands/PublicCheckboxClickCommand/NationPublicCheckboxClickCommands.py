from src.main.Randomazer.Commands.PublicCheckboxClickCommand.PublicCheckboxClickCommand import \
    PublicCheckboxClickCommand
from src.main.Randomazer.Settings import Settings


class NationPublicCheckboxClickCommand(PublicCheckboxClickCommand):

    def __init__(self):
        super().__init__(Settings.NATION_PREFIX)

    def execute(self):
        super().execute()
