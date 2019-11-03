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

    def test_fibonacci(self):
        fibonacci_ = fibonacci(5)
        a, b = 0, 1
        for _ in range(1, 5):
            a, b = b, b + a
        self.assertEqual(fibonacci_, (a,b))

    def test_linear_sum(self):
        sequence = [_ for _ in range(100)]
        self.assertEqual(linear_sum(sequence, 10), sum(sequence[:10]))

    def test_reverse(self):
        n = 20
        sequence = [_ for _ in range(100)]
        reversed_nth = sequence[n-1:0:-1] #reversing using slicing
        function_reversed_nth = reverse(sequence, 1, n)[1:n] #slicing only reversed part
        self.assertEqual(function_reversed_nth, reversed_nth)

    def test_power(self):
        self.assertEqual(power(3,5), pow(3,5))

    def test_power_(self):
        self.assertEqual(power_(3, 5), pow(3,5))

    def test_binary_sum(self):
        sequence = [_ for _ in range(100)]
        self.assertEqual(binary_sum(sequence, 1, 20), sum(sequence[1:20]))

if __name__ == "__main__":
    unittest.main()
