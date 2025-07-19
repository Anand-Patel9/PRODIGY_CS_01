class CaesarCipher:
    def __init__(self, shift=3):
        """
        Initialize the cipher with a shift value
        """
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'  
        self.upper_alphabet = self.alphabet.upper()   
        self.shift = shift
    
    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using Caesar Cipher
        """
        ciphertext = []
        for char in plaintext:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.shift) % 26  # Fixed typo aplphabet→alphabet
                ciphertext.append(self.alphabet[index])
            elif char in self.upper_alphabet:
                index = (self.upper_alphabet.index(char) + self.shift) % 26
                ciphertext.append(self.upper_alphabet[index])
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)  # Removed space between quotes and dot
    
    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using Caesar Cipher
        """
        plaintext = []
        for char in ciphertext:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.shift) % 26
                plaintext.append(self.alphabet[index])
            elif char in self.upper_alphabet:
                index = (self.upper_alphabet.index(char) - self.shift) % 26
                plaintext.append(self.upper_alphabet[index])
            else:
                plaintext.append(char)
        return ''.join(plaintext)  # Removed space between quotes and dot