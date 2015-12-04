def encrypting(text, rot, reverse=False):
    if reverse:
        step = -int(rot)
    else:
        step = int(rot)

    result = ''
    for char in text:
        if 97 <= ord(char) <= 122:
            result += chr(((ord(char) - 97) + int(step)) % 26 + 97)
        elif 65 <= ord(char) <= 90:
            result += chr(((ord(char) - 65) + int(step)) % 26 + 65)
        else:
            result += char

    return result


a = 'This is a new text'


def countChar(text):

    resDict = {}

    for char in text:
        if not resDict.get(char):
            resDict[char] = 1
        else:
            resDict[char] += 1

    return resDict


def convertToDiagram(dict):
    li = []
    for k, v in dict.items():
        li.append({'label': k, 'value': v})
    return li
