import matplotlib.pyplot as plt


def plot_spectrums(freqs, fft, hps_spectrum):
    """
    Plots the FFT spectrum and HPS spectrum.

    Parameters:
    - freqs (array-like): Array of frequencies.
    - fft (array-like): Array of amplitudes for the FFT spectrum.
    - hps_spectrum (array-like): Array of amplitudes for the HPS spectrum.
    """
    plt.subplot(1, 2, 1)
    plt.plot(freqs, fft)
    plt.title("FFT Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 300)

    plt.subplot(1, 2, 2)
    plt.plot(freqs, hps_spectrum)
    plt.title("HPS Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 300)

    plt.tight_layout()
    plt.show()
