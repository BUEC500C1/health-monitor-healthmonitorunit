from InputError import InputError

class AI_Analysis(object):
    def __init__(self):
        super(AI_Analysis, self).__init__()

    def __str__(self):
        return "Very simple AI, Anti Intelligence"

    def analysis(self, impulse, blood_pressure, blood_oxygen, latest=3):
        # check latest


        # This is extremely simple "AI" lol
        # impulse
        future_impulse = 0
        for fiele in impulse:
            future_impulse += fiele
        future_impulse /= latest

        # blood_pressure
        future_pressure = list()
        fp_lo = 0
        fp_hi = 0
        for fpele in blood_pressure:
            fp_lo += fpele[0]
            fp_hi += fpele[1]
        future_pressure.append(fp_lo / latest)
        future_pressure.append(fp_hi / latest)

        # blood_oxygen
        future_oxygen = 0
        for foele in blood_oxygen:
            future_oxygen += foele
        future_oxygen /= latest

        # alarm_boolean
        # according to the future data, still False
        alarm_boolean = False

        return alarm_boolean, future_impulse, future_pressure, future_oxygen

