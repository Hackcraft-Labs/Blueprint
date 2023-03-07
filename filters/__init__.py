from copyreg import constructor
import importlib
import sys
import os


def import_filter(filter_name: str):
    try:
        module = importlib.import_module(
            "filters.{name}".format(name=filter_name))

        name = getattr(module, "FILTER_NAME")
        filter = getattr(module, "filter")
        init = getattr(module, "init")
        vars = getattr(module, "variables")

    except Exception as e:
        print("[!] Could not import filter {name}!".format(
            name=filter_name))
        sys.exit(1)

    return name, filter, init, vars
