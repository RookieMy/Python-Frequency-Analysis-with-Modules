import freqAnalysis as analysis

def main():
    userInput=input("Metin giriniz: ")
    freq = analysis.calculate_freq(userInput)

    for char in freq:
        totalchars=analysis.lenghtofText(userInput)
        print(f"{char} number of used {freq[char]} - using percentage: {(freq[char]/totalchars)*100}%")

if __name__ == "__main__":
    main()
