from scipy.io import wavfile
import glob
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft




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

        plt.plot(data)
        plt.show()

        signal1 = fft(data)
        signal1 = abs(signal1) / len(data) * 2 
        signal1[0] = 0

        n = len(data)
        freqs = [fq*fs/n for fq in range(int(n))]
        plt.plot(freqs[:10000], signal1[:10000])
        plt.xlabel("Częstotliwość")
        plt.ylabel("Amplituda")
        plt.show()


        ################
        data = signal1[:10000]
        window_array = np.kaiser(len(data), 200)
        signal_kaiser = data * window_array


        plt.plot(signal_kaiser)
        plt.show()

        break


main()