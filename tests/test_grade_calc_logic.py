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


class TestCheckIndex(unittest.TestCase):
    def test_check_index_pd_high_range(self):
        result = kivy_grade_calc.check_index(4.0, kivy_grade_calc.PD_GRADE_RANGE)

        self.assertEqual(50, result)

    def test_check_index_pd_low_range(self):
        result = kivy_grade_calc.check_index(3.5, kivy_grade_calc.PD_GRADE_RANGE)

        self.assertEqual(0, result)

    def test_check_index_p_high_range(self):
        result = kivy_grade_calc.check_index(3.4, kivy_grade_calc.P_GRADE_RANGE)

        self.assertEqual(90, result)

    def test_check_index_p_low_range(self):
        result = kivy_grade_calc.check_index(2.5, kivy_grade_calc.P_GRADE_RANGE)

        self.assertEqual(0, result)

    def test_check_index_bp_high_range(self):
        result = kivy_grade_calc.check_index(2.4, kivy_grade_calc.BP_GRADE_RANGE)

        self.assertEqual(40, result)

    def test_check_index_bp_low_range(self):
        result = kivy_grade_calc.check_index(2, kivy_grade_calc.BP_GRADE_RANGE)

        self.assertEqual(0, result)

    def test_check_index_i_high_range(self):
        result = kivy_grade_calc.check_index(1.9, kivy_grade_calc.I_GRADE_RANGE)

        self.assertEqual(40, result)

    def test_check_index_i_low_range(self):
        result = kivy_grade_calc.check_index(1.5, kivy_grade_calc.I_GRADE_RANGE)

        self.assertEqual(0, result)

    def test_check_index_n_high_range(self):
        result = kivy_grade_calc.check_index(1.4, kivy_grade_calc.N_GRADE_RANGE)

        self.assertEqual(140, result)

    def test_check_index_n_low_range(self):
        result = kivy_grade_calc.check_index(0, kivy_grade_calc.N_GRADE_RANGE)

        self.assertEqual(0, result)


class TestGradeConverter(unittest.TestCase):
    def test_grade_converter_pd_high(self):
        result = kivy_grade_calc.grade_converter(4)

        self.assertEqual(100, result)

    def test_grade_converter_pd_low(self):
        result = kivy_grade_calc.grade_converter(3.5)

        self.assertEqual(92, result)

    def test_grade_converter_p_high(self):
        result = kivy_grade_calc.grade_converter(3.4)

        self.assertEqual(91, result)

    def test_grade_converter_p_low(self):
        result = kivy_grade_calc.grade_converter(2.5)

        self.assertEqual(76, result)

    def test_grade_converter_bp_high(self):
        result = kivy_grade_calc.grade_converter(2.4)

        self.assertEqual(75, result)

    def test_grade_converter_bp_low(self):
        result = kivy_grade_calc.grade_converter(2)

        self.assertEqual(66, result)

    def test_grade_converter_i_high(self):
        result = kivy_grade_calc.grade_converter(1.9)

        self.assertEqual(65, result)

    def test_grade_converter_i_low(self):
        result = kivy_grade_calc.grade_converter(1.5)

        self.assertEqual(55, result)

    def test_grade_converter_n_high(self):
        result = kivy_grade_calc.grade_converter(1.4)

        self.assertEqual(54, result)

    def test_grade_converter_n_low(self):
        result = kivy_grade_calc.grade_converter(0)

        self.assertEqual(0, result)

    def test_grade_converter_error(self):
        result = kivy_grade_calc.grade_converter(4.1)

        self.assertEqual('Grade is out of range', result)


if __name__ == '__main__':
    unittest.main()
