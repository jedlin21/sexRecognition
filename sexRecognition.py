from scipy.io import wavfile
import glob
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from scipy import signal



def main():
    regex = "train/*.wav"
    files = glob.glob(f"./{regex}", recursive=True)
    for f in files:
        print(f)
        fs, data = wavfile.read(f)
        print(len(data))
        data = data[ int(len(data)*0.1) : int(len(data)*0.9) ] #cut ends of the signal to avoid interference
        print(len(data))
        print(fs)
        print(data)

        # plt.plot(data)
        # plt.show()

        signal1 = fft(data)
        signal1 = abs(signal1) / len(data) * 2 
        signal1[0] = 0

        n = len(data)
        freqs = [fq*fs/n for fq in range(int(n))]
        plt.plot(freqs[:10000], signal1[:10000])
        plt.xlabel("Częstotliwość")
        plt.ylabel("Amplituda")
        #plt.show()

        ################
        N = 10000
        data = signal1[:N]
        freqs = freqs[:N]
        window_array = np.kaiser(len(data), 500)
        signal_kaiser = np.convolve(data, window_array, mode='same') / sum(window_array)

        plt.plot(freqs, signal_kaiser)
        plt.show()

        maxIndex = np.argmax(signal_kaiser)

        print(len(signal1))
        print(len(freqs))
        print(f"Max amplitude at: {freqs[maxIndex]}")

        break


main()