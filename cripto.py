def cesar_cryptography(text):
    encryptedText = ""
    for letter in text:
        index = ord(letter) - ord("A")
        new_character = chr((index + 3) % 26 + ord("A"))
        encryptedText = encryptedText + new_character

    return encryptedText

phrase = input("type some text to be encrypted: ")
phrase = phrase.upper();

print(cesar_cryptography(phrase))