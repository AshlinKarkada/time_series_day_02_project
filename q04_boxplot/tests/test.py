import unittest
from inspect import getfullargspec
from ..build import q04_boxplot as student
from greyatomlib.time_series_day_02_project.q04_boxplot.build import q04_boxplot as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('q04_boxplot/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q04_boxplot/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q04_boxplot/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q04_boxplot/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/elecdemand.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_timeseries(self):
        # Input parameters tests
        args = getfullargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))

    def test_series_default(self):
        args = getfullargspec(student)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")
    
