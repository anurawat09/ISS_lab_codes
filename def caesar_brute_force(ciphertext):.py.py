def caesar_brute_force(ciphertext):
    print("Trying all possible keys for Caesar Cipher:")
    for key in range(26):
        decrypted = ''
        for char in ciphertext:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - shift - key) % 26 + shift)
            else:
                decrypted += char
        print(f'Key {key}: {decrypted}')


cipher = "Wklv lv d whvw phvvdjh"  
caesar_brute_force(cipher)
