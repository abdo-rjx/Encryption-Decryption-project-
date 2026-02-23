from cryptography.fernet import Fernet
import os


def generate_key():
    return Fernet.generate_key()


def save_key(key, key_path="secret.key"):
    with open(key_path, 'wb') as f:
        f.write(key)
    return key_path


def load_key(key_path="secret.key"):
    with open(key_path, 'rb') as f:
        return f.read()


def encrypt_file(file_path):
    if not os.path.exists(file_path):
        return None, None, "File not found!"

    key = generate_key()
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        original_data = file.read()

    original_size = len(original_data)
    encrypted_data = f.encrypt(original_data)

    enc_path = file_path + '.encrypted'
    with open(enc_path, 'wb') as file:
        file.write(encrypted_data)

    key_path = file_path + '.key'
    save_key(key, key_path)

    info = {
        "original_size": f"{original_size} bytes",
        "encrypted_size": f"{len(encrypted_data)} bytes",
        "key_saved_to": key_path,
        "encrypted_file": enc_path
    }

    return key, enc_path, info


def decrypt_file(encrypted_path, key=None, key_path=None):
    if key is None and key_path:
        key = load_key(key_path)
    elif key is None:
        return "No key provided!"

    f = Fernet(key)

    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data)
    except Exception:
        return "Wrong key or corrupted file!"

    dec_path = encrypted_path.replace('.encrypted', '.decrypted')
    with open(dec_path, 'wb') as file:
        file.write(decrypted_data)

    return f"File decrypted: {dec_path}"