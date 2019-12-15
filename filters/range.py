import numpy as np


class RangeFilter:
    """ 
    Range filter for lidar sensor.

    The range filter crops all the values that are below lower_range (resp. above upper range), 
    and replaces them with the lower_range value (resp. upper_range). 

    Measurements received in lists of N floating point values from Lidar.
    """
    def __init__(self, N, lower_range, upper_range):
        self.N = N
        self.upper_range = upper_range
        self.lower_range = lower_range
        self.measurement = None
            
    def add_measurement(self, measurement):
        """
        Add a new measurement for processing.

        Parameters
        ----------
        measurement - list
            Measurement received from lidar sensor.

        Returns
        -------
        """
        self.measurement = np.array(measurement)   
        self.measurement = self.measurement.reshape(1, self.N)
            
    def update(self):
        """
        Update measurement with filter.

        Parameters
        ----------

        Returns
        -------
        """
        i = 0
        #update the measurement with the filter
        for x in self.measurement.flatten():
            if x < self.lower_range:
                    self.measurement[0, i] = self.lower_range
            if x > self.upper_range:
                    self.measurement[0, i] = self.upper_range
            i = i + 1

    def get_measurement(self):
        """
        Return measurements after processing. 
        
        Parameters
        ----------

        Returns
        -------
        measurement - list
            Value received from range filter.
        """
        return self.measurement

    def _print_res(self):
        """ Print result for debugging. """
        print(self.measurement)
