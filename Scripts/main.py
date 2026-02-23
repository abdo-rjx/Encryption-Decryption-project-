from modules.encryption import aes_ed, rsa_ed
from modules.hash import hash_file, verify_integrity
from modules.FileEncryption import encrypt_file, decrypt_file
from modules.password  import check_stength, hash_pw, verify_password
from getpass import getpass
def menu ():
    print("\n select an option")
    print("1. hash file ")
    print("2. check file integrity ")
    print("3. AES Encrypt/Decrypt")
    print("4. RSA Encrypt/Decrypt")
    print("5. password Managger")
    print("6. File Encryption/Decryption")
    print("0. Exit")

print("welcome to my ode i write it to learn more about cryptographhy ")

while True:
    menu()
    choice = input("Einter choince (0-6) :")
    if choice == "0":
        break
    elif choice == "1":
        file_path = input("input file path 1 :")
        print("\n hash of file is : ", hash_file(file_path))
    elif choice == "2":
        file_path1 = input("enter the file path 1:")
        file_path2 = input("enter the file path 2:")
        print (verify_integrity(file_path1,file_path2))
    elif choice == "3":
        message = input("enter message : ")
        key, ciphertext , plaintext = aes_ed(message)
        print("AES key : ", key)
        print("AES ciphertext ", ciphertext)
        print("AES plaintext ", plaintext)
    elif choice == "4":
        message = input("Enter message ; ")
        ciphertext, plaintext = rsa_ed(message)
        print("RSA message , encrypted with a public key ",ciphertext)
        print("RSA message , decrypted with a private key ",plaintext)
    elif choice == "5":
         while True :
            password1 = getpass("enter a password ")
            print (check_stength(password1))
            if check_stength(password1).startswith("week"):
                print("pleas chose a strong password. ")
            else :
                break

            hashed_password = hash_pw(password1)
            print("hashed password ", hashed_password)
            attempt = getpass("re enter the password to verify ")
            print (verify_password(attempt,hashed_password))
    elif choice == "6":
        print("\na. Encrypt file")
        print("b. Decrypt file")
        sub = input("Choose (a/b): ")

        if sub == "a":
            path = input("Enter file path: ")
            key, enc_path, info = encrypt_file(path)
            if key:
                print("Key: ", key.decode())
                print("Encrypted file: ", info["encrypted_file"])
                print("Key saved to: ", info["key_saved_to"])
                print("Original size: ", info["original_size"])
                print("Encrypted size: ", info["encrypted_size"])
            else:
                print(info)

        elif sub == "b":
            path = input("Enter encrypted file path: ")
            print("\na. Enter key manually")
            print("b. Use key file")
            method = input("Choose (a/b): ")

            if method == "a":
                key = input("Enter key: ").encode()
                print(decrypt_file(path, key=key))
            elif method == "b":
                key_path = input("Enter key file path: ")
                print(decrypt_file(path, key_path=key_path))    
    else :
    
        print("invalid choince")

print ("tnx for ur work <3")
