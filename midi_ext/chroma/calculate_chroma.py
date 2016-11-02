import os
import numpy as np
import pretty_midi

import matplotlib.pyplot as plt


def calculate_chroma(self, midi_file):
    # get midi information from pretty_midi
    midi = pretty_midi.PrettyMIDI(midi_file)
    # chroma matrix - the energy in each semitone across octaves
    chroma_midi = midi.get_chroma(times=np.arange(0, midi.get_end_time(), 1 / 25.0))
    ## 0.04sec

    # normalize chroma_matrix columnwise by max
    chroma_midi /= (chroma_midi.max(axis=0) + (chroma_midi.max(axis=0) == 0))

    return chroma_midi