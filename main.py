#!/usr/bin/env python


import sys
from dsp_filter import Filter
from band_filter import BandFilter


def arg_defined(arg):
    return arg in sys.argv

def show_help():
    print('USAGE: ./main.py [FLAGS]')
    print()
    print('Possible FLAGS:')
    print('-h or --help --> shows this help menu.')
    print()
    print('Type of the filter: "low", "high", "bandpass", "bandstop"')
    print('Order: integer, >= 1.')
    print('Samplerate frequency: float, > 0.0 Hz.')
    print('Cutoff frequency: float, 0.0 Hz < f_cutoff < f_sample / 2.')
    print()

if __name__ == "__main__":
    if arg_defined("-h") or arg_defined("--help"):
        show_help()
        exit()

    print("Starting script to calculate digital filter.")
    f = None

    # TODO add category (butterworth / chebyshev, ...)
    filter_type = input("Enter type of the filter: ")
    order = int(input("Order of the filter: "))
    f_sample = float(input("Enter samplerate frequency (in Hz): "))
    
    # TODO refactor this part later.
    if filter_type in ['bandpass', 'bandstop']:
        f_cutoff1 = float(input("Enter first cutoff frequency (in Hz): "))
        f_cutoff2 = float(input("Enter second cutoff frequency (in Hz): "))
        f_cutoffs = [f_cutoff1, f_cutoff2]

        # next line is only useful if you also use buttord along with butter 
        # => higher filter order but stop band is properly defined.
        # stopband_dB = float(input(("Enter desired amplitude in stop band (in Db): "))

        f = BandFilter(filter_type, order, f_sample, f_cutoffs)
    else:
        f_cutoff = float(input("Enter cutoff frequency (in Hz): "))

        # next line is only useful if you also use buttord along with butter 
        # => higher filter order but stop band is properly defined.
        # stopband_dB = float(input(("Enter desired amplitude in stop band (in Db): "))

        f = Filter(filter_type, order, f_sample, f_cutoff)
    
    f.simulate(20)

    print("Filter calculated without errors.")
    print()
    print("Filter coefficients:")
    print("a: %s" % f.get_a())
    print("b: %s" % f.get_b())
    print()
    input("Press enter to close script..")
    
    exit()
