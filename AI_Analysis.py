from InputError import InputError
#Author: Jialun Wang (wjl1996@bu.edu) Here I simply commented the initial checks started from line 12 since these cases are posible in reality

class AI_Analysis(object):
    def __init__(self):
        super(AI_Analysis, self).__init__()

    def __str__(self):
        return "Very simple AI, Anti Intelligence"

    def analysis(self, impulse, blood_pressure, blood_oxygen, latest=3):
        # check latest
        # if latest <= 0 or latest > 20:
        #     raise InputError("Invalid [latest]!")
        # # check impulse
        # for ii in impulse:
        #     if ii <= 60 or ii > 100:
        #         raise InputError("Invalid [impulse]!")
        # # check blood_pressure
        # for jj in blood_pressure:
        #     if jj[0] <= 60 or jj[0] > 90 or \
        #        jj[1] <= 90 or jj[1] > 140:
        #         raise InputError("Invalid [blood_pressure]!")
        # # check blood_oxygen
        # for kk in blood_oxygen:
        #     if kk <= 0.0 or kk > 1.0:
        #         raise InputError("Invalid [blood_oxygen]!")

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


