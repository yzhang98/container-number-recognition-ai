import unittest
from pathlib import Path
import re

class TestCroppingCode(unittest.TestCase):
    def test_get_ctnr_color_from_byte_indices(self):
        text = Path('main.py').read_text()
        pattern_y = re.compile(r"max\(0, crop_zone\[1\] - 100\): min\(crop_zone\[3\] \+ 100,\s*img_np.shape\[0\]\)")
        pattern_x = re.compile(r"max\(0, crop_zone\[0\] - 100\): min\(crop_zone\[2\] \+ 100,\s*img_np.shape\[1\]\)")
        self.assertRegex(text, pattern_y)
        self.assertRegex(text, pattern_x)

    def test_main_block_indices(self):
        text = Path('main.py').read_text()
        pattern_y = re.compile(r"max\(0, res\[\"bounding_box\"\]\[1\] - 100\): min\(res\[\"bounding_box\"\]\[3\] \+ 100,\s*input_img.shape\[0\]\)")
        pattern_x = re.compile(r"max\(0, res\[\"bounding_box\"\]\[0\] - 100\): min\(res\[\"bounding_box\"\]\[2\] \+ 100,\s*input_img.shape\[1\]\)")
        self.assertRegex(text, pattern_y)
        self.assertRegex(text, pattern_x)

if __name__ == '__main__':
    unittest.main()
