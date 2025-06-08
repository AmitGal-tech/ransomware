import os
import cryptography
from cryptography.fernet import Fernet 
import base64
import getpass

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_files(key, directory):
    f = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f_file:
                file_data = f_file.read()
            
            encrypted_data = f.encrypt(file_data)
            with open(file_path, 'wb') as f_file:
                f_file.write(encrypted_data)

def decrypt_files(key, directory):
    f = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f_file:
                encrypted_data = f_file.read()
            try:
                decrypted_data = f.decrypt(encrypted_data)
                with open(file_path, 'wb') as f_file:
                    f_file.write(decrypted_data)
            except:
                print("Error decrypting file: ", file_path)

def main():
    key = generate_key()
    print("Generated Key: ", key)

    directory = input("Enter directory to encrypt: ")    
    encrypt_files(key, directory)
    print("Files encrypted.")

    password = getpass.getpass("Enter Password to decrypt: ")
    if password == "correct_password": #replace with read one verification
        decrypt_files(key, directory)
        print("Files decrypted")
    else:
        print("Incorrect Password")

if __name__ == "__main__":
    main()
       