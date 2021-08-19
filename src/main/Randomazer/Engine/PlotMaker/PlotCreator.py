from src.main.Randomazer.Engine.PlotMaker.PlotPack import PlotPack
from matplotlib.pylab import Figure


class PlotCreator:
    PLT_FIGURE_SIZE = [4, 3]

    @staticmethod
    def create_as_plot_pack():
        figure = PlotCreator.__create_figure()
        axes = PlotCreator.__create_axes(figure)
        plot_pack = PlotCreator.__create_plot_pack(figure, axes)
        return plot_pack

    @staticmethod
    def __create_figure():
        return Figure(figsize=PlotCreator.PLT_FIGURE_SIZE)

    @staticmethod
    def __create_axes(figure):
        return figure.add_subplot(1, 1, 1)

    @staticmethod
    def __create_plot_pack(figure, axes):
        plot_pack = PlotPack(figure, axes)
        return plot_pack
