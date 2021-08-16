from src.main.Randomazer.IOCContainer import IOCContainer
from src.main.Randomazer.Settings import Settings


class GUIObjectInitiator:
    __description = {}
    __object = None

    def create_register_and_locate_object(self, object_description):
        self.__description = object_description

        self.__create_object()
        self.__register_object()
        self.__locate_object()

    def __create_object(self):
        master_object = self.__find_master_object()
        object_type = self.__description[Settings.SPECIFICATION_OBJECT_PATTERN_KEY]
        properties_dict = self.__description[Settings.SPECIFICATION_OBJECT_PROPERTIES_KEY]
        self.__object = object_type(master_object, properties_dict)

    def __register_object(self):
        object_name = self.__description[Settings.SPECIFICATION_OBJECT_NAME_KEY]
        IOCContainer.register_dependency(object_name, self.__object)

    def __locate_object(self):
        location_dict = self.__description[Settings.SPECIFICATION_OBJECT_LOCATION_KEY]
        self.__object.locate(location_dict)

    def __find_master_object(self):
        master_object_name = self.__description[Settings.SPECIFICATION_OBJECT_MASTER_OBJECT_KEY]
        master_object = IOCContainer.resolve_dependency(master_object_name)
        return master_object
