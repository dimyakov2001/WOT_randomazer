from src.main.Randomazer.Engine.NormalLevelDistribution import NormalLevelDistribution
from matplotlib import pylab as plt
from matplotlib.pylab import Figure
import numpy as np


class LevelDistributionGraphicsMaker:
    __PLT_FIGURE_SIZE = (4, 3)
    __PLT_X_LIMITS = [1, 10]
    __PLT_Y_LIMITS = [0, 1]

    __LIMITS_LINES_LOW_Y_COORD = 0
    __LIMIT_LINES_COLOR = "r"
    __LIMIT_LINES_WIDTH = 2

    __DISTRIBUTION_CURVE_WIDTH = 2
    __DISTRIBUTION_CURVE_COLOR = "b"

    __MIN_STD_VALUE = 0.001

    __need_to_create_figure = True

    __mean = 0
    __std = __MIN_STD_VALUE
    __limits = 0

    __figure = None
    __axes = None

    # singleton realisation
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if self.__need_to_create_figure:
            self.__make_figure_and_plot()
            self.__need_to_create_figure = False

    def set_params(self, mean, std, limits):
        self.__mean = mean
        self.__limits = limits
        if std < self.__MIN_STD_VALUE:
            self.__std = self.__MIN_STD_VALUE
        else:
            self.__std = std

    def make_graphics(self):
        self.__clear_axes()
        self.__set_figure_limits()
        self.__draw_grid()
        self.__draw_distribution_curve()
        self.__draw_level_limits_lines()
        self.__make_filling()
        return self.__figure

    def __make_figure_and_plot(self):
        self.__figure = Figure(figsize=self.__PLT_FIGURE_SIZE)
        self.__axes = self.__figure.add_subplot(1, 1, 1)

    def __clear_axes(self):
        self.__axes.clear()

    def __set_figure_limits(self):
        self.__axes.set_xlim(self.__PLT_X_LIMITS)
        self.__axes.set_ylim(self.__PLT_Y_LIMITS)

    def __draw_grid(self):
        self.__axes.grid()

    def __draw_level_limits_lines(self):
        left_line_x_coord = self.__mean - self.__limits
        right_line_x_coord = self.__mean + self.__limits
        left_line_max_y = NormalLevelDistribution.generate_pdf(left_line_x_coord, self.__mean, self.__std)
        right_line_max_y = NormalLevelDistribution.generate_pdf(right_line_x_coord, self.__mean, self.__std)

        self.__axes.vlines(left_line_x_coord, self.__LIMITS_LINES_LOW_Y_COORD, left_line_max_y,
                           colors=self.__LIMIT_LINES_COLOR, linewidth=self.__LIMIT_LINES_WIDTH)
        self.__axes.vlines(right_line_x_coord, self.__LIMITS_LINES_LOW_Y_COORD, right_line_max_y,
                           colors=self.__LIMIT_LINES_COLOR, linewidth=self.__LIMIT_LINES_WIDTH)

    def __draw_distribution_curve(self):
        x = np.linspace(1, 10, 1000)
        y = NormalLevelDistribution.generate_pdf(x, self.__mean, self.__std)
        self.__axes.plot(x, y, color=self.__DISTRIBUTION_CURVE_COLOR, linewidth=self.__DISTRIBUTION_CURVE_WIDTH)

    def __make_filling(self):
        left_line_x_coord = self.__mean - self.__limits
        right_line_x_coord = self.__mean + self.__limits
        x = np.linspace(left_line_x_coord, right_line_x_coord, 100)
        y = NormalLevelDistribution.generate_pdf(x, self.__mean, self.__std)
        self.__axes.fill_between(x, 0, y, alpha=0.5)

    @staticmethod
    def show_graphics():
        plt.show()
