FILTER_NAME = "djb2"


def init():
    return

def variables(variables: dict):
    return variables

def filter(input):
    hash = 0x7734773477347734

    for byte in input:
        hash = ((hash << 0x5) + hash) + ord(byte)
    
    hash = hash & 0xFFFFFFFFFFFFFFFF

    return hex(hash)