from complex_numbers import complex_number
import numpy as np
import matplotlib.pyplot as plt

class complex_function:
    def __init__(self, domain, function):
        self.domain = domain
        self.f = np.array(domain)
        for i in range(domain.shape[0]):
            for j in range(domain.shape[1]):
                self.f[i, j] = function(domain[i, j])
    def __iter__(self):
        pass
    def plot(self):
        pass