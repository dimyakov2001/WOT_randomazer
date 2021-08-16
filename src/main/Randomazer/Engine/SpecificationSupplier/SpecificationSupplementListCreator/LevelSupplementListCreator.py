from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.SupplementListCreator import \
    SupplementListCreator
from src.main.Randomazer.Settings import Settings


class LevelSupplementListCreator(SupplementListCreator):

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _create_specification_supplement_list(self):
        levels_set = set(self._data[Settings.DATA_LEVEL_COLUMN_NAME])
        levels_list = sorted(list(levels_set))
        return levels_list
