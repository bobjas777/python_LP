parrot="Norwegian Blue"
print(parrot[0:9]+" "+parrot[10:])
print(parrot[::1])
print(parrot[::-1])
print("=========================")
print(" Very simple encryption ")
text_to_encrypt=input("Enter a text to encrypt:  ")
encrypted_text=text_to_encrypt[::-1]
print(f"Encrypted text: {encrypted_text} ")
decrypted_text=encrypted_text[::-1]
if decrypted_text==text_to_encrypt:
    print(f" Decrypted text: {decrypted_text}")
else:
    print("Error during decryption")

