from src.main.Randomazer.Engine.PlotMaker.PlotGridDrawer import PlotGridDrawer
from src.main.Randomazer.Engine.NormalLevelDistribution import NormalLevelDistribution
from src.main.Randomazer.Settings import Settings
import numpy as np


class PlotWriter:
    LIMITS_LINES_LOW_Y_COORD = 0
    LIMIT_LINES_COLOR = "r"
    LIMIT_LINES_WIDTH = 2

    DISTRIBUTION_CURVE_RESOLUTION = 1000
    DISTRIBUTION_HIST_SIZE = 1000
    DISTRIBUTION_FILLING_RESOLUTION = 100

    DISTRIBUTION_CURVE_WIDTH = 2
    DISTRIBUTION_CURVE_COLOR = "b"

    DISTRIBUTION_HIST_COLOR = "g"
    DISTRIBUTION_HIST_ALPHA = 0.3

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
        PlotWriter.__draw_distribution(axes)

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
    def __draw_distribution(axes):
        rvs_keys, rvs_values = PlotWriter.__make_rvs_stats()
        axes.bar(rvs_keys, rvs_values, alpha=PlotWriter.DISTRIBUTION_HIST_ALPHA,
                 color=PlotWriter.DISTRIBUTION_HIST_COLOR)

    @staticmethod
    def __make_rvs_stats():
        rvs_dict = PlotWriter.__make_rvs_dict()
        rvs_keys = sorted(rvs_dict.keys())
        rvs_values = []
        for key in rvs_keys:
            rvs_values.append(rvs_dict[key] / PlotWriter.DISTRIBUTION_HIST_SIZE)
        return rvs_keys, rvs_values

    @staticmethod
    def __make_rvs_dict():
        rvs_dict = {}
        for i in range(PlotWriter.DISTRIBUTION_HIST_SIZE):
            level = round(NormalLevelDistribution.generate_rvs(PlotWriter.__mean, PlotWriter.__std, size=1)[0])
            if level not in rvs_dict.keys():
                rvs_dict[level] = 0
            rvs_dict[level] += 1
        return rvs_dict

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
        x_left = Settings.PLOT_X_LIMITS[0]
        x_right = Settings.PLOT_X_LIMITS[1]
        x = np.linspace(x_left, x_right, PlotWriter.DISTRIBUTION_CURVE_RESOLUTION)
        y = NormalLevelDistribution.generate_pdf(x, PlotWriter.__mean, PlotWriter.__std)
        axes.plot(x, y, color=PlotWriter.DISTRIBUTION_CURVE_COLOR, linewidth=PlotWriter.DISTRIBUTION_CURVE_WIDTH)

    @staticmethod
    def __make_filling(axes):
        left_line_x_coord = PlotWriter.__mean - PlotWriter.__limits
        right_line_x_coord = PlotWriter.__mean + PlotWriter.__limits
        x = np.linspace(left_line_x_coord, right_line_x_coord, PlotWriter.DISTRIBUTION_FILLING_RESOLUTION)
        y = NormalLevelDistribution.generate_pdf(x, PlotWriter.__mean, PlotWriter.__std)
        axes.fill_between(x, 0, y, alpha=0.5)
