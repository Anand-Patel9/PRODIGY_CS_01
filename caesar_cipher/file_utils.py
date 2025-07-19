from caesar_cipher.cipher import CaesarCipher

class FileCipher:
    @staticmethod
    def encrypt_file(input_path, output_path, shift):
        cipher = CaesarCipher(shift)
        with open(input_path, 'r', encoding='utf-8') as f:  # Explicit UTF-8
            content = f.read()
        encrypted = cipher.encrypt(content)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(encrypted)
    
    @staticmethod
    def decrypt_file(input_path, output_path, shift):
        cipher = CaesarCipher(shift)
        with open(input_path, 'r', encoding='utf-8') as f:  # Explicit UTF-8
            content = f.read()
        decrypted = cipher.decrypt(content)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(decrypted)