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
        if char.isalpha():
            if not resDict.get(char):
                resDict[char] = 1
            else:
                resDict[char] += 1
        else:
            continue

    return resDict


def convertToDiagram(dict):
    li = []
    for k, v in dict.items():
        li.append({'label': k, 'value': v})
    return li


def possibleRot(text):
    letter_dict = countChar(text)
    max_count_lett = max(letter_dict, key=letter_dict.get)
    ordering_lett = [101, 97, 104, 111, 105, 110]
    if len(text) > 10:
        if ord(max_count_lett) in ordering_lett:
            return 'We think, you don\'t need to encrypt your text!'
        else:
            return 'We think, you can try ' + \
                ', '.join([str(abs(i - ord(max_count_lett))) for i in ordering_lett]) + \
                ' ROT\'S to encrypt your text'
    else:
        return 'It\'s too short, we can\'t analyzing your text'
