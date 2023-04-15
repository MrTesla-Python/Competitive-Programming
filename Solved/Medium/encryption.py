def encrypt(letter_list, word):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    encrypter = {}
    for i in range(len(alpha)):
        encrypter[alpha[i]] = []
        encrypter[alpha[i]].append(letter_list[i])
    for i in word:
        if i.isalpha():
            letter = encrypter[i.lower()]
            letter = "".join(letter)
            if i.isupper():
                ans+=letter.upper()
            else:
                ans+=letter
        else:
            ans+=i
    return ans.strip()
def decrypt(letter_list, word):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    encrypter = {}
    for i in range(len(alpha)):
        encrypter[letter_list[i]] = []
        encrypter[letter_list[i]].append(alpha[i])
    for i in word:
        if i.isalpha():
            letter = encrypter[i.lower()]
            letter = "".join(letter)
            if i.isupper():
                ans+=letter.upper()
            else:
                ans+=letter
        else:
            ans+=i
    return ans.strip()
for t in range(int(input())):
    decrypt_or_encrypt = input()
    cipher_key = input()
    for n in range(int(input())):
        if decrypt_or_encrypt == "ENCRYPT":
            to_encrypt =  input()
            print(encrypt(cipher_key, to_encrypt))
        else:
            to_decrypt = input()
            print(decrypt(cipher_key, to_decrypt))