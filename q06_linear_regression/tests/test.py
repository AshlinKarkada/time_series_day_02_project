import unittest
from inspect import getfullargspec
from ..build import q06_linear_regression as student
from greyatomlib.time_series_day_02_project.q06_linear_regression.build import q06_linear_regression as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal

fe =  ["WorkDay", "Peakhours", "Peakmonths"]

class Testing(unittest.TestCase):
    def setUp(self):
        with open('q06_linear_regression/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q06_linear_regression/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q06_linear_regression/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q06_linear_regression/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/elecdemand.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_timeseries(self):
        # Input parameters tests
        args = getfullargspec(student)
        self.assertEqual(len(args[0]), 3, "Expected argument(s) %d, Given %d" % (3, len(args)))

    def test_timeseries_default(self):
        args = getfullargspec(student)
        self.assertEqual(args[3], (fe,9), "Expected default values do not match given default values")
    
    def test_return(self):
        self.assertEqual(self.student_return, self.original_return, "The return values do not match expected values")

