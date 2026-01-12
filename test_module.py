import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelTestCase(unittest.TestCase):
    def test_plot(self):
        ax = sea_level_predictor.draw_plot()

        
        self.assertEqual(ax.get_title(), "Rise in Sea Level")

        
        self.assertEqual(ax.get_xlabel(), "Year")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)")

        
        lines = ax.get_lines()
        self.assertEqual(len(lines), 2)

if __name__ == "__main__":
    unittest.main()
