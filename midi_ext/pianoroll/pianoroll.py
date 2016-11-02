import os
import numpy as np
import pretty_midi

import matplotlib.pyplot as plt


## need to check instrument number first
def pianoroll(self, midi_file, instrument):
    midi = pretty_midi.PrettyMIDI(midi_file)
    option = instrument  ## need to fix
    m = midi.instruments[option].get_piano_roll(fs=100)

    return m