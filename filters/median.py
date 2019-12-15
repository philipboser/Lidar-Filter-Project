import numpy as np


class MedianFilter:
    """
    Median filter for lidar sensor

    The median filter returns the median of the current and the previous D scans:
    
    y(t) = median(x(t), x(t-1), ..., x(t-D))

    x is the input from the lidar in form of a list of N floating point values and y is the output. 
    D and N must be given when creating a new median filter and are subsequently fixed values.
    """
    def __init__(self, D, N):
        self.memory = np.empty([0,N])
        self.D = D
        self.N = N
        self.measurement = None
            
    def add_measurement(self, measurement):
        """
        Add a new measurement to memory and
        delete an old one if needed (based on D).

        Parameters
        ----------
        measurement - list
            Measurement rceived from lidar sensor.

        Returns
        -------
        """
        self.measurement = np.array(measurement)   
        self.measurement = self.measurement.reshape(1, self.N)
        
        #Add measurement to memory of size D
        if self.memory.shape[0] < self.D + 1:
            self.memory = np.append(self.memory, self.measurement, axis=0)
        else:
            self.memory = np.delete(self.memory, 0, axis=0)
            self.memory = np.append(self.memory, self.measurement, axis=0)

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
        for x in self.memory[0].flatten():
            self.measurement[0, i] = np.median(self.memory[:, i])
            i = i + 1

    def get_measurement(self):
        """
        Return measurements after processing. 
        
        Parameters
        ----------

        Returns
        -------
        measurement - list
            Value received from median filter.
        """
        return self.measurement

    def _print_res(self):
        """ Print result for debugging. """
        print(self.measurement)
