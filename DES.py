from pyDes import *

def des_encrypt(key, message):
    k = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_data = k.encrypt(message)
    return encrypted_data

def des_decrypt(key, encrypted_message):
    k = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    decrypted_data = k.decrypt(encrypted_message)
    return decrypted_data

key = input("Enter the encryption key (8 characters long): ")
message = input("Enter the message to encrypt: ")

encrypted_message = des_encrypt(key, message)
print("Encrypted message: ", encrypted_message)

decrypted_message = des_decrypt(key, encrypted_message)
print("Decrypted message: ", decrypted_message)
