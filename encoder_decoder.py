def encode(string):
    encoded_string = ''
    for i in string:
        order = ord(i) - 26 if i.isalpha() else ord(i)
        encoded_string += chr(917604) * order + chr(917601) if i.isalpha() else chr(917617) * order + chr(917601)
    return encoded_string


def decode(encoded_string):
    return ''.join([chr(len(i)) if ord(i[0]) == 917617 else chr(len(i)+26) for i in encoded_string.split(chr(917601))[:-1]])
