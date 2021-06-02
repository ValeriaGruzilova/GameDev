import os
import sys
import shelve


def resource_path(relative):
    """Function to find and add a related file path.

    Args:
        relative: the path to which you need to pick up a related path.
    Returns:
        relative path
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class Save:
    """Class for writing data to a file and reading it.

    Attributes:
        file: files using shelve to write and read data.
    """
    def __init__(self):
        self.file = shelve.open(resource_path(os.path.join('C:/Games/Magic Rush/src', 'data')))

    def get_data(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0

    def add(self, name, value):
        self.file[name] = value
        self.file.sync()

    def __del__(self):
        self.file.close()