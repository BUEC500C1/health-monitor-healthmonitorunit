# The Monitor is to show the information from Sensor, AI module, and database to users and modify the data.

# from sensor import generatedata
from InputError import InputError


class Monitor:
    raw = [0, [0, 0], 0.0]
    processed = [0, [0, 0], 0.0]
    ai = [0, [0, 0], 0.0]

    def __init__(self, raw, processed, ai, flag_raw=None, flag_processed=None, flag_ai=None):
        if flag_raw is None:
            self.raw = raw
        else:
            raise InputError("Invalid data!")
        if flag_processed is None:
            self.processed = processed
        else:
            raise InputError("Invalid processed data!")
        if flag_ai is None:
            self.ai = ai
        else:
            raise InputError("Invalid AI data!")

    # If the system has new measure data, then input the new data.
    # Input example: "66 78 120 0.24"
    def modify(self, flag_modify=None):
        if flag_modify is not None:
            new_data = input("Please input the new data.\n").split()
            self.raw[0] = new_data[0]
            self.raw[1] = [int(new_data[1]), int(new_data[2])]
            self.raw[2] = new_data[3]

    # Show the data to user
    def show(self):
        print("Measurement data: \n" +
              "Impulse: " + str(self.raw[0]) + "\n" +
              "Blood Pressure: " + str(self.raw[1]) + "\n" +
              "Blood Oxygen: " + str(self.raw[2]) + "\n" +
              "\n" +
              "Processed data: \n" +
              "Impulse: " + str(self.processed[0]) + "\n" +
              "Blood Pressure: " + str(self.processed[1]) + "\n" +
              "Blood Oxygen: " + str(self.processed[2]) + "\n" +
              "\n" +
              "AI prediction: \n" +
              "Impulse Prediction: " + str(self.ai[0]) + "\n" +
              "Blood Pressure Prediction: " + str(self.ai[1]) + "\n" +
              "Blood Oxygen Prediction: " + str(self.ai[2]) + "\n"
              )
