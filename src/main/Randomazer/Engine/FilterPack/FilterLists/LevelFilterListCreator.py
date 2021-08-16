from src.main.Randomazer.Engine.FilterPack.FilterLists.FilterListCreator import FilterListCreator
from src.main.Randomazer.Settings import Settings


class LevelFilterListCreator(FilterListCreator):

    def __init__(self):
        super().__init__(Settings.LEVEL_PREFIX)

    @staticmethod
    def _make_filter_elem_from_checkbox_text(checkbox_text):
        return int(checkbox_text)
