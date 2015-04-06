from dsp_filter import Filter
from band_filter import BandFilter


class FilterBuilder:
    """
    Class to easily construct a lowpass, highpass, bandpass or bandstop filter.
    """

    @staticmethod
    def build():
        """
        Builds a lowpass, highpass, bandpass or bandstop filter after 
        the user enter specific filter parameters.
        Returns the filter that was created in this function.
        """
        f = None

        # TODO add category (butterworth / chebyshev, ...)
        filter_type = input('Enter type of the filter: ')
        order = int(input('Order of the filter: '))
        f_sample = float(input('Enter samplerate frequency (in Hz): '))
        
        if filter_type in ['bandpass', 'bandstop']:
            f_cutoff1 = float(input('Enter first cutoff frequency (in Hz): '))
            f_cutoff2 = float(input('Enter second cutoff frequency (in Hz): '))
            f_cutoffs = [f_cutoff1, f_cutoff2]

            # next line is only useful if you also use buttord along with butter 
            # => higher filter order but stop band is properly defined.
            # stopband_dB = float(input(('Enter desired amplitude in stop band (in Db): '))

            f = BandFilter(filter_type, order, f_sample, f_cutoffs)
        else:
            f_cutoff = float(input('Enter cutoff frequency (in Hz): '))

            # next line is only useful if you also use buttord along with butter 
            # => higher filter order but stop band is properly defined.
            # stopband_dB = float(input(('Enter desired amplitude in stop band (in Db): '))

            f = Filter(filter_type, order, f_sample, f_cutoff)

        return f 
