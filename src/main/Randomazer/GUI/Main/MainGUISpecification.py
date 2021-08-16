from src.main.Randomazer.GUI.GUIObjects import Frame, Label, Button, Checkbutton, Entry, Scale, DoubleVarScale
import tkinter as tk
from copy import deepcopy
from src.main.Randomazer.Settings import Settings


class MainGUISpecificationSupplement:

    __specification = {}

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.__specification = MAIN_GUI_SPECIFICATION

    def add_levels_to_specification(self, levels_list):
        self.__add_list_to_specification(Settings.LEVEL_PREFIX, levels_list)

    def add_types_to_specification(self, types_list):
        self.__add_list_to_specification(Settings.TYPE_PREFIX, types_list)

    def add_nations_to_specification(self, nations_list):
        self.__add_list_to_specification(Settings.NATION_PREFIX, nations_list)

    def __add_list_to_specification(self, checkbox_group_name, options_list):
        checkbox_group_name_in_specification_dict = checkbox_group_name + "_main_checkboxes"
        checkbox_group_specification_list = self.__specification["object_descriptions"][
            checkbox_group_name_in_specification_dict]
        group_checkbox_pattern = self.__specification["main_select_checkbox_patterns"][checkbox_group_name]

        for elem in options_list:
            checkbox_specification = self.__format_checkbox_pattern(group_checkbox_pattern, elem)
            checkbox_group_specification_list.append(checkbox_specification)

    @staticmethod
    def __format_checkbox_pattern(source_pattern, option):
        object_name = source_pattern["object_name"]
        object_text = source_pattern["properties_dict"]["text"]
        formatted_object_name = object_name.format(option)
        formatted_object_text = object_text.format(option)

        formatted_pattern = deepcopy(source_pattern)
        formatted_pattern["object_name"] = formatted_object_name
        formatted_pattern["properties_dict"]["text"] = formatted_object_text
        return formatted_pattern


LEVEL_PUBLIC_CHECKBOX_NAME = Settings.LEVEL_PREFIX + Settings.PUBLIC_CHECKBOX_POSTFIX
TYPE_PUBLIC_CHECKBOX_NAME = Settings.TYPE_PREFIX + Settings.PUBLIC_CHECKBOX_POSTFIX
NATION_PUBLIC_CHECKBOX_NAME = Settings.NATION_PREFIX + Settings.PUBLIC_CHECKBOX_POSTFIX

formatting_part = "{}"
LEVEL_COMMON_CHECKBOX_FORMAT_PATTERN = Settings.LEVEL_PREFIX + Settings.COMMON_CHECKBOX_POSTFIX + formatting_part
TYPE_COMMON_CHECKBOX_FORMAT_PATTERN = Settings.TYPE_PREFIX + Settings.COMMON_CHECKBOX_POSTFIX + formatting_part
NATION_COMMON_CHECKBOX_FORMAT_PATTERN = Settings.NATION_PREFIX + Settings.COMMON_CHECKBOX_POSTFIX + formatting_part

MAIN_GUI_SPECIFICATION = {
    "window_params": {
        "size": "600x450",
        "title": "Randomazer v3.0",
        "name": Settings.MAIN_WINDOW_NAME
    },

    "object_placing_order": ["frames", "frame_labels", "buttons", "output", "level_main_checkboxes",
                             "type_main_checkboxes", "nation_main_checkboxes", "priority_selection_elements"],

    "object_descriptions": {
        "frames": [
            {
                "object_name": "top_frame",
                "gui_object_pattern": Frame,
                "master_object_name": Settings.MAIN_WINDOW_NAME,
                "properties_dict": {},
                "location_dict": {"pady": 10}
            },
            {
                "object_name": "start_button_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "top_frame",
                "properties_dict": {},
                "location_dict": {"column": 0, "row": 0}
            },
            {
                "object_name": "output_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "top_frame",
                "properties_dict": {},
                "location_dict": {"column": 1, "row": 0}
            },
            {
                "object_name": "mid_frame",
                "gui_object_pattern": Frame,
                "master_object_name": Settings.MAIN_WINDOW_NAME,
                "properties_dict": {},
                "location_dict": {"padx": 20, "sticky": "W"}
            },
            {
                "object_name": "level_checks_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "mid_frame",
                "properties_dict": {},
                "location_dict": {"column": 0, "row": 0, "padx": 20, "sticky": "N"}
            },
            {
                "object_name": "type_checks_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "mid_frame",
                "properties_dict": {},
                "location_dict": {"column": 1, "row": 0, "padx": 10, "sticky": "N"}
            },
            {
                "object_name": "nation_checks_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "mid_frame",
                "properties_dict": {},
                "location_dict": {"column": 2, "row": 0, "padx": 10, "sticky": "N"}
            },
            {
                "object_name": "priority_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "mid_frame",
                "properties_dict": {},
                "location_dict": {"column": 3, "row": 0, "padx": 20, "sticky": "N"}
            },
            {
                "object_name": "premium_priority_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "priority_frame",
                "properties_dict": {},
                "location_dict": {"column": 0, "row": 0, "sticky": "NW"}
            },
            {
                "object_name": "level_priority_frame",
                "gui_object_pattern": Frame,
                "master_object_name": "priority_frame",
                "properties_dict": {},
                "location_dict": {"column": 0, "row": 1, "pady": 15, "sticky": "N"}
            }
        ],

        "frame_labels": [
            {
                "object_name": "level_frame_label",
                "gui_object_pattern": Label,
                "master_object_name": "level_checks_frame",
                "properties_dict": {"text": "Уровень", "font": ("Arial Bold", 9)},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": "type_frame_label",
                "gui_object_pattern": Label,
                "master_object_name": "type_checks_frame",
                "properties_dict": {"text": "Тип", "font": ("Arial Bold", 9)},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": "nation_frame_label",
                "gui_object_pattern": Label,
                "master_object_name": "nation_checks_frame",
                "properties_dict": {"text": "Нация", "font": ("Arial Bold", 9)},
                "location_dict": {"sticky": "W"}
            }
        ],

        "buttons": [
            {
                "object_name": Settings.START_BUTTON_NAME,
                "gui_object_pattern": Button,
                "master_object_name": "start_button_frame",
                "properties_dict": {"text": "Старт", "width": 25, "height": 5},
                "location_dict": {"padx": 50}
            }
        ],

        "output": [
            {
                "object_name": Settings.OUTPUT_FIELD_NAME,
                "gui_object_pattern": Entry,
                "master_object_name": "output_frame",
                "properties_dict": {"width": 25, "state": "disabled", "font": ("Arial Bold", 14)},
                "location_dict": {"padx": 0, "sticky": "W"}
            }
        ],

        "level_main_checkboxes": [
            {
                "object_name": LEVEL_PUBLIC_CHECKBOX_NAME,
                "gui_object_pattern": Checkbutton,
                "master_object_name": "level_checks_frame",
                "properties_dict": {"text": "Все"},
                "location_dict": {"sticky": "W"}
            }
        ],

        "type_main_checkboxes": [
            {
                "object_name": TYPE_PUBLIC_CHECKBOX_NAME,
                "gui_object_pattern": Checkbutton,
                "master_object_name": "type_checks_frame",
                "properties_dict": {"text": "Все"},
                "location_dict": {"sticky": "W"}
            }
        ],

        "nation_main_checkboxes": [
            {
                "object_name": NATION_PUBLIC_CHECKBOX_NAME,
                "gui_object_pattern": Checkbutton,
                "master_object_name": "nation_checks_frame",
                "properties_dict": {"text": "Все"},
                "location_dict": {"sticky": "W"}
            }
        ],

        "priority_selection_elements": [
            {
                "object_name": Settings.PREMIUM_PRIORITY_CHECKBOX_NAME,
                "gui_object_pattern": Checkbutton,
                "master_object_name": "premium_priority_frame",
                "properties_dict": {"text": "Только премиум техника"},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": Settings.LEVEL_PRIORITY_CHECKBOX_NAME,
                "gui_object_pattern": Checkbutton,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"text": "Установка приоритета уровня"},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": Settings.MEAN_LEVEL_SCALE_NAME,
                "gui_object_pattern": Scale,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"orient": tk.HORIZONTAL, "length": 250, "from_": 1, "to": 10, "tickinterval": 1,
                                    "resolution": 1, "state": "disabled"},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": Settings.MEAN_LEVEL_SCALE_LABEL_NAME,
                "gui_object_pattern": Label,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"text": "Приоритет уровня", "state": "disabled"},
                "location_dict": {}
            },
            {
                "object_name": Settings.STD_LEVEL_SCALE_NAME,
                "gui_object_pattern": DoubleVarScale,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"orient": tk.HORIZONTAL, "length": 250, "from_": 0.1, "to": 3.0, "tickinterval": 0.1,
                                    "resolution": 0.1, "state": "disabled"},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": Settings.STD_LEVEL_SCALE_LABEL_NAME,
                "gui_object_pattern": Label,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"text": "Стандартное отклонение", "state": "disabled"},
                "location_dict": {}
            },
            {
                "object_name": Settings.LIMITS_LEVEL_SCALE_NAME,
                "gui_object_pattern": Scale,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"orient": tk.HORIZONTAL, "length": 250, "from_": 1, "to": 10, "tickinterval": 1,
                                    "resolution": 1, "state": "disabled"},
                "location_dict": {"sticky": "W"}
            },
            {
                "object_name": Settings.LIMITS_LEVEL_SCALE_LABEL_NAME,
                "gui_object_pattern": Label,
                "master_object_name": "level_priority_frame",
                "properties_dict": {"text": "Пределы (+/- уровень)", "state": "disabled"},
                "location_dict": {}
            }
        ]
    },

    "main_select_checkbox_patterns": {
        "level": {
            "object_name": LEVEL_COMMON_CHECKBOX_FORMAT_PATTERN,
            "gui_object_pattern": Checkbutton,
            "master_object_name": "level_checks_frame",
            "properties_dict": {"text": "{}"},
            "location_dict": {"sticky": "W"}
        },
        "type": {
            "object_name": TYPE_COMMON_CHECKBOX_FORMAT_PATTERN,
            "gui_object_pattern": Checkbutton,
            "master_object_name": "type_checks_frame",
            "properties_dict": {"text": "{}"},
            "location_dict": {"sticky": "W"}
        },
        "nation": {
            "object_name": NATION_COMMON_CHECKBOX_FORMAT_PATTERN,
            "gui_object_pattern": Checkbutton,
            "master_object_name": "nation_checks_frame",
            "properties_dict": {"text": "{}"},
            "location_dict": {"sticky": "W"}
        }
    }
}
