# Cryptography Toolkit 

A command-line tool built with Python to learn and practice cryptography concepts.

## About

I built this project to understand how cryptography works in practice.
It covers hashing, encryption, decryption, password management, and file encryption.
Everything runs in the terminal with a simple menu.

## Features

### 1. File Hashing
Hash any file using SHA-256 algorithm.
You give it a file, it gives you a unique fingerprint of that file.

### 2. File Integrity Check
Compare two files to check if they are identical.
It hashes both files and compares the results.
If someone changed even one character, the hashes will be different.

### 3. AES Encryption/Decryption
Encrypt and decrypt messages using AES (Advanced Encryption Standard).
AES is a symmetric algorithm, meaning the same key is used to encrypt and decrypt.

### 4. RSA Encryption/Decryption
Encrypt and decrypt messages using RSA algorithm.
RSA is asymmetric, it uses a public key to encrypt and a private key to decrypt.

### 5. Password Manager
- Check password strength (weak, medium, strong)
- Hash passwords using bcrypt
- Verify a password against its hash

### 6. File Encryption/Decryption
Encrypt entire files using Fernet (AES-128-CBC + HMAC-SHA256).
The key is saved in a separate file.
Without the key, the file cannot be decrypted.

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

Clone the repository:

```bash
git clone https://github.com/abdo-rjx/Encryption-Decryption-project.git
cd Encryption-Decryption-project
