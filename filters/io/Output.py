FILTER_NAME = "output"


def init():
    return


def variables(variables: dict):
    return variables


def filter(output, name=None) -> str:
    print("[DBG] Running output.")

    with open(name, "wb") as file:
        file.write(bytearray(output))
    
    return ""