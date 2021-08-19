import unittest

from src.main.Randomazer.Engine.PlotMaker.PlotGridDrawer import PlotGridDrawer
from src.main.Randomazer.Engine.PlotMaker.PlotPack import PlotPack
import matplotlib.pylab as plt


class GridDrawerTest(unittest.TestCase):
    def test(self):
        figure = plt.Figure(figsize=(12, 8))
        axes = figure.add_subplot(1, 1, 1)

        plot_pack = PlotPack()
        plot_pack.figure = figure
        plot_pack.axes = axes

        PlotGridDrawer.draw_grid_in_plot_pack(plot_pack)

        plt.show()
