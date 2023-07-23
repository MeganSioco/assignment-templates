'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
        
    mystring = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    current_index = mystring.index(letter)
    shifted_letterindex = (current_index + shift) % 26
    shifted_letter = mystring[shifted_letterindex]
    
    return shifted_letter
    

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    newMessage = []
    for letter in message:
        if letter >= 'A' and letter <= 'Z':
            char = chr((((ord(letter) - 65) + shift) % 26) + 65)
            newMessage.append(char)
        else:
            newMessage.append(letter)
    return ''.join(newMessage)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "

    current_index = ord(letter) - ord("A")
    letter_shift_index = ord(letter_shift) - ord("A")

    shifted_letter_index = (current_index + letter_shift_index) % 26
    shifted_letter = chr(shifted_letter_index + ord("A"))

    return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    stringLen = len(message)
    keyLen = len(key)
    
    ##make key same length as string
    tempKey = key*(stringLen // keyLen + 1)
    key = tempKey[:stringLen+1]
    
    newMessage = []
    for i in range(stringLen):
        if message[i] >= 'A' and message[i] <= 'Z':
            newMessage.append(chr((((ord(message[i])-65) + (ord(key[i])-65))%26)+65))
        else:
            newMessage.append(message[i])
    return ''.join(newMessage)

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shifted_message_list = []
    key_index = 0

    if len(message) % shift == 0:
        for char_index in range(len(message)):
            index = (char_index // shift) + (len(message) // shift) * (char_index % shift)
            shifted_message_list.append(message[index])
            key_index += 1

        ciphered_message = "".join(shifted_message_list)
        return ciphered_message

    if len(message) % shift != 0:
        remainder = len(message) % shift
        num_underscores = shift - remainder
        nonmultiple_message = message + '_' * num_underscores

        for char_index in range(len(nonmultiple_message)):
            index = (char_index // shift) + (len(nonmultiple_message) // shift) * (char_index % shift)
            shifted_message_list.append(nonmultiple_message[index])
            key_index += 1

        ciphered_message = "".join(shifted_message_list)
        return ciphered_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    deciphered_message_list = [''] * len(message)
    key_index = 0

    if len(message) % shift == 0:
        for char in message:
            index = (key_index // shift) + (len(message) // shift) * (key_index % shift) 
            deciphered_message_list[index] = char 
            key_index += 1

        deciphered_message = "".join(deciphered_message_list)
        return deciphered_message

    if len(message) % shift != 0:
        remainder = len(message) % shift
        num_underscores = shift - remainder
        nonmultiple_message = message + '_' * num_underscores

        for index in range(len(nonmultiple_message) - 1):
            index = (key_index // shift) + (len(nonmultiple_message) // shift) * (key_index % shift)
            deciphered_message_list[index] = nonmultiple_message[key_index] 
            key_index += 1

        deciphered_message = "".join(deciphered_message_list)
        return deciphered_message
