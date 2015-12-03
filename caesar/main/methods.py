def encrypting(text, rot, reverse=False):
    if reverse:
        step = -rot
    else:
        step = rot

    result = ''
    for char in text:
        if 97 <= ord(char) <= 122:
            result += chr(((ord(char) - 97) + int(step)) % 26 + 97)
        elif 65 <= ord(char) <= 90:
            result += chr(((ord(char) - 65) + int(step)) % 26 + 65)
        else:
            result += char

    return result
