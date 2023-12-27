import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import decimate
import sys
import warnings

# from plot_spectrums import plot_spectrums

warnings.filterwarnings("ignore")


def classify_gender(fundamental_freq):
    if fundamental_freq < 160:
        return "M"
    else:
        return "K"


def harmonic_product_spectrum(fft_spectrum, sample_rate, num_harmonics=5):
    """
    Calculates the harmonic product spectrum of a given FFT spectrum.

    Parameters:
    - fft_spectrum (array-like): The input FFT spectrum.
    - sample_rate (int): The sample rate of the audio signal.
    - num_harmonics (int, optional): The number of harmonics to consider. Defaults to 5.

    Returns:
    - hps_spectrum (array-like): The harmonic product spectrum.
    """

    hps_spectrum = fft_spectrum.copy()
    for harmonic in range(2, num_harmonics + 1):
        downsampled_spectrum = decimate(fft_spectrum, harmonic)
        hps_spectrum[: len(downsampled_spectrum)] *= downsampled_spectrum
    return hps_spectrum


def find_fundamental_frequency_hps(hps_spectrum, freqs):
    """
    Finds the fundamental frequency using the Harmonic Product Spectrum (HPS) method.

    Parameters:
    - hps_spectrum (ndarray): The HPS spectrum.
    - freqs (ndarray): The frequency values corresponding to the HPS spectrum.

    Returns:
    - fundamental_freq (float): The fundamental frequency.
    """

    # Filtering out frequencies below 80 Hz
    filtered_freqs = freqs[freqs > 80]
    filtered_hps = hps_spectrum[freqs > 80]
    fundamental_freq_index = np.argmax(filtered_hps)
    fundamental_freq = filtered_freqs[fundamental_freq_index]
    return fundamental_freq


def determine_gender_from_voice(file_path):
    """
    Determines the gender from a given voice file.

    Args:
        file_path (str): The path to the voice file.

    Returns:
        str: The gender classification ('M' for male, 'F' for female, 'K' for unknown/error).
    """

    try:
        sample_rate, data = wav.read(file_path)
        if len(data.shape) == 2:
            data = data.mean(axis=1)

        fft_spectrum = abs(np.fft.rfft(data))
        freqs = np.fft.rfftfreq(len(data), d=1 / sample_rate)
        hps_spectrum = harmonic_product_spectrum(fft_spectrum, sample_rate)

        fundamental_freq = find_fundamental_frequency_hps(hps_spectrum, freqs)
        # print(f"Fundamental frequency: {fundamental_freq:.3f}Hz")

        # plot_spectrums(freqs, fft_spectrum, hps_spectrum)

        return classify_gender(fundamental_freq)

    except Exception as e:
        # print("Error processing file:", e)

        # print K (Woman) if an error occured
        return "K"


def main():
    file_path = sys.argv[1]
    print(determine_gender_from_voice(file_path))


if __name__ == "__main__":
    main()
