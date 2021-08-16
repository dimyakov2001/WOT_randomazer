import re


class IOCContainerException(Exception):
    pass


class IOCContainer:
    _objects = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def register_dependency(dependency_name, object_to_register):
        IOCContainer._objects[dependency_name] = object_to_register

    @staticmethod
    def resolve_dependency(dependency_name):
        try:
            return IOCContainer._objects[dependency_name]
        except KeyError:
            raise IOCContainerException("Can't find dependence '" + dependency_name + "' to resolve.")

    @staticmethod
    def delete_dependency(dependency_name):
        try:
            del IOCContainer._objects[dependency_name]
        except KeyError:
            raise IOCContainerException("Can't find dependence '" + dependency_name + "' to delete.")

    @staticmethod
    def count_elements_registered():
        return len(IOCContainer._objects)

    @staticmethod
    def existing_dependencies():
        return IOCContainer._objects.keys()

    @staticmethod
    def find_dependency_names_by_regular(regular_expression):
        result_set = set()
        for dependence_name in IOCContainer.existing_dependencies():
            if re.fullmatch(regular_expression, dependence_name) is not None:
                result_set.add(dependence_name)
        return result_set
