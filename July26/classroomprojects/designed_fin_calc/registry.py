import json
REGISTER: dict = {}


def register(name: str):
    """A decorator to register a class in the REGISTER dictionary.

    Args:
        name (str): The name to register the class under.
    """

    def _register(cls):
        # read from supported.json all values in supported
        # and if name not in supported, raise an exception
        with open("supported.json") as f:
            config = json.load(f)
        if name not in config["unsupported"]:
            REGISTER[name] = cls
        return cls

    return _register
