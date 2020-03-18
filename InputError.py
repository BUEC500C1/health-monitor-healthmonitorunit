class InputError(Exception):
    def __init__(self, arg):
        super(InputError, self).__init__()
        self.arg = arg

    def __str__(self):
        return self.arg
