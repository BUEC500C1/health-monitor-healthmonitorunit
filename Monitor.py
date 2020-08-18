# The Monitor is to show the information from Sensor, AI module, and database to users and modify the data.
# from sensor import generatedata
from InputError import InputError


class Monitor:
    raw = [0, [0, 0], 0.0]
    processed = [0, [0, 0], 0.0]
    ai = [0, [0, 0], 0.0]

        if flag_raw is None:
            self.raw = raw
        else:
            raise InputError("Invalid data!")

        if flag_ai is None:
            self.ai = ai
        else:
            raise InputError("Invalid AI data!")

    # If the system has new measure data, then input the new data.
    # Input example: "66 78 120 0.24"
    def modify(self, flag_modify=None):
        if flag_modify is not None:
            new_data = input("Please input the new data.\n").split()

    # Show the data to user
    def show(self):
        print("Measurement data: \n" +
