import pandas as pd
import numpy as np
import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def some_rv(l, s, x):
    ans = -(l/np.power(s, 2))*np.power(x - l, 2.0) + l
    if ans < 0:
        return 0
    return ans


class Engine:
    _needs_refresh = True
    _main_df = 0
    _previous_answer = ""

    def _read_file(self):
        self._main_df = pd.read_csv(resource_path("RandomData.csv"), encoding="UTF-8", sep=";")
        self._main_df = self._main_df.iloc[:, :5]
        self._main_df.fillna("NaN", inplace=True)

    def fill_settings(self, settings):
        self._read_file()
        settings["levels"] = sorted(list(set(self._main_df["Уровень"])))
        settings["types"] = list(set(self._main_df["Класс"]))
        settings["nations"] = list(set(self._main_df["Нация"]))

    def needs_refresh(self):
        self._needs_refresh = True

    def start(self, values):
        if self._needs_refresh:
            self._refresh_data(values)

        if values["level_priority"]["level_switch"].get():
            weights = list(self._main_df["Уровень"])
            prior_level = float(values["level_priority"]["main_level_scale"].get())
            prior_accuracy = float(values["level_priority"]["add_level_scale"].get())
            weights = list(map(lambda x: some_rv(prior_level, prior_accuracy + 1, float(x)), weights))

            sum_ = sum(weights)
            weights = list(map(lambda x: x/sum_, weights))

            answer = np.random.choice(self._main_df["Название"], replace=True, p=weights)

        else:
            answer = np.random.choice(self._main_df["Название"], replace=True)
            if answer == self._previous_answer:
                answer = np.random.choice(self._main_df["Название"], replace=True)

        values["output"].set(answer)
        self._previous_answer = answer

    def _refresh_data(self, values):
        start_settings = {
            "levels": [],
            "types": [],
            "nations": [],
            "priority": values["level_priority"]["level_switch"].get(),
            "level_priority": values["level_priority"]["main_level_scale"].get(),
            "priority_accuracy": values["level_priority"]["add_level_scale"].get(),
            "premium": values["premium_priority"].get(),
        }

        for key in values["level_checks"]:
            if values["level_checks"][key].get():
                start_settings["levels"].append(int(key))

        for key in values["type_checks"]:
            if values["type_checks"][key].get():
                start_settings["types"].append(key)

        for key in values["nation_checks"]:
            if values["nation_checks"][key].get():
                start_settings["nations"].append(key)

        self._reconfigure(start_settings)
        self._needs_refresh = False

    def _reconfigure(self, settings):
        self._read_file()
        self._main_df = self._main_df.query("Уровень in " + str(settings["levels"]))
        self._main_df = self._main_df.query("Класс in " + str(settings["types"]))
        self._main_df = self._main_df.query("Нация in " + str(settings["nations"]))
        if settings["premium"]:
            self._main_df = self._main_df.query("Премиум != 'NaN'")




