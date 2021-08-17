import unittest

from src.main.Randomazer.Engine.LevelDistributionGraphicsMaker import LevelDistributionGraphicsMaker


class LevelDistributionGraphicsTest(unittest.TestCase):

    def test(self):
        graphics_maker = None
        graphics_maker = LevelDistributionGraphicsMaker()
        graphics_maker.set_params(5, 1, 2)
        graphics_maker.make_graphics()
        graphics_maker.show_graphics()