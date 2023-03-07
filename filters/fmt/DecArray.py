FILTER_NAME = "decarr"


def init():
    return


def variables(variables: dict):
    return variables


def filter(input) -> str:
    print("[DBG] Running decarr.")

    return ', '.join("{x}".format(x) for x in input)
