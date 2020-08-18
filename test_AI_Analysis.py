import pytest
from AI_Analysis import AI_Analysis
from InputError import InputError


tai = AI_Analysis()
tip = [66, 77, 88, 99]
tbp = [[70, 110],
       [75, 130],
       [80, 115],
       [75, 125]]
tbo = [0.77, 0.62, 0.55, 0.49]


def test_regular_input():
    out = tai.analysis(tip, tbp, tbo, 4)
    assert out[0] == False
    assert out[1] == 82
    assert out[2][0] == 75
    assert out[2][1] == 120
    assert out[3] == 0.6075


def test_bad_latest():
    with pytest.raises(InputError) as excinfo:
        tai.analysis(tip, tbp, tbo, 0)
    assert "Invalid [latest]!" in str(excinfo)


def test_bad_impulse():
    bip = [66, 77, 88, -99]
    with pytest.raises(InputError) as excinfo:
        tai.analysis(bip, tbp, tbo, 4)
    assert "Invalid [impulse]!" in str(excinfo)


def test_bad_blood_pressure():
    bbp = [[1, 110],
           [75, 130],
           [80, 115],
           [75, 125]]
    with pytest.raises(InputError) as excinfo:
        tai.analysis(tip, bbp, tbo, 4)
    assert "Invalid [blood_pressure]!" in str(excinfo)


def test_bad_blood_oxygen():
    bbo = [0.77, 0.62, -0.55, 0.49]
    with pytest.raises(InputError) as excinfo:
        tai.analysis(tip, tbp, bbo, 4)
    assert "Invalid [blood_oxygen]!" in str(excinfo)
