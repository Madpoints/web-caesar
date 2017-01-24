def alphabet_position(letter):
    if letter.isupper():
        position = ord(letter) - 65
        return position
    else:
        position = ord(letter) - 97
        return position
        

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    elif char.isupper():
        rot_char = chr( ( ( alphabet_position(char) + rot ) % 26 ) + 65 )
        return rot_char
    else:
        rot_char = chr( ( ( alphabet_position(char) + rot ) % 26 ) + 97 )
        return rot_char


def encrypt(text, rot):
    encrypted = ""
    for char in text:
        if char.isalpha():
            encrypted = encrypted + rotate_character(char, rot)
        else:
            encrypted = encrypted + char
    return encrypted
