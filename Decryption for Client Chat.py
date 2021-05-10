from cryptography.fernet import Fernet

f = Fernet("trtW_GH9qjysGMIZcZh76BnLn68FD0loUt7EdC_jK6M=")

while True:
    encrypted_data = input("Please enter the text you would like to decrypt(Enter Q to Quit): ")
    if encrypted_data != "Q":
        d = f.decrypt(bytes(encrypted_data, encoding='utf8'))
        print(d)
    else:
        break