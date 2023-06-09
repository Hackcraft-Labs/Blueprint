FILTER_NAME = "content"


def init():
    return


def variables(variables: dict):
    return variables


def filter(input, mode="rb") -> str:
    print("[DBG] Running content.")

    with open(input, mode) as file:
        return file.read()
