import math as m
import numpy as np

ALPHABET = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p',  
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z', '.', ',',
            ' ']

POWER = len(ALPHABET)


def getListFromStr(string):
    return [x for x in string]


def getPlainMatrix(plaintext, key_size):
    matrices = []
    n = m.sqrt(key_size)

    while int( len(plaintext) / key_size ) == 0:
        plaintext.append( ALPHABET[28] )

    for symbol in plaintext:
        row = []
        i = 0

        while i != n:
            row.append( ALPHABET.index(symbol) )
            i += 1
        
        matrices.append(row)

    return matrices


def getKeyMatrix(key):
    n = m.sqrt( len(key) ) # matrix size
    matrix = []

    for value in key:
        row = []
        i = 0
        while i != n:
            row.append( ALPHABET.index(value) )
            i += 1
        matrix.append(row)

    return matrix


def hillEncrypt(plaintext, key):
    key_matrix = getKeyMatrix(key)
    plain_matrix = getPlainMatrix(plaintext, len(key))
    encrypted_text = ''

    for row in plain_matrix:
        mult_matrix = np.dot(row, key_matrix)
        new_matrix = [ x % len(ALPHABET) for x in mult_matrix]
        encrypted_text += ''.join(new_matrix)
        
    return encrypted_text


def hillDecrypted():
    pass


plaintext = ''
key = ''


while True:
    input("Input your text: ", plaintext)
    input("Input your key: ", key)

    if m.sqrt(key) - int(m.sqrt(key)) != 0:
        print("\nError: the length of your key is invalid - it must be a value from which the root can be extracted\n")
    else:
        break

encrypedText = hillEncrypt(plaintext, key)




