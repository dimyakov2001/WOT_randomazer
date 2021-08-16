from src.main.Randomazer.Settings import Settings
from src.main.Randomazer.IOCContainer import IOCContainer


class PremiumPriorityFlagGetter:

    __premium_priority_checkbox = None

    def __init__(self):
        self.__premium_priority_checkbox = IOCContainer.resolve_dependency(Settings.PREMIUM_PRIORITY_CHECKBOX_NAME)

    def get_premium_priority_flag(self):
        return self.__premium_priority_checkbox.get_value()
