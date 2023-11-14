import tkinter as tk

def caesar_encrypt():
    plaintext = entry_plaintext.get()
    shift = int(entry_shift.get())
    ciphertext = ""
    for char in plaintext:
        encrypted_char = (ord(char) + shift) % 256
        ciphertext += chr(encrypted_char)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(tk.END, ciphertext)

def caesar_decrypt():
    ciphertext = entry_ciphertext.get()
    shift = int(entry_shift.get())
    plaintext = ""
    for char in ciphertext:
        decrypted_char = (ord(char) - shift) % 256
        plaintext += chr(decrypted_char)
    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(tk.END, plaintext)

# Membuat window aplikasi
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("300x200")

# Membuat label dan entry untuk plaintext
label_plaintext = tk.Label(window, text="Plaintext:")
label_plaintext.pack()
entry_plaintext = tk.Entry(window)
entry_plaintext.pack()

# Membuat label dan entry untuk ciphertext
label_ciphertext = tk.Label(window, text="Ciphertext:")
label_ciphertext.pack()
entry_ciphertext = tk.Entry(window)
entry_ciphertext.pack()

# Membuat label dan entry untuk jumlah geser
label_shift = tk.Label(window, text="Jumlah Geser:")
label_shift.pack()
entry_shift = tk.Entry(window)
entry_shift.pack()

# Membuat tombol untuk enkripsi dan dekripsi
button_encrypt = tk.Button(window, text="Enkripsi", command=caesar_encrypt)
button_encrypt.pack()
button_decrypt = tk.Button(window, text="Dekripsi", command=caesar_decrypt)
button_decrypt.pack()

# Menjalankan aplikasi
window.mainloop()