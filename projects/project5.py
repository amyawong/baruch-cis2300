letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']


def mc(symbol):
    symbol = str(symbol).lower()
    morse_code_dict = {}

    for i in range(len(letters)):
        morse_code_dict[letters[i]] = morse_code[i]
    
    translated = ''

    for i in range(len(symbol)):
        if symbol[i] in letters:
            translated += morse_code_dict[symbol[i]] + ' '
        else:
            return None
            
    return translated[:len(translated) - 1]

print(mc('orchids12345'))   # expected: '--- .-. -.-. .... .. -.. ... .---- ..--- ...-- ....- .....', printed: '--- .-. -.-. .... .. -.. ... .---- ..--- ...-- ....- .....'
# print(mc('orchids12345') == '--- .-. -.-. .... .. -.. ... .---- ..--- ...-- ....- .....')     # expected: True, printed: True