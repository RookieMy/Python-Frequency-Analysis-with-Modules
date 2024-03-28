def isLetter(char):
    return 'a'<= char <= 'z' or 'A' <= 'Z' or 'ç' <= char <= 'ü' or 'Ç' <= char <= "Ü"

def toLower(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char)+32)
    elif 'Ç'<= char <='Ü':
        turkishcharstolower={'Ç': 'ç', 'Ğ': 'ğ', 'İ': 'i', 'I': 'ı', 'Ö': 'ö', 'Ş': 'ş', 'Ü': 'ü'}
        return turkishcharstolower[char]
    else:
        return char

def lenghtofText(text):
    lenghtoftext=0.00
    for char in text:
        lenghtoftext+=1

    return lenghtoftext

def calculate_freq(text):
    freq = {char: 0 for char in 'abcçdefgğhıijklmnoöprsştuüvyz'}
    total_letters = 0
    
    for char in text:
        if isLetter(char):
            charLower=toLower(char)
            if charLower in freq:
                freq[charLower]+=1
                total_letters+=1

    total_letters=max(total_letters,1)

    return {char: freq[toLower(char)] / total_letters for char in freq}