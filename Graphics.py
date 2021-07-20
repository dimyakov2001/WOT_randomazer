import tkinter as tk
from tkinter.ttk import Checkbutton
from tkinter.ttk import Progressbar


class GUI:
    _WINDOW_TITLE = "Randomazer v3.0"
    _WINDOW_SIZE = "600x450"

    _window = 0
    _elements = {}
    _values = {}

    def get_values(self):
        return self._values

    def get_elements(self):
        return self._elements

    def _get_common_value(self, dict_):
        value = True
        for key in dict_:
            value *= dict_[key].get()
        return value

    def _public_checkbox_click(self, public_checkbox_value, checkboxes_values_array, command):
        for elem in checkboxes_values_array:
            checkboxes_values_array[elem].set(public_checkbox_value.get())
        command()

    def _priority_checkbox_click(self):
        val = "disable"
        if self._values["level_priority"]["level_switch"].get():
            val = "active"
        self._elements["level_priority"]["main_level_scale"]["state"] = val
        self._elements["level_priority"]["label1"]["state"] = val
        self._elements["level_priority"]["add_level_scale"]["state"] = val
        self._elements["level_priority"]["label2"]["state"] = val

    # Разметка верхней части окна
    def _init_top(self):
        top_frame = tk.Frame(master=self._window)
        top_frame.grid(pady=10)
        start_button_frame = tk.Frame(master=top_frame)
        start_button_frame.grid(column=0, row=0, padx=20)
        output_frame = tk.Frame(master=top_frame)
        output_frame.grid(column=1, row=0, padx=10, sticky="W")

        self._elements["start_button"] = tk.Button(master=start_button_frame, text="Старт", width=25, height=5,
                                                   command=None)
        self._elements["start_button"].grid()
        self._elements["start_button"].focus()

        self._elements["progressbar"] = Progressbar(master=output_frame, length=250)
        self._elements["progressbar"].grid(sticky="W")

        self._elements["output"] = tk.Entry(master=output_frame, width=35, state="disabled", font=("Arial Bold", 10))
        self._elements["output"].grid(pady=10, sticky="W")

    def _init_med(self, settings):
        mid_frame = tk.Frame(master=self._window)
        mid_frame.grid(padx=20, sticky="W")
        levels_checks_frame = tk.Frame(master=mid_frame)
        levels_checks_frame.grid(column=0, row=0, padx=20, sticky="N")
        type_checks_frame = tk.Frame(master=mid_frame)
        type_checks_frame.grid(column=1, row=0, padx=10, sticky="N")
        nation_checks_frame = tk.Frame(master=mid_frame)
        nation_checks_frame.grid(column=2, row=0, padx=10, sticky="N")

        priority_frame = tk.Frame(master=mid_frame)
        priority_frame.grid(column=3, row=0, padx=20, sticky="N")
        premium_priority_frame = tk.Frame(master=priority_frame)
        premium_priority_frame.grid(column=0, row=0, sticky="NW")
        level_priority_frame = tk.Frame(master=priority_frame)
        level_priority_frame.grid(column=0, row=1, pady=15, sticky="N")

        tk.Label(master=levels_checks_frame, text="Уровень", font=("Arial Bold", 9)).grid(sticky="W")
        tk.Label(master=type_checks_frame, text="Тип", font=("Arial Bold", 9)).grid(sticky="W")
        tk.Label(master=nation_checks_frame, text="Нация", font=("Arial Bold", 9)).grid(sticky="W")

        self._elements["level_public_check"] = Checkbutton(levels_checks_frame, text="Все", var=None)
        self._elements["level_public_check"].grid(sticky="W")
        self._elements["type_public_check"] = Checkbutton(type_checks_frame, text="Все", var=None)
        self._elements["type_public_check"].grid(sticky="W")
        self._elements["nation_public_check"] = Checkbutton(nation_checks_frame, text="Все", var=None)
        self._elements["nation_public_check"].grid(sticky="W")

        self._elements["level_checks"] = {}
        self._elements["type_checks"] = {}
        self._elements["nation_checks"] = {}

        for elem in settings["levels"]:
            self._elements["level_checks"][str(elem)] = Checkbutton(levels_checks_frame, text=elem, var=None)
            self._elements["level_checks"][str(elem)].grid(sticky="W")

        for elem in settings["types"]:
            self._elements["type_checks"][str(elem)] = Checkbutton(type_checks_frame, text=elem, var=None)
            self._elements["type_checks"][str(elem)].grid(sticky="W")

        for elem in settings["nations"]:
            self._elements["nation_checks"][str(elem)] = Checkbutton(nation_checks_frame, text=elem, var=None)
            self._elements["nation_checks"][str(elem)].grid(sticky="W")

        # приоритеты уровня и премиальности
        self._elements["premium_priority"] = Checkbutton(premium_priority_frame, text="Только премиум техника", var=None)
        self._elements["premium_priority"].grid(sticky="W")

        self._elements["level_priority"] = {}

        self._elements["level_priority"]["level_switch"] = Checkbutton(level_priority_frame, text="Установка приоритета уровня", var=None)
        self._elements["level_priority"]["level_switch"].grid(sticky="W")

        self._elements["level_priority"]["main_level_scale"] = tk.Scale(level_priority_frame, orient=tk.HORIZONTAL, length=250, from_=1, to=10, tickinterval=1, resolution=1, state="disabled")
        self._elements["level_priority"]["main_level_scale"].grid(sticky="W")

        self._elements["level_priority"]["label1"] = tk.Label(level_priority_frame, text="Приоритет уровня", state="disabled")
        self._elements["level_priority"]["label1"].grid()

        self._elements["level_priority"]["add_level_scale"] = tk.Scale(level_priority_frame, orient=tk.HORIZONTAL, length=250, from_=1, to=9, tickinterval=1, resolution=1, state="disabled")
        self._elements["level_priority"]["add_level_scale"].grid(sticky="W")

        self._elements["level_priority"]["label2"] = tk.Label(level_priority_frame, text="Точность", state="disabled")
        self._elements["level_priority"]["label2"].grid()

    def _bind_vars(self):
        self._values = {
            "level_checks": {},
            "type_checks": {},
            "nation_checks": {},
            "level_priority": {},
            "output": tk.StringVar(),
            "level_public_check": tk.BooleanVar(),
            "type_public_check": tk.BooleanVar(),
            "nation_public_check": tk.BooleanVar(),
            "premium_priority": tk.BooleanVar()
        }

        self._elements["output"]["text"] = self._values["output"]

        self._elements["level_public_check"]["var"] = self._values["level_public_check"]
        self._elements["type_public_check"]["var"] = self._values["type_public_check"]
        self._elements["nation_public_check"]["var"] = self._values["nation_public_check"]

        for key in self._elements["level_checks"]:
            self._values["level_checks"][key] = tk.BooleanVar()
            self._elements["level_checks"][key]["var"] = self._values["level_checks"][key]

        for key in self._elements["type_checks"]:
            self._values["type_checks"][key] = tk.BooleanVar()
            self._elements["type_checks"][key]["var"] = self._values["type_checks"][key]

        for key in self._elements["nation_checks"]:
            self._values["nation_checks"][key] = tk.BooleanVar()
            self._elements["nation_checks"][key]["var"] = self._values["nation_checks"][key]

        # приоритеты уровня и премиальности
        self._elements["premium_priority"]["var"] = self._values["premium_priority"]

        self._values["level_priority"]["level_switch"] = tk.BooleanVar()
        self._values["level_priority"]["main_level_scale"] = tk.IntVar()
        self._values["level_priority"]["add_level_scale"] = tk.IntVar()

        self._elements["level_priority"]["level_switch"]["var"] = self._values["level_priority"]["level_switch"]
        self._elements["level_priority"]["main_level_scale"]["var"] = self._values["level_priority"]["main_level_scale"]
        self._elements["level_priority"]["add_level_scale"]["var"] = self._values["level_priority"]["add_level_scale"]

    def _set_vars(self):
        # установка всех флажков на True
        for key1 in ("level_checks", "type_checks", "nation_checks"):
            for key2 in self._values[key1]:
                self._values[key1][key2].set(True)

        # исключение
        # todo

        # установка флагов для чекбоксов типа "все"
        self._values["level_public_check"].set(self._get_common_value(self._values["level_checks"]))
        self._values["type_public_check"].set(self._get_common_value(self._values["type_checks"]))
        self._values["nation_public_check"].set(self._get_common_value(self._values["nation_checks"]))

        # приоритеты уровня и премиальности
        self._values["premium_priority"].set(False)
        self._values["level_priority"]["level_switch"].set(False)
        self._values["level_priority"]["main_level_scale"].set(1)
        self._values["level_priority"]["add_level_scale"].set(2)

    def _bind_commands(self, settings):
        # команда для кнопки
        self._elements["start_button"]["command"] = lambda: settings["start_button_command"](self._values)

        # команды для верхних чекбоксов
        self._elements["level_public_check"]["command"] = lambda: self._public_checkbox_click(
            self._values["level_public_check"], self._values["level_checks"], settings["refresh_data_command"])
        self._elements["type_public_check"]["command"] = lambda: self._public_checkbox_click(
            self._values["type_public_check"], self._values["type_checks"], settings["refresh_data_command"])
        self._elements["nation_public_check"]["command"] = lambda: self._public_checkbox_click(
            self._values["nation_public_check"], self._values["nation_checks"], settings["refresh_data_command"])

        # комадны для нижних чекбоксов
        for key1 in ("level_checks", "type_checks", "nation_checks"):
            for key2 in self._elements[key1]:
                self._elements[key1][key2]["command"] = settings["refresh_data_command"]

        # приоритеты уровня и премиальности
        self._elements["premium_priority"]["command"] = settings["refresh_data_command"]
        self._elements["level_priority"]["level_switch"]["command"] = self._priority_checkbox_click
        # self._elements["level_priority"]["main_level_scale"]["command"] = settings["refresh_data_command"]
        # self._elements["level_priority"]["add_level_scale"]["command"] = settings["refresh_data_command"]

    def __init__(self, settings):
        self._window = tk.Tk()
        self._window.title(self._WINDOW_TITLE)
        self._window.geometry(self._WINDOW_SIZE)

        self._init_top()
        self._init_med(settings)
        self._bind_vars()
        self._set_vars()
        self._bind_commands(settings)

    def start(self):
        self._window.mainloop()
