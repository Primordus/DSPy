#!/usr/bin/env python


import sys
from dsp_filter import Filter
from band_filter import BandFilter
from filter_builder import FilterBuilder


def arg_defined(arg):
    """
    Checks if the arg is in the list of arguments this script was started with.
    """
    return arg in sys.argv

def show_help():
    """
    Shows the help menu
    """

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

    dsp_filter = FilterBuilder.build()    
    dsp_filter.simulate(20)

    print("Filter calculated without errors.")
    print()
    print("Filter coefficients:")
    print("a: %s" % dsp_filter.get_a())
    print("b: %s" % dsp_filter.get_b())
    print()
    input("Press enter to close script..")
    
    exit()
