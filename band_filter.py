from dsp_filter import Filter
from scipy import signal

class BandFilter(Filter):
    """
    Bandpass filter object, provides methods to easily construct and simulate
    a digital bandpass or bandstop (notch) filter.
    """

    def __init__(self, filter_type, order, f_sample, f_cutoffs):
        """
        Initializes a new bandpass or bandstop filter object with 
        filter coefficients in lists a and b.
        """

        # Input validation:
        if filter_type not in ['bandpass', 'bandstop']:
            raise Exception('Invalid type, expected "bandpass" or "bandstop.')
        
        if order < 1:
            raise Exception('Invalid filter order, should be >= 1!')

        if f_sample < 0:
            raise Exception('Invalid sample frequency, should be > 0!')
        
        if len(f_cutoffs) != 2:
            raise Exception('Expected 2 cutoff frequencies.')
        
        if f_cutoffs[0] > f_cutoffs[1]:
            raise Exception("""First cutoff frequency should be 
                                smaller than the second""")

        for f_cutoff in f_cutoffs:
            if f_cutoff > f_sample / 2:
                raise Exception("""Invalid cutoff frequency or sample frequency,
                                   f_cutoff should be < f_sample / 2.""")

        # Actual calculation of the filter:
        self.filter_type = filter_type
        self.a, self.b = self.calc_coefficients(order, f_sample, f_cutoffs)

    def calc_coefficients(self, order, f_sample, f_cutoffs):
        """
        Calculates the filter coefficients to achieve the desired frequency
        respons.
        Returns a tuple of the form (a, b):
            - a: array of feedback coefficients of the filter
            - b: array of feedforward coefficients of the filter
        """

        w_pass = []
        for f_cutoff in f_cutoffs:
            # Calculate normalized frequency instantly (skip conversion f -> w)
            w_pass.append(f_cutoff / (f_sample / 2))  # f_sample / 2 = f_nyquist

        # TODO add buttord here if stopband_dB is specified
        b, a = signal.butter(order, w_pass, self.filter_type, analog=False)
        return a, b
