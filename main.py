from Engine import Engine
from Graphics import GUI

if __name__ == "__main__":
    settings = {}

    engine = Engine()
    engine.fill_settings(settings)

    settings["start_button_command"] = engine.start
    settings["refresh_data_command"] = engine.needs_refresh

    gui = GUI(settings)
    gui.start()
