class InputError(Exception):
    """docstring for InputError"""
    def __init__(self, arg):
        super(InputError, self).__init__()
        self.arg = arg
