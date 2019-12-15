from __future__ import absolute_import

import numpy as np
import unittest

from filters import MedianFilter


class MedianTest(unittest.TestCase):
    """ 
    Tests for median filter. 

    scans_a is the example given in the promp by Brain Corp.
    res_a is the expected results from the median filter provided by Brain Corp.

    scans_b was created with a random floaing point generator with values between .03 and 50.
    res_b is the expected results from the median filter.

    The test takes scans and passes it through the median filter, then compares the results to res.
    Based on the results the method will return "ok" or "Fail"
    """
    scans_a = [[0., 1., 2., 1., 3.],
               [1., 5., 7., 1., 3.],
               [2., 3., 4., 1., 0.],
               [3., 3., 3., 1., 3.],
               [10., 2., 4., 0., 0.]]

    res_a = [[0., 1., 2., 1., 3.],
             [0.5, 3.,  4.5, 1.,  3. ],
             [1., 3., 4., 1., 3.],
             [1.5, 3.,  3.5, 1.,  3. ],
             [2.5, 3.,  4.,  1.,  1.5]]
    
    scans_b = [[20.022, .03,    8.406,  23.454,   19.962],
               [47.185, 33.872, 11.825, 43.031,   .03   ],
               [5.479,  2.018,  25.358, 41.162,   50.   ],
               [40.916, .03,    48.745, 38.669,   49.085],
               [3.859,  50.,    50.,    31.289,   35.621],
               [40.778, 38.852, 19.624, 25.026,   29.782],
               [0.983,  24.859, 9.705,  27.821,   33.474],
               [39.409, 15.441, 32.333, 1.4168,   48.772],
               [37.086, 5.056,  36.830, 2.4577,   32.435],
               [36.980, 4.341,  45.141, 20.9863 , 35.838]]

    res_b = [[20.022,  0.03,  8.406, 23.454, 19.962],
             [33.6035, 16.951,  10.1155, 33.2425,  9.996],
             [20.022,  2.018, 11.825, 41.162, 19.962],
             [30.469,   1.024,  18.5915, 39.9155, 34.5235],
             [20.022,  2.018, 25.358, 38.669, 35.621],
             [30.4,    17.945,  22.491,  34.979,  32.7015],
             [23.1285, 29.3655, 22.491,  34.979,  34.5475],
             [22.444,  20.15,   28.8455, 29.555,  42.1965],
             [38.2475, 20.15,   34.5815, 26.4235, 34.5475],
             [37.033,   20.15,    34.5815,  23.00615, 34.5475 ]]
    
    def test_scenario_a(self):
        """ 
        Run scans_a through RangeFilter and compare results to res_a
        """
        median_filter = MedianFilter(3, 5)

        for scan, expected_res in zip(self.scans_a, self.res_a):
            median_filter.add_measurement(scan)
            median_filter.update()

            assert np.allclose(expected_res, median_filter.get_measurement()), "Error, incorrect median found"

    def test_scenario_b(self):
        """ 
        Run scans_b through RangeFilter and compare results to res_b
        """
        median_filter = MedianFilter(5, 5)

        for scan, expected_res in zip(self.scans_b, self.res_b):
            median_filter.add_measurement(scan)
            median_filter.update()
            assert np.allclose(expected_res, median_filter.get_measurement()), "Error, incorrect median found"
            
if __name__=='__main__':
    unittest.main()
