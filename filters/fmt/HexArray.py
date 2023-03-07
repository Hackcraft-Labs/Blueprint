FILTER_NAME = "hexarr"


def init():
    return


def variables(variables: dict):
    return variables


def filter(input) -> str:
    print("[DBG] Running hexarr.")

    return ', '.join("0x{:02x}".format(x) for x in input)
