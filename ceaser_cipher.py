def encrypt_caesar(text, shift):
    r=0
    m=''
    n=[]
    
    for i in text:
            char=i
            if char.isalpha():
                #for upper case
                if char.isupper():
                    r=ord(char)
                    m+=chr((r+shift-65)%26+65)
                    # m=chr((ord(char)+shift -65)%26+65)
                else: #for lower case
                    r=ord(char)
                    m+=chr((r+shift-97)%26+97)
                    # m=chr((ord(char)+shift -65)%26+65)
            else:
                if char.isdigit():
                     n.append(char)
                     m+='0'
                else:
                     m+=char

                
    #returned encrypted text
    return m,n
def decrypt_caesar(text, shift,n):
    q=''
    digit_index=0
    for i in text:
       
        char=i

        if char.isalpha():
                if char.isupper():
                    q += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    q += chr((ord(char) - shift - 97) % 26 + 97)
        elif char == '0':
                q += n[digit_index]
                digit_index += 1
        else:
                q += char
    return q
text=input("enter you text here: ")

shift=3
e,n=encrypt_caesar(text, shift)
d=decrypt_caesar(e,shift,n)
#printed encrypted and decrypted text
print(e)
print(d)


            
           

    


