# Caesar Cipher
select = input("Type 'encode' to encrypt, tyep 'decode' to decrypt:\n").lower().strip()
alphapet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
msg = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        new_pos = alphapet.index(letter) + shift_amount
        new_alph = alphapet[new_pos]
        cipher_text += new_alph
    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    caesar_text = ""
    for letter in plain_text:
        new_pos = alphapet.index(letter) - shift_amount
        new_alph = alphapet[new_pos]
        caesar_text += new_alph
    print(f"The encoded text is {caesar_text}")
    

if select == "encode":
    encrypt(plain_text=msg, shift_amount=shift)
elif select == "decode":
    decrypt(plain_text=msg, shift_amount=shift)