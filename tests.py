import unittest

import day1.problem1 as day1_problem1
import day1.problem2 as day1_problem2
import day2.problem1 as day2_problem1
import day2.problem2 as day2_problem2
import day3.problem1 as day3_problem1
import day3.problem2 as day3_problem2
import day4.problem1 as day4_problem1
import day4.problem2 as day4_problem2
import day5.problem1 as day5_problem1
import day5.problem2 as day5_problem2

class Advent2019Tests(unittest.TestCase):
    def test_day1_problem1(self):
        f = open("day1/input.txt")
        contents = f.read()
        f.close()
        
        arr = list(map(int, contents.split('\n')[:-1]))
        ans = day1_problem1.solve(arr)
        self.assertEqual(ans, 3268951)
    
    def test_day1_problem2(self):
        f = open("day1/input.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split('\n')[:-1]))
        ans = day1_problem2.solve(arr)
        self.assertEqual(ans, 4900568)
        
    def test_day2_problem1(self):
        f = open("day2/input.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        ans = day2_problem1.solve(arr)
        self.assertEqual(ans, 6568671)

    def test_day2_problem2(self):
        f = open("day2/input.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        ans = day2_problem2.solve(arr, 19690720)
        self.assertEqual(ans, 3951)

    def test_day3_problem1(self):
        f = open("day3/input.txt")
        contents = f.read()
        f.close()
        
        paths = [x.split(',') for x in contents.split('\n')]
        ans = day3_problem1.solve(paths[0], paths[1])
        self.assertEqual(ans, 1017)

    def test_day3_problem2(self):
        f = open("day3/input.txt")
        contents = f.read()
        f.close()

        paths = [x.split(',') for x in contents.split('\n')]
        ans = day3_problem2.solve(paths[0], paths[1])
        self.assertEqual(ans, 11432)

    def test_day4_problem1(self):
        f = open("day4/input.txt")
        contents = f.read()
        f.close()
    
        prange = list(map(int, contents.split('-')))
        ans = day4_problem1.solve(prange)
        self.assertEqual(ans, 579)

    def test_day4_problem2(self):
        f = open("day4/input.txt")
        contents = f.read()
        f.close()
    
        prange = list(map(int, contents.split('-')))
        ans = day4_problem2.solve(prange)
        self.assertEqual(ans, 358)

    def test_day5_problem1(self):
        f = open("day5/input.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        ans = day5_problem1.solve(arr, 1)
        self.assertEqual(ans, 15259545)

    def test_day5_problem2(self):
        f = open("day5/input.txt")
        contents = f.read()
        f.close()

        arr = list(map(int, contents.split(',')))
        ans = day5_problem2.solve(arr, 5)
        self.assertEqual(ans, 7616021)

if __name__ == "__main__":
    unittest.main()
