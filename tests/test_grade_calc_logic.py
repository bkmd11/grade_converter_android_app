import unittest
import kivy_grade_calc


class TestFindAverage(unittest.TestCase):
    def test_find_average_multiple(self):
        result = kivy_grade_calc.find_average([2.1, 3.4, 4, 2, 1.6, 0.4])

        self.assertEqual(2.25, result)

    def test_find_average_single(self):
        result = kivy_grade_calc.find_average([1.3])

        self.assertEqual(1.3, result)


class TestCheckRange(unittest.TestCase):
    def test_check_range(self):
        result = kivy_grade_calc.check_range(3.6)

        self.assertEqual(3.6, result)

    def test_check_range_fails(self):
        result = kivy_grade_calc.check_range(4.1)

        self.assertEqual('4.1 is out of range', result)

    def test_check_range_type_float(self):
        result = kivy_grade_calc.check_range(3.6)

        self.assertIsInstance(result, float)

    def test_check_range_type_string(self):
        result = kivy_grade_calc.check_range(4.1)

        self.assertIsInstance(result, str)


class TestMakeList(unittest.TestCase):
    def test_make_list(self):
        result = kivy_grade_calc.make_list('4.2, 3.4, 4.2')

        self.assertEqual([4.2, 3.4, 4.2], result)


if __name__ == '__main__':
    unittest.main()
