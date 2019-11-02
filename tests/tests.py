import unittest
from random import randint
from recursion import *


class TestCases(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120, '5! should be 120')

    def test_binary_search(self):
        data = sorted(set([randint(1, 100) for x in range(50)]))
        target = data[randint(0, len(data)-1)]
        self.assertEqual(binary_search(
            data, target, 0, len(data)), True)

    def test_disk_usage(self):
        import os
        import re
        import subprocess
        # get  disk_usage_size using funtion
        current_path = os.getcwd()
        disk_usage_size = disk_usage(current_path)/1000
        # get summary of current path from console/terminal
        console_report = str(subprocess.run(
            f"du -sx '{current_path}'", shell=True, capture_output=True))
        reported_size = re.search(
            r'stdout=b\'(\d+)', console_report).groups()[0]
        reported_size = int(reported_size)
        # compare values
        self.assertAlmostEqual(disk_usage_size, reported_size, delta=2)


if __name__ == "__main__":
    unittest.main()
