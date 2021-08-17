from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.main.Randomazer.Engine.LevelDistributionGraphicsMaker import LevelDistributionGraphicsMaker
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable


class LevelDistributionPlot(GUIObject, GUIVariable):
    __graphics_maker = None

    __SETITEM_DICT = {}

    def __init__(self, master, properties_dict):
        self.__graphics_maker = LevelDistributionGraphicsMaker()
        self.__create_canvas(master)

        self.__SETITEM_DICT = {
            GUIObject.GUI_OBJECT_STATE_FIELD: self.__set_state
        }

    def __create_canvas(self, master_object):
        figure = self.__get_figure()
        if isinstance(master_object, GUIObject):
            self._object = FigureCanvasTkAgg(figure, master_object._object)
        else:
            self._object = FigureCanvasTkAgg(figure)

    def __get_figure(self):
        return self.__graphics_maker.clear()

    def keys(self):
        return []

    def get_value(self):
        return self.__graphics_maker.make_graphics()

    def locate(self, location_dict):
        self._object.get_tk_widget().grid(location_dict)

    def set_value(self, value):
        mean = value[0]
        std = value[1]
        limits = value[2]
        self.__graphics_maker.set_params(mean, std, limits)
        self.__graphics_maker.make_graphics()
        self._object.draw()

    def __setitem__(self, key, value):
        func_to_call = self.__SETITEM_DICT[key]
        func_to_call.__call__(value)

    def __set_state(self, value):
        if value == GUIObject.GUI_OBJECT_STATE_DISABLED:
            self.__disable_graphic()
        elif value == GUIObject.GUI_OBJECT_STATE_ENABLED:
            self.__enable_graphics()

    def __disable_graphic(self):
        self.__graphics_maker.clear()
        self._object.draw()

    def __enable_graphics(self):
        self.__graphics_maker.make_graphics()
        self._object.draw()
