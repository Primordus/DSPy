# DSPy

Very basic script to compute digital filters. Based on scipy, numpy and matplotlib.

## Usage

1. Make sure scipy, matplotlib and numpy are installed
2. Clone this repo: ``` git clone git://github.com/Primordus/DSPy.git ```
3. cd DSPy.git && chmod u+x main.py
4. ./main.py (-h or --help for help menu)
5. Enter desired filter parameters
6. ???
7. Profit!

## Features

- Plots magnitude, phase, step and impulse response once the filter has been calculated.
- Script will also print a list of feedforward (b) and feedback coefficients (a) to easily implement the filter in another language (TODO example!).

Currently supports the following category of filters:

- Lowpass 
- Highpass
- Bandpass
- Bandstop

All filters are currently of type Butterworth. (More types will be added later..)
