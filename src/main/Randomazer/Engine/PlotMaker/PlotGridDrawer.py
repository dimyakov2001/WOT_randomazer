import matplotlib.pylab as plt


class PlotGridDrawer:

    PLT_X_LIMITS = [1, 10]
    PLT_Y_LIMITS = [0, 1]
    PLT_FIGURE_FACECOLOR = "#f0f0f0"

    @staticmethod
    def draw_grid_in_plot_pack(plot_pack):
        figure = plot_pack.get_figure()
        axes = plot_pack.get_axes()
        PlotGridDrawer.__clear_axes(axes)
        PlotGridDrawer.__set_limits(axes)
        PlotGridDrawer.__set_figure_facecolor(figure)
        PlotGridDrawer.__set_plot_facecolor(axes)
        PlotGridDrawer.__set_up_ticks(axes)
        PlotGridDrawer.__draw_grid(axes)
        plot_pack.figure = figure
        plot_pack.axes = axes

    @staticmethod
    def __clear_axes(axes):
        axes.clear()

    @staticmethod
    def __set_limits(axes):
        axes.set_xlim(PlotGridDrawer.PLT_X_LIMITS)
        axes.set_ylim(PlotGridDrawer.PLT_Y_LIMITS)

    @staticmethod
    def __set_figure_facecolor(figure):
        figure.patch.set_facecolor(PlotGridDrawer.PLT_FIGURE_FACECOLOR)

    @staticmethod
    def __set_plot_facecolor(axes):
        axes.set_facecolor(PlotGridDrawer.PLT_FIGURE_FACECOLOR)

    @staticmethod
    def __set_up_ticks(axes):
        start_x = PlotGridDrawer.PLT_X_LIMITS[0]
        end_x = PlotGridDrawer.PLT_X_LIMITS[1]
        axes.set_xticks(range(start_x, end_x + 1))

    @staticmethod
    def __draw_grid(axes):
        axes.grid()
