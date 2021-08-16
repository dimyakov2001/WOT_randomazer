from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.SupplementListCreator import \
    SupplementListCreator
from src.main.Randomazer.Settings import Settings


class NationSupplementListCreator(SupplementListCreator):

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _create_specification_supplement_list(self):
        nations_list = []
        for nation in self._data[Settings.DATA_NATION_COLUMN_NAME].values:
            if nation not in nations_list:
                nations_list.append(nation)
        return nations_list
