# This program consists of 2 functions which cipher and decipher text.
# And it implements the Cesar encryption technique
import string


# ****
# author: Ishan Kashyap
# created: 3/4/2021
# ****


def encrypt(text, key):
    """
    This function implements Cesar encryption to encrypt text
    This function encrypts text
    :param key:
    :type text: str
    """
    # make variable to store cyphered text
    encrypted_text = ""
    # loop through each element in text
    for i in text:
        # if its a letter shift its value
        try:
            # get index of i, shift it, get its mod 26, then find
            # corresponding value and concatenate it to encrypted text
            encrypted_text += letters[(letters.index(i) + key) % len(letters)]
        # other vise don't cipher it
        except ValueError:
            encrypted_text += i
    # finally, return ciphered text
    return encrypted_text


def decrypt(text, key):
    """
    This function is the inverse of the encrypt function. It decrypts
    text using the key that was used to encrypt it.
    :param text: Text to decrypt
    :param key: key that was used to encrypt text
    :return: decrypted text
    """
    decrypted_text = ""
    for i in text:
        try:
            decrypted_text += letters[letters.index(i) - key % len(letters)]
        except ValueError:
            decrypted_text += i
    return decrypted_text


letters = string.ascii_letters
# print(letters)
# print(" ".lower() == " ")
# print("a" < "A")


# print(encrypt("hello", 2))
# print(decrypt(encrypt("Hello! My name is Ishan Kashyap", 5), 5))