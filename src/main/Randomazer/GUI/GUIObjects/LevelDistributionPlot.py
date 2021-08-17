from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.main.Randomazer.Engine.LevelDistributionGraphicsMaker import LevelDistributionGraphicsMaker
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable


class LevelDistributionPlot(GUIObject, GUIVariable):
    __graphics_maker = None

    def __init__(self, master, properties_dict):
        self.__graphics_maker = LevelDistributionGraphicsMaker()
        self.__create_canvas(master)

    def __create_canvas(self, master_object):
        figure = self.__graphics_maker.make_graphics()
        if isinstance(master_object, GUIObject):
            self._object = FigureCanvasTkAgg(figure, master_object._object)
        else:
            self._object = FigureCanvasTkAgg(figure)

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
