import unittest
from caesar_cipher.cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(shift=3)

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("hello"), "khoor")
        self.assertEqual(self.cipher.encrypt("HELLO"), "KHOOR")
        self.assertEqual(self.cipher.encrypt("Hello, World!"), "Khoor, Zruog!")

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("khoor"), "hello")
        self.assertEqual(self.cipher.decrypt("KHOOR"), "HELLO")
        self.assertEqual(self.cipher.decrypt("Khoor, Zruog!"), "Hello, World!")

    def test_edge_cases(self):
        self.assertEqual(self.cipher.encrypt("xyz"), "abc")
        self.assertEqual(self.cipher.decrypt("abc"), "xyz")
        self.assertEqual(self.cipher.encrypt("123!@#"), "123!@#")

if __name__ == "__main__":
    unittest.main()