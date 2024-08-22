def rotateOneLeft(list):
    length = len(list)
    temp = list[0]
    for i in range(1, length):
        list[i-1]=list[i]
    list[length-1] = temp

    return list


def rotateOneRight(list):
    length = len(list)
    temp = list[length-1]
    for i in range(length-1,0, -1):
        list[i]=list[i-1]
    list[0] = temp
    return list


def rotateManyLeft(list, n = 1):
    for i in range(n):
        rotateOneLeft(list)
    return list


def rotateManyRight(list, n = 1):
    for i in range(n):
        list = rotateOneRight(list)
    return list


def CesarCipher(str):
    encoded_str = ''
    for l in str:
        if l == ' ':
            encoded_str += ' '
        else:
            encoded_str += dictionary[l]
    return encoded_str

string1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
backup_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiper = rotateManyRight(string1, 3)
dictionary = dict(zip(backup_alphabet, chiper))
enc = CesarCipher(input("Enter your message : ").upper())
print(enc)

