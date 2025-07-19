from caesar_cipher.cipher import CaesarCipher

class FileCipher:
    @staticmethod
    def encrypt_file(input_path, output_path, shift):
        cipher = CaesarCipher(shift)  # Fixed: Added parentheses with shift
        with open(input_path, 'r') as f:
            content = f.read()
        encrypted = cipher.encrypt(content)
        with open(output_path, 'w') as f:
            f.write(encrypted)
    
    @staticmethod
    def decrypt_file(input_path, output_path, shift):
        cipher = CaesarCipher(shift)  # Fixed: Added parentheses with shift
        with open(input_path, 'r') as f:
            content = f.read()
        decrypted = cipher.decrypt(content)
        with open(output_path, 'w') as f:
            f.write(decrypted)