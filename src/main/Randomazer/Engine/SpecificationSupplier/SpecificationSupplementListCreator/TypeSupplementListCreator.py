from src.main.Randomazer.Engine.SpecificationSupplier.SpecificationSupplementListCreator.SupplementListCreator import \
    SupplementListCreator, SupplementListCreatorException
from src.main.Randomazer.Settings import Settings


class TypeSupplementListCreator(SupplementListCreator):

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _create_specification_supplement_list(self):
        types_set = set(self._data[Settings.DATA_TYPE_COLUMN_NAME])
        types_list = sorted(list(types_set), key=self.__get_type_index)
        return types_list

    @staticmethod
    def __get_type_index(typename):
        try:
            return Settings.TYPES_SORT_SETTINGS[typename]
        except KeyError:
            raise SupplementListCreatorException("Wrong vehicle type. See valid types in Settings.TYPES_SORT_SETTINGS")
