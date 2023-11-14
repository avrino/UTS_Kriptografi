import base64

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk enkripsi dan encoding pesan
def encrypt_message(message, shift):
    encrypted = caesar_cipher_encrypt(message, shift)
    encoded_message = base64.b64encode(encrypted.encode()).decode()
    return encoded_message

# Fungsi untuk dekripsi dan decoding pesan
def decrypt_message(encoded_message, shift):
    decoded_message = base64.b64decode(encoded_message).decode()
    decrypted = caesar_cipher_encrypt(decoded_message, -shift)
    return decrypted

# Pesan yang ingin dikirim
pesan_asli = "Avrino Hanggoro Saputra"

# Geseran (shift) untuk Caesar Cipher
geseran = 15

# Enkripsi pesan
pesan_terenkripsi = encrypt_message(pesan_asli, geseran)
print("Pesan terenkripsi:", pesan_terenkripsi)

# Dekripsi pesan
pesan_terdekripsi = decrypt_message(pesan_terenkripsi, geseran)
print("Pesan terdekripsi:", pesan_terdekripsi)