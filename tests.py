import unittest

import day1.problem1 as day1_problem1
import day1.problem2 as day1_problem2
import day2.problem1 as day2_problem1
import day2.problem2 as day2_problem2

class Advent2019Tests(unittest.TestCase):
    def test_day1_problem1(self):
        f = open("day1/input1.txt")
        contents = f.read()
        f.close()
        
        arr = list(map(int, contents.split('\n')[:-1]))
        ans = day1_problem1.solve(arr)
        self.assertEqual(ans, 3268951)
    
    def test_day1_problem2(self):
        f = open("day1/input2.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split('\n')[:-1]))
        ans = day1_problem2.solve(arr)
        self.assertEqual(ans, 4900568)
        
    def test_day2_problem1(self):
        f = open("day2/input1.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        ans = day2_problem1.solve(arr)
        self.assertEqual(ans, 6568671)

    def test_day2_problem2(self):
        f = open("day2/input2.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        # ans = day2_problem2.solve(arr)

if __name__ == "__main__":
    unittest.main()