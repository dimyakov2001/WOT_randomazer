from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.main.Randomazer.Engine.PlotMaker.PlotCreator import PlotCreator
from src.main.Randomazer.GUI.GUIObjects.GUIObject import GUIObject
from src.main.Randomazer.GUI.GUIObjects.GUIVariable import GUIVariable
from src.main.Randomazer.Engine.PlotMaker.PlotWriter import PlotWriter
from src.main.Randomazer.Engine.PlotMaker.PlotGridDrawer import PlotGridDrawer
from src.main.Randomazer.Settings import Settings


class LevelDistributionPlot(GUIObject, GUIVariable):
    __plot_pack = None
    __values = None

    __SETITEM_DICT = {}

    def __init__(self, master, properties_dict):
        self.__plot_pack = PlotCreator.create_as_plot_pack()
        self.__master_object = master
        self.__values = [Settings.MEAN_LEVEL_SCALE_START_VALUE, Settings.STD_LEVEL_SCALE_START_VALUE,
                         Settings.LIMITS_LEVEL_SCALE_START_VALUE]

        self.__create_canvas()
        self.__clear_graphics()
        self.__SETITEM_DICT = {
            GUIObject.GUI_OBJECT_STATE_FIELD: self.__set_state
        }

    def __create_canvas(self):
        figure = self.__plot_pack.get_figure()
        if isinstance(self.__master_object, GUIObject):
            self._object = FigureCanvasTkAgg(figure, self.__master_object._object)
        else:
            self._object = FigureCanvasTkAgg(figure)

    def keys(self):
        return []

    def get_value(self):
        return self.__plot_pack

    def locate(self, location_dict):
        self._object.get_tk_widget().grid(location_dict)

    def set_value(self, value):
        self.__values = value
        self.__draw_graphics()

    def __setitem__(self, key, value):
        func_to_call = self.__SETITEM_DICT[key]
        func_to_call.__call__(value)

    def __set_state(self, value):
        if value == GUIObject.GUI_OBJECT_STATE_DISABLED:
            self.__clear_graphics()
        elif value == GUIObject.GUI_OBJECT_STATE_ENABLED:
            self.__draw_graphics()

    def __clear_graphics(self):
        PlotGridDrawer.draw_grid_in_plot_pack(self.__plot_pack)
        self._object.draw()

    def __draw_graphics(self):
        PlotWriter.write_plot_to_plot_pack(self.__plot_pack, self.__values)
        self._object.draw()
