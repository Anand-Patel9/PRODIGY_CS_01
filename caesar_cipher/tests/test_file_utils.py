import os
import pytest
import tempfile
from caesar_cipher.file_utils import FileCipher
from caesar_cipher.cipher import CaesarCipher

@pytest.fixture
def sample_files():
    # Setup
    original_content = "Hello World! 123"
    shift = 3
    
    # Create temp files
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as input_file:
        input_file.write(original_content)
        input_path = input_file.name
    
    output_path = input_path + ".enc"
    decrypted_path = input_path + ".dec"
    
    yield original_content, input_path, output_path, decrypted_path, shift
    
    # Teardown
    for path in [input_path, output_path, decrypted_path]:
        if os.path.exists(path):
            os.remove(path)

def test_file_encryption_decryption(sample_files):
    original_content, input_path, output_path, decrypted_path, shift = sample_files
    
    # Test encryption
    FileCipher.encrypt_file(input_path, output_path, shift)
    assert os.path.exists(output_path)
    
    # Verify encrypted content
    with open(output_path, 'r') as f:
        encrypted = f.read()
    cipher = CaesarCipher(shift)
    assert encrypted == cipher.encrypt(original_content)
    
    # Test decryption
    FileCipher.decrypt_file(output_path, decrypted_path, shift)
    assert os.path.exists(decrypted_path)
    
    # Verify decrypted content matches original
    with open(decrypted_path, 'r') as f:
        decrypted = f.read()
    assert decrypted == original_content

def test_file_with_non_ascii(sample_files):
    _, input_path, output_path, decrypted_path, shift = sample_files
    
    # Write non-ASCII content
    with open(input_path, 'w') as f:
        f.write("Héllø Wørld! 123")
    
    # Test roundtrip
    FileCipher.encrypt_file(input_path, output_path, shift)
    FileCipher.decrypt_file(output_path, decrypted_path, shift)
    
    with open(decrypted_path, 'r') as f:
        assert f.read() == "Héllø Wørld! 123"

def test_empty_file(sample_files):
    _, input_path, output_path, decrypted_path, shift = sample_files
    
    # Create empty file
    with open(input_path, 'w') as f:
        pass
    
    FileCipher.encrypt_file(input_path, output_path, shift)
    FileCipher.decrypt_file(output_path, decrypted_path, shift)
    
    with open(decrypted_path, 'r') as f:
        assert f.read() == ""