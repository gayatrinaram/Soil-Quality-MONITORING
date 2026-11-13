import unittest
import numpy as np
from src.rgb_index import calculate_rgb_red_blue_index, colourise_index


class RGBIndexTests(unittest.TestCase):
    def test_equal_red_and_blue_returns_zero(self):
        image = np.array([[[100, 20, 100]]], dtype=np.uint8)
        result = calculate_rgb_red_blue_index(image)
        self.assertAlmostEqual(float(result[0, 0]), 0.0, places=6)

    def test_red_dominant_pixel_is_positive(self):
        image = np.array([[[10, 20, 200]]], dtype=np.uint8)
        result = calculate_rgb_red_blue_index(image)
        self.assertGreater(float(result[0, 0]), 0.0)

    def test_blue_dominant_pixel_is_negative(self):
        image = np.array([[[200, 20, 10]]], dtype=np.uint8)
        result = calculate_rgb_red_blue_index(image)
        self.assertLess(float(result[0, 0]), 0.0)

    def test_invalid_shape_raises(self):
        with self.assertRaises(ValueError):
            calculate_rgb_red_blue_index(np.zeros((10, 10), dtype=np.uint8))

    def test_colour_map_has_three_channels(self):
        result = colourise_index(np.zeros((4, 4), dtype=np.float32))
        self.assertEqual(result.shape, (4, 4, 3))


if __name__ == "__main__":
    unittest.main()
