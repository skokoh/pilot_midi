import os
import numpy as np
import pretty_midi

import matplotlib.pyplot as plt


def chroma_energy(self):
    ## chroma energy distribution

    chroma_midi_norm = chroma_midi / np.sum(chroma_midi, axis=0)
    chroma_midi_norm = np.nan_to_num(chroma_midi_norm)

    CENS_midi = np.zeros(tuple(chroma_midi.shape[0:2]))

    CENS_midi[np.where(chroma_midi_norm > 0.4)] = 4
    CENS_midi[np.where((chroma_midi_norm >= 0.2) & (chroma_midi_norm <= 0.4))] = 3
    CENS_midi[np.where((chroma_midi_norm >= 0.1) & (chroma_midi_norm < 0.2))] = 2
    CENS_midi[np.where((chroma_midi_norm >= 0.05) & (chroma_midi_norm < 0.1))] = 1
    CENS_midi[np.where(chroma_midi_norm < 0.05)] = 0

    return CENS_midi