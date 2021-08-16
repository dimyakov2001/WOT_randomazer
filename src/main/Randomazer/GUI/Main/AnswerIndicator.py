from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class AnswerIndicator:

    __output_field_object = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.__output_field_object = IOCContainer.resolve_dependency(Settings.OUTPUT_FIELD_NAME)

    def indicate_answer(self, text):
        self.__output_field_object.set_value(text)
