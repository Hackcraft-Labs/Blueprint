import random

FILTER_NAME = "xor"
KEY = 0x0


def init():
    global KEY

    KEY = random.randint(0, 255)
    print("[*] Generated random XOR key: {key}".format(key=str(hex(KEY))))


def variables(variables: dict):
    global KEY

    variables["XOR_KEY"] = str(hex(KEY))

    return variables


def filter(input) -> str:
    print("[DBG] Running xor.")
    output = []

    # XOR each character with the key
    for letter in input:
        output.append(ord(letter) ^ KEY)

    return output
