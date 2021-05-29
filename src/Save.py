import shelve


class Save:
    """

    """

    def __init__(self):
        self.file = shelve.open('data')

    def get_data(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0

    def add(self, name, value):
        self.file[name] = value

    def __del__(self):
        self.file.close()
