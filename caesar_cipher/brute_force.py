from caesar_cipher.cipher import CaesarCipher

class BruteForce:
    @staticmethod
    def brute_force_decrypt(ciphertext):
        results = []
        for shift in range(1, 26):
            cipher = CaesarCipher(shift)
            decrypted = cipher.decrypt(ciphertext)
            results.append((shift, decrypted))
        return results