import os
import numpy as np
import pretty_midi

import matplotlib.pyplot as plt


def chroma_energy_han(self):
    ## CENS_midi_hann

    CENS_midi_hann = np.zeros(tuple(CENS_midi.shape[0:2]))

    for i in range(12):
        for j in np.arange(0, CENS_midi.shape[1], 41):
            CENS_midi_hann[i, j:j + 41] = np.convolve(CENS_midi[i, j:j + 41],
                                                      np.hanning(41)[0:CENS_midi[i, j:j + 41].shape[0]], 'same')

    CENS_midi_hann /= np.linalg.norm(CENS_midi_hann, 2, axis=0)
    CENS_midi_hann = np.nan_to_num(CENS_midi_hann)

    return CENS_midi_hann