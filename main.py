import odev2_freqanalysis as analysis

def main():
    userInput=input("Metin giriniz: ")
    frequency_percentages = analysis.calculate_freq(userInput)

    for char, percentage in frequency_percentages.items():
        numberofused=int(percentage*analysis.lenghtofText(userInput))
        print(f"{char} number of used {numberofused} - using percentage: {percentage:.2%}")

if __name__ == "__main__":
    main()
