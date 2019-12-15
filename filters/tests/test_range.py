from __future__ import absolute_import

import numpy as np
import unittest

from filters import RangeFilter


class RangeTest(unittest.TestCase):
    """ 
    Tests for range filter. 

    scans_a was created with a random floaing point generator with values between -10 and 60.
    res_a is the expected results from the range filter.

    The test takes scans_a and passes it through the range filter, then compares the results to res_a.
    Based on the results the method will return "ok" or "Fail"
    """
    scans_a = [[20.02263683, -3.52923163,  8.40605181, 23.45465361, 19.96296929],
               [47.18566622, 33.87225144, 11.825358  , 43.03164693, -3.42982551],
               [ 5.47945597,  2.01825964, 25.35806176, 41.16256062, 53.86371915],
               [40.91601112, -8.23385735, 48.74555999, 38.66930482, 49.08564674],
               [ 3.85949135, 59.10321848, 54.35039612, 31.28972901, 35.62176336]]

    res_a = [[20.02263683, .03,  8.40605181, 23.45465361, 19.96296929],
            [47.18566622, 33.87225144, 11.825358  , 43.03164693, .03],
            [ 5.47945597,  2.01825964, 25.35806176, 41.16256062, 50.],
            [40.91601112, .03, 48.74555999, 38.66930482, 49.08564674],
            [ 3.85949135, 50., 50., 31.28972901, 35.62176336]]

    def test_scenario_a(self):
        """ 
        Run scans_a through RangeFilter and compare results to res_a
        """
        range_filter =RangeFilter(5, .03, 50)

        for scan, expected_res in zip(self.scans_a, self.res_a):
            range_filter.add_measurement(scan)
            range_filter.update()

            assert np.allclose(expected_res, range_filter.get_measurement()), "Error, value found out of range"

if __name__=='__main__':
    unittest.main()
