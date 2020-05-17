"""
ROT13
cryptor and decryptor
"""
import string

#Insert the text you want to encrypt or decrypt into the variable.
text = 'Lbh ner n ynml nffubyr jub pna\'g cebtenz fvzcyr tneontr.'

ALPH = string.ascii_lowercase
#cryptor and decriptor
def cryptor(text):
    buf = ''
    num = 0
    for char in text:
        flag_upper = 0
        if string.ascii_letters.find(char) == -1:
            buf += char
            continue
        if char.isupper(): 
            char = char.lower()
            flag_upper = 1        
        num = ALPH.find(char) + 13
        if num >= len(ALPH):
            buf += ALPH[num - len(ALPH)]
        else:
            buf += ALPH[num]
        if flag_upper == 1: buf = buf[:-1] + buf[-1].upper()
    return buf


print (cryptor(text))
