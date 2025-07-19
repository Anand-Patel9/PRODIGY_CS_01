import pytest
from caesar_cipher.brute_force import BruteForce
from caesar_cipher.cipher import CaesarCipher

@pytest.mark.parametrize("plaintext,shift", [
    ("hello", 3),
    ("WORLD", 10),
    ("Mixed CASE", 7),
    ("With punctuation! 123", 5),
])
def test_brute_force_decrypt(plaintext, shift):
    # Encrypt the plaintext
    from caesar_cipher.cipher import CaesarCipher
    cipher = CaesarCipher(shift)
    encrypted = cipher.encrypt(plaintext)
    
    # Test brute force finds the correct shift
    results = BruteForce.brute_force_decrypt(encrypted)
    
    # Check all shifts are present
    assert len(results) == 25
    
    # Check the correct shift is in results
    shifts = [s for s, _ in results]
    assert shift in shifts
    
    # Check the correct decryption is present
    decrypted_texts = [t for _, t in results]
    assert plaintext in decrypted_texts

def test_brute_force_with_empty_string():
    results = BruteForce.brute_force_decrypt("")
    assert len(results) == 25
    for shift, text in results:
        assert text == ""

def test_brute_force_with_non_alpha():
    test_string = "123!@#"
    results = BruteForce.brute_force_decrypt(test_string)
    for _, text in results:
        assert text == test_string

def test_brute_force_known_phrases():
    common_phrases = [
        ("the quick brown fox", 7),
        ("PYTHON PROGRAMMING", 10),
        ("Caesar Cipher", 15)
    ]
    
    for phrase, shift in common_phrases:
        cipher = CaesarCipher(shift)
        encrypted = cipher.encrypt(phrase)
        results = BruteForce.brute_force_decrypt(encrypted)
        decrypted_texts = [t for _, t in results]
        assert phrase in decrypted_texts