import scipy.constants as constants
import scipy.special as special
import pandas as pd
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

class Calculate_EDA:
    def __init__(self, diameter, frequency):
        self.radius = diameter / 2
        self.wave_length = constants.speed_of_light / frequency
        self.k = 2 * constants.pi / self.wave_length

    def a_n(self, n):
        numerator = special.spherical_jn(n, self.k * self.radius)
        divider = self.h_n(n, self.k * self.radius)
        return numerator / divider

    def b_n(self, n):
        numerator = self.k * self.radius * float(special.spherical_jn(n-1, self.k * self.radius)) - n * float(special.spherical_jn(n, self.k * self.radius))
        divider = self.k * self.radius * self.h_n(n-1, self.k * self.radius) - n * self.h_n(n, self.k * self.radius)
        return numerator / divider

    def h_n(self, n, arg):
        return float(special.spherical_jn(n, arg)) + float(special.spherical_yn(n, arg)) * 1j
    
    def result(self):
        coef = self.wave_length * self.wave_length / constants.pi
        series_sum = 0
        for n in range(1, 100):
            series_sum += (-1)**n * (n + 0.5) * (self.b_n(n) * self.a_n(n))
        result = coef * abs(series_sum)**2
        return result


class Write_Result:
    def __init__(self, frequency, wave_length, eda):
        self.len = [x for x in range(1, len(frequency)+1)]
        self.frequency = frequency
        self.wave_length = wave_length
        self.eda = eda

    def write(self, name):
        df = pd.DataFrame({'#': self.len,
                           'freq': self.frequency,
                           'wave_len': self.wave_length,
                           'eda': self.eda})
        df.to_csv(f'{name}.csv', index=False)