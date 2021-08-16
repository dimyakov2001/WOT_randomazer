from src.main.Randomazer.Engine.FilterPack.FilterLists.FilterListCreator import FilterListCreator
from src.main.Randomazer.Settings import Settings


class NationFilterListCreator(FilterListCreator):

    def __init__(self):
        super().__init__(Settings.NATION_PREFIX)
