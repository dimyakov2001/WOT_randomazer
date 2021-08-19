class PlotPack:
    __figure = None
    __axes = None

    def __init__(self, figure, axes):
        self.__figure = figure
        self.__axes = axes

    def get_figure(self):
        return self.__figure

    def get_axes(self):
        return self.__axes
