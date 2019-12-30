from scipy.io import wavfile
import glob




def main():
    regex = "train/*.wav"
    files = glob.glob(f"./{regex}", recursive=True)
    for f in files:
        print(f)
        fs, data = wavfile.read(f)
        print(fs)
        print(data)
        break


main()