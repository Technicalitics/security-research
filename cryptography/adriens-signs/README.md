# Cryptography Foundations: Decrypting an Algorithm Using Modular Arithmetic

**Lab Covered:** Modular Arithmetic - Adrien's Signs  
**Platform:** CryptoHack [(Link)](https://cryptohack.org/courses/modular/adrien/)  
**Date Completed:** December 26, 2025  
**Tools Used:** Python 3, Jupyter Notebook, PyCryptodome

## Executive Summary
This repository contains a detailed cryptanalysis of the "Adrien's Signs" challenge from CryptoHack. The encryption scheme uses modular arithmetic and quadratic residues to encrypt bits, and by analyzing the algorithm, we can recover the plaintext message.  
The goal of this project is to demonstrate the method of breaking the encryption by leveraging **Euler's Criterion** and exploiting the **quadratic residue** property of the modulus to decrypt ciphertext without needing the secret key.

## Problem Overview
This lab provides an encryption algorithm in python, and an `output.txt` file that is the result of encrypting some string (which will be the solution).   
In the python file, I discovered that many of the inputs are public, including `a` and `p`. The `output.txt` file provided the result from this encryption scheme, which I named the `encrypted_flag`. The goal of this lab is to recover the string that was encrypted with the provided algorithm, and produced the result in `output.txt`

## Understanding The Encryption Scheme
### Bit-level Encoding
Each character of the flag is converted to its 8-bit ASCII representation. For example: 
   - `'A'` is represented as `65` in decimal, which converts to `01000001` in binary.

### Converting Bits to Ciphertext
After converting the characters to bits, the algorithm then performs the following operations for each bit:
- Chooses a random exponent `e`
- Calculates `n`, which is equal to `a^e mod p`
- If the bit is 1, output `n`
- If the bit is 0, output `-n mod p`

The last two steps of this algorithm means that each element of the ciphertext is either:
1. A value of the form `a^e mod p`, or
2. its modular negation  
This observation is key to cracking this lab.

## Key Mathematical Observation
### Why Quadratic Residues Matter
The `p` value used in the algorithm is prime. If we take a look at Fermat's Little Theorem/Euler's Criterion, Euler's Criterion states that for a prime `p` and an integer `a`:  
`a^(p-1)/2 ≡ 1 (mod p)` if `a` is a quadratic residue mod `p`  
`a^(p-1)/2 ≡ -1 (mod p)` if `a` is a quadratic non-residue mod `p`

We can connect this to the lab by observing that:
- `a^e mod p` is always a quadratic residue. Since `a` was chosen to be a quadratic residue modulo `p`, any power `a^e` is also a quadratic residue
- `-a^e mod p` is a **non-residue** (Because the provided prime satisfies `p ≡ 3 (mod 4)`, `−1` is a quadratic non-residue modulo `p`)

This means that *even after the bits are encrypted* with this algorithm, we have a method of determining if the bit was a 1 or a 0, because they were encrypted differently based on their value.

## Breaking the Encryption
**Step 1:** For each ciphertext element `c`, compute `pow(c, (p-1)//2, p)`  
**Step 2:** If the result is 1, the bit was 1. If the result is p-1, the bit was 0.

**Important Note:** The randomness provided by `e` does not matter. The quadratic residuosity depends only on the sign of the value, not on the exponent.

**Step 3:** Reconstruct the flag by joining the recovered bits into a binary string, converting binary to integer, integer to bytes, and then decoding as ASCII text.

## Final Solve Script
The following Python code demonstrates how to break the encryption and recover the original plaintext flag.  
```python
from Crypto.Util.number import long_to_bytes

bits = []
# decrypt each element of the encrypted_flag
for c in encrypted_flag:
    bits.append(str(int(pow(c, (p-1)//2, p) == 1)))

# reconstruct the flag
binary = ''.join(bits)
flag = long_to_bytes(int(binary, 2))
print(flag.decode())
```

## Takeaways
- Bitwise encryption is dangerous if bits leak structural information
- Randomness does not guarantee security
- Quadratic residuosity can distinguish values modulo a prime
- Sign information modulo `p` is often exploitable
