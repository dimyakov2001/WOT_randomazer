
class Settings:
    CHECKBOX_POSTFIX = "check"
    PUBLIC_OBJECT_RADICAL = "public"

    CHECKBOX_POSTFIX_PATTERN = "\\w*" + CHECKBOX_POSTFIX + "(_\\w*)?"
    PUBLIC_CHECKBOX_POSTFIX = "_" + PUBLIC_OBJECT_RADICAL + "_" + CHECKBOX_POSTFIX
    COMMON_CHECKBOX_POSTFIX = "_" + CHECKBOX_POSTFIX + "_"
    COMMON_CHECKBOX_POSTFIX_PATTERN = COMMON_CHECKBOX_POSTFIX + "\\w*"

    LEVEL_PREFIX = "level"
    NATION_PREFIX = "nation"
    TYPE_PREFIX = "type"

    PREMIUM_PRIORITY_CHECKBOX_NAME = "premium_priority"
    LEVEL_PRIORITY_CHECKBOX_NAME = "level_priority"
    MEAN_LEVEL_SCALE_NAME = "mean_level_scale"
    SCATTER_LEVEL_SCALE_NAME = "scatter_level_scale"
    MEAN_LEVEL_SCALE_LABEL_NAME = "mean_level_scale_label"
    SCATTER_LEVEL_SCALE_LABEL_NAME = "scatter_level_scale_label"
    OUTPUT_FIELD_NAME = "output_field"
    START_BUTTON_NAME = "start_button"

    DATA_TYPE_COLUMN_NAME = "Класс"
    DATA_NATION_COLUMN_NAME = "Нация"
    DATA_LEVEL_COLUMN_NAME = "Уровень"
    DATA_PREMIUM_COLUMN_NAME = "Премиум"
    DATA_TANK_COLUMN_NAME = "Название"
    DATA_PREMIUM_FLAG = "+"
    TYPES_SORT_SETTINGS = {
        "ЛТ": 0,
        "СТ": 1,
        "ТТ": 2,
        "ПТ": 3,
        "САУ": 4
    }

    SPECIFICATION_WINDOW_PARAMS_KEY = "window_params"
    SPECIFICATION_WINDOW_TITLE_KEY = "title"
    SPECIFICATION_WINDOW_SIZE_KEY = "size"
    SPECIFICATION_WINDOW_NAME_KEY = "name"

    SPECIFICATION_OBJECT_DESCRIPTION_KEY = "object_descriptions"
    SPECIFICATION_OBJECTS_PLACING_ORDER_KEY = "object_placing_order"

    SPECIFICATION_OBJECT_NAME_KEY = "object_name"
    SPECIFICATION_OBJECT_PATTERN_KEY = "gui_object_pattern"
    SPECIFICATION_OBJECT_MASTER_OBJECT_KEY = "master_object_name"
    SPECIFICATION_OBJECT_PROPERTIES_KEY = "properties_dict"
    SPECIFICATION_OBJECT_LOCATION_KEY = "location_dict"

    MAIN_WINDOW_NAME = "main_window"
    DATA_OBJECT_NAME = "data"

    @staticmethod
    def get_public_checkbox_name_by_group(checkbox_group_name):
        return checkbox_group_name + Settings.PUBLIC_CHECKBOX_POSTFIX

    @staticmethod
    def get_common_checkbox_pattern_by_group(checkbox_group_name):
        return checkbox_group_name + Settings.COMMON_CHECKBOX_POSTFIX_PATTERN
