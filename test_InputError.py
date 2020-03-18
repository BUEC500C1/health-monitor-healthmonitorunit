import pytest
from InputError import InputError


class TestAssert():
    def test_raise_exception(self):
        with pytest.raises(InputError) as excinfo:
            raise InputError("Nyet!!")

        assert "Nyet!!" in str(excinfo)
        assert excinfo.type == InputError
