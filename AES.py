def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

from Crypto.Cipher import AES
def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as f:
        data=f.read()

        cipher=AES.new(key,AES.MODE_CBC,iv)
        encrypted=cipher.encrypt(pad(data))
    
    with open(file_path+'.enc','wb') as f:
        f.write(encrypted)

def decrypt_file(enc_path,key, iv):
    with open(enc_path, 'rb') as f:
        encrypted=f.read()

        cipher=AES.new(key,AES.MODE_CBC,iv)
        decrypted=unpad(cipher.decrypt(encrypted))

        out_path=enc_path.replace(".enc","decrypted")
        with open(out_path, 'wb') as f:
            f.write(decrypted)


from Crypto.Random import get_random_bytes
import base64

choice = input("Choose:[E]ncrypt or [D]ecrypt? ").strip().upper()

if choice == 'E':
    key = get_random_bytes(16)  
    iv = get_random_bytes(16)

    print("Key (base64):", base64.b64encode(key).decode())
    print("IV  (base64):", base64.b64encode(iv).decode())
    print("Save these for decryption!")

    path = input("File path to encrypt: ").strip()
    encrypt_file(path, key, iv)

elif choice == 'D':
    path = input("Encrypted file path: ").strip()
    key = base64.b64decode(input("Key (base64): ").strip())
    iv = base64.b64decode(input("IV (base64): ").strip())

    decrypt_file(path, key, iv)

else:
    print("Invalid choice")



    










