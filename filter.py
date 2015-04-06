#!/usr/bin/env python


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

class Filter(object):
    """
    Filter object, provides methods to easily construct and simulate 
    a digital filter.
    """
	
    def __init__(self, order, f_sample, f_cutoff):
        """
        Initializes a new filter object with filter coefficients in lists a and b.
        """

        # Input validation:
        if order < 1:
            raise Exception('Invalid filter order, should be >= 1!')

        if f_sample < 0:
            raise Exception('Invalid sample frequency, should be > 0!')
        
        if f_cutoff < 0:
            raise Exception('Invalid cutoff frequency, should be > 0!')

        if f_cutoff > f_sample / 2:
            raise Exception("""Invalid cutoff frequency or sample frequency,
                               f_cutoff should be < f_sample / 2.""")

        # Actual calculation of the filter:
        self.a, self.b = self.calc_coefficients(order, f_sample, f_cutoff)

    def calc_coefficients(self, order, f_sample, f_cutoff):
        """
        Calculates the filter coefficients to achieve the desired frequency
        respons.
        Returns a tuple of the form (a, b):
            - a: array of feedback coefficients of the filter
            - b: array of feedforward coefficients of the filter
        """

        # Calculate normalized frequency instantly (skip conversion f -> w)
        w_pass = f_cutoff / (f_sample / 2)  # f_sample / 2 = f_nyquist
        b, a = signal.butter(order, w_pass, 'low', analog=False)
        return a, b

    def get_a(self):
        """
        Returns the a coefficients of the filter.
        """
        return self.a.tolist()
            
    def get_b(self):
        """
        Returns the b coefficients of the filter.
        """
        return self.b.tolist()

    def step_response(self, n=100):
        """
        Calculates the step response of the filter (n steps, default = 100)
        """
        step = []
        for number in range(0, n):
            step.append(1)

        _times, step_resp = signal.dstep((self.b, self.a, 1), n=n)
        step_response = step_resp[0].flatten()
        return step, step_response

    def impulse_response(self, n=100):
        """
        Calculates the impulse response of the filter (n steps, default = 100)
        """
        impulse = [1]
        for number in range(1, n):
            impulse.append(0)

        _times, imp_resp = signal.dimpulse((self.b, self.a, 1), n=n)
        impulse_response = imp_resp[0].flatten()
        return impulse, impulse_response

    def bode(self):
        """
        Calculates the magnitude response and phase response of a filter.
        Returns a tuple of the form (w_normalized, H_z_dB, phase):
            - w_normalized: all radial frequencies (normalized) 
                            for which H(z) and f(z) have been calculated
            - H(z): frequency response of the filter (in dB)
            - phase: phase response of the filter (in degrees)
        """
        w, H_z = signal.freqz(self.b, self.a)
        w_normalized = w / np.max(w)
        H_z_dB = 20 * np.log10(abs(H_z))
        phase = np.angle(H_z, deg=True)
        return w_normalized, H_z_dB, phase

    def simulate(self, n=100):
        """
        Plots the impulse and step response (n steps, default = 100) of the filter.
        """
        # w is all radial frequencies for which H(z) has been calculated.
        w_normalized, H_z_dB, phase = self.bode()
        step, step_resp = self.step_response(n)
        impulse, imp_resp = self.impulse_response(n)
            
        figure, plots = plt.subplots(2, 2)

        # Plot frequency response:
        ampl_plot = plots[0][0]
        ampl_plot.plot(w_normalized, H_z_dB)
        ampl_plot.set_title('Frequency response')
        ampl_plot.set_xlabel('Normalized frequency (0 .. pi)')
        ampl_plot.set_ylabel('Magnitude (dB)')

        # Plot phase response:
        phase_plot = plots[1][0]
        phase_plot.plot(w_normalized, phase)
        phase_plot.set_title('Frequency response')
        phase_plot.set_xlabel('Normalized frequency (0..pi)')
        phase_plot.set_ylabel('Phase (in °)')

        # Plot impulse response:
        impulse_plot = plots[0][1]
        impulse_plot.plot(impulse)
        impulse_plot.plot(imp_resp)
        impulse_plot.set_title('Impulse response (%d steps)' % n)
        impulse_plot.set_xlabel('Discrete time (n)')
        impulse_plot.set_ylabel('Input / Output')

        # Plot step response:
        step_plot = plots[1][1]
        step_plot.plot(step)
        step_plot.plot(step_resp)
        step_plot.set_title('Step response (%d steps)' % n)
        step_plot.set_xlabel('Discrete time (n)')
        step_plot.set_ylabel('Input / Output')

        for plot_arr in plots:
            for plot in plot_arr:
                plot.grid(which='both', axis='both')

        figure.show()

if __name__ == "__main__":
    print("Starting script to calculate digital filter.")

    # TODO add iir/fiir functionality, 
    # TODO add category (butterworth / chebyshev, ...)
    # TODO add type (lowpass, highpass, bandpass..)
    order = int(input("Order of the filter: "))
    f_sample = float(input("Enter sample rate frequency (in Hz): "))
    f_cutoff = float(input("Enter cutoff frequency (in Hz): "))

    # next line is only useful if you also use buttord along with butter 
    # => higher filter order but stop band is properly defined.
    # stopband_dB = float(input(("Enter desired amplitude in stop band (in Db): "))
            
    f = Filter(order, f_sample, f_cutoff)
    f.simulate(20)

    print("Filter calculated without errors.")
    print("Filter coefficients:")
    print("a: %s" % f.get_a())
    print("b: %s" % f.get_b())
    print()
    input("Press enter to close script..")
