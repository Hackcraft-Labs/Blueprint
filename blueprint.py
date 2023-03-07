from filters import import_filter
from jinja2 import Template
import traceback
import jinja2
import json
import sys
import os

def get_template(filename: str) -> str:
    """Gets a template from a file.

    Parameters
    ----------
    template : str
        The file location of the template

    Returns
    -------
    template
        a Blueprint template
    """

    template = ""

    try:
        with open(filename, "r") as template_file:
            template = template_file.read()
    except:
        print("[!] Could not open template file '{file}'!".format(file=filename))
        sys.exit(1)

    return template

def run_config(config_path: str, base_path=""):
    """Runs a Blueprint configuration from a specific path.

    Parameters
    ----------
    config_path : str
        The file location of the configuration
    base_path : str
        The path (until directory, including seperator), under which the configuration will be run. 

    
    """
    config_json = ""

    try:
        with open(config_path, "r") as config_file:
            config_json = config_file.read()
    except:
        print("[!] Could not read configuration file '{file}'".format(file=config_path))
        sys.exit(1)

    config = {}

    try:
        config = json.loads(config_json)
    except:
        print("[!] Invalid configuration file '{file}'".format(file=config))
        sys.exit(1)

    filters = config["filters"]
    targets = config["targets"]

    init_handlers = []
    vars_handlers = []
    imported_filters = {}

    for filter in filters:
        filter_name, filter_function, filter_init, filter_vars = import_filter(filter)

        imported_filters[filter_name] = filter_function
        init_handlers.append(filter_init)
        vars_handlers.append(filter_vars)

        print("[+] Imported filter '{name}'".format(name=filter))

    for k, v in imported_filters.items():
        jinja2.filters.FILTERS[k] = v

    for init_handler in init_handlers:
        init_handler()

    for target in targets:
        file_input = os.path.join(base_path, target["input"])
        file_output = os.path.join(base_path, target["output"])

        output = ""
        target_template = get_template(file_input)

        try:
            variables = target["variables"]

            for vars_handler in vars_handlers:
                variables = vars_handler(variables)

            output = Template(target_template).render(**variables)

        except Exception as e:
            print("[!] Failed when rendering template '{filename}'".format(filename=file_input))
            traceback.print_exception(e)
            sys.exit(1)

        try:
            with open(file_output, "w") as output_file:
                output_file.write(output)
                print("[+] Wrote output file '{filename}'".format(filename=file_output))
        except:
            print("[!] Could not write output file '{filename}'".format(filename=file_output))
            sys.exit(1)

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage:\n\tpython3 blueprint.py config.json")
        sys.exit(1)

    run_config(sys.argv[1])
