FILTER_NAME = "content"


def init():
    return


def variables(variables: dict):
    return variables


def filter(input) -> str:
    print("[DBG] Running content.")

    with open(input, "rb") as file:
        return file.read()
