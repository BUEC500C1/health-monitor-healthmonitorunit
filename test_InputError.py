import pytest
from InputError import InputError


def test_raise_exception():
    with pytest.raises(InputError) as excinfo:
        raise InputError("Nyet!!")

    assert "Nyet!!" in str(excinfo)
    assert excinfo.type == InputError
