'''
/*=============================================================================
| pa01 - Encrypting a plaintext file using the Vigenere cipher
|
| Author: Faramarz Aboutalebi
| Language: python
|
| To Compile: 
|
| To Execute: python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
|
| Note: All input files are simple 8 bit ASCII input
|
|Security in Computing
+=============================================================================*/
'''

import sys
import numpy as np

# Read key file
key_file = open(sys.argv[1], 'r')
n = int(key_file.readline())
key_matrix = np.zeros((n, n), dtype=int)
for i in range(n):
    row = key_file.readline().split()
    for j in range(n):
        key_matrix[i][j] = int(row[j])
key_file.close()

# Read plaintext file
plaintext_file = open(sys.argv[2], 'r')
plaintext = ""
for line in plaintext_file:
    for char in line:
        if char.isalpha() and char.isascii():
            plaintext += char.lower()
plaintext_file.close()

plaintext_len = len(plaintext)
block_size = n
if plaintext_len % block_size != 0:
    plaintext += 'x' * (block_size - plaintext_len % block_size)
plaintext_len = len(plaintext)
plaintext_blocks = [plaintext[i:i+block_size] for i in range(0, plaintext_len, block_size)]

# Encrypt plaintext blocks
ciphertext = ""
for block in plaintext_blocks:
    block_vec = np.zeros((block_size, 1), dtype=int)
    for i in range(block_size):
        block_vec[i][0] = ord(block[i]) - 97
    encrypted_vec = np.matmul(key_matrix, block_vec) % 26
    for i in range(block_size):
        ciphertext += chr(encrypted_vec[i][0] + 65)

# Output results
print("\nKey matrix:")
for i, row in enumerate(key_matrix):
    print(" ", end="")
    for j, cell in enumerate(row):
        if int(len(str(cell))) == 1:
            print(f"  {cell} ", end="")
        else:
            print(f" {cell} ", end="")
    print()
print("\nPlaintext:")
#print(plaintext)

for i in range(0, len(plaintext), 80):
    print(plaintext[i:i+80].lower())
print()
print("Ciphertext:")
for i in range(0, len(ciphertext), 80):
    print(ciphertext[i:i+80].lower())

