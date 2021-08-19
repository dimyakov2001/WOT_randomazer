from src.main.Randomazer.Engine.PlotMaker.PlotGridDrawer import PlotGridDrawer
from src.main.Randomazer.Engine.NormalLevelDistribution import NormalLevelDistribution
from matplotlib import pylab
import numpy as np


class PlotWriter:
    LIMITS_LINES_LOW_Y_COORD = 0
    LIMIT_LINES_COLOR = "r"
    LIMIT_LINES_WIDTH = 2

    DISTRIBUTION_CURVE_WIDTH = 2
    DISTRIBUTION_CURVE_COLOR = "b"

    __MIN_STD_VALUE = 0.001

    __mean = 0
    __std = 0
    __limits = 0

    @staticmethod
    def write_plot_to_plot_pack(plot_pack, params):
        axes = plot_pack.get_axes()
        PlotWriter.__clear_axes(axes)
        PlotWriter.__print_grid(plot_pack)
        PlotWriter.__unpack_params(params)
        PlotWriter.__draw_level_limits_lines(axes)
        PlotWriter.__draw_distribution_curve(axes)
        PlotWriter.__make_filling(axes)

    @staticmethod
    def __clear_axes(axes):
        axes.clear()

    @staticmethod
    def __print_grid(plot_pack):
        PlotGridDrawer.draw_grid_in_plot_pack(plot_pack)

    @staticmethod
    def __unpack_params(params):
        PlotWriter.__mean = params[0]
        PlotWriter.__std = params[1]
        PlotWriter.__limits = params[2]
        if PlotWriter.__std < PlotWriter.__MIN_STD_VALUE:
            PlotWriter.__std = PlotWriter.__MIN_STD_VALUE

    @staticmethod
    def __draw_level_limits_lines(axes):
        left_line_x_coord = PlotWriter.__mean - PlotWriter.__limits
        right_line_x_coord = PlotWriter.__mean + PlotWriter.__limits
        left_line_max_y = NormalLevelDistribution.generate_pdf(left_line_x_coord, PlotWriter.__mean, PlotWriter.__std)
        right_line_max_y = NormalLevelDistribution.generate_pdf(right_line_x_coord, PlotWriter.__mean, PlotWriter.__std)

        axes.vlines(left_line_x_coord, PlotWriter.LIMITS_LINES_LOW_Y_COORD, left_line_max_y,
                    colors=PlotWriter.LIMIT_LINES_COLOR, linewidth=PlotWriter.LIMIT_LINES_WIDTH)
        axes.vlines(right_line_x_coord, PlotWriter.LIMITS_LINES_LOW_Y_COORD, right_line_max_y,
                    colors=PlotWriter.LIMIT_LINES_COLOR, linewidth=PlotWriter.LIMIT_LINES_WIDTH)

    @staticmethod
    def __draw_distribution_curve(axes):
        x = np.linspace(1, 10, 1000)
        y = NormalLevelDistribution.generate_pdf(x, PlotWriter.__mean, PlotWriter.__std)
        axes.plot(x, y, color=PlotWriter.DISTRIBUTION_CURVE_COLOR, linewidth=PlotWriter.DISTRIBUTION_CURVE_WIDTH)

    @staticmethod
    def __make_filling(axes):
        left_line_x_coord = PlotWriter.__mean - PlotWriter.__limits
        right_line_x_coord = PlotWriter.__mean + PlotWriter.__limits
        x = np.linspace(left_line_x_coord, right_line_x_coord, 100)
        y = NormalLevelDistribution.generate_pdf(x, PlotWriter.__mean, PlotWriter.__std)
        axes.fill_between(x, 0, y, alpha=0.5)
