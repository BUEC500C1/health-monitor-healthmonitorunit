from InputError import InputError


'''
para impulse:           heartrate               list [ int (60,100] ]
para blood_pressure:    blood pressure          list [ list[ int (60,90] , int (90,140] ] ]
para blood_oxygen:      blood oxygen            list [ float (0.0,1.0] ]
para latest:            get latest N inputs     int (1,20]

return list[ alarm_boolean , impulse , blood_pressure , blood_oxygen ]
'''
def ai_analysis(impulse, blood_pressure, blood_oxygen, latest=3):
    try:
        # check latest
        if latest <= 0 or latest > 20:
            raise InputError("Invalid [latest]!")
    except InputError as e:
        print(e)
    else:
        future = list()
        # This is extremely simple "AI" lol

        # alarm_boolean
        future.append(False)

        # impulse
        future_impulse = 0
        for fiele in impulse:
            future_impulse += fiele
        future.append(future_impulse / latest)

        # blood_pressure
        future_pressure = list()
        fp_lo = 0
        fp_hi = 0
        for fpele in blood_pressure:
            fp_lo += fpele[0]
            fp_hi += fpele[1]
        future_pressure.append(fp_lo / latest)
        future_pressure.append(fp_hi / latest)
        future.append(future_pressure)

        # blood_oxygen
        future_oxygen = 0
        for foele in blood_oxygen:
            future_oxygen += foele
        future.append(future_oxygen / latest)

        # recheck the alarm_boolean
        # according to the future data, still False
        future[0] = False

        return future
