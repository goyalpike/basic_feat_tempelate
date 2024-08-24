import pytest

from math_ops.basic_math_ops import Adder, Multiplier


@pytest.mark.parametrize("test_input1, test_input2, result", [(1, 2, 3), (3, 4, 7)])
def test_add(test_input1, test_input2, result):
    assert Adder(test_input1)(test_input2) == result


def test_multiply():
    assert Multiplier(3)(10) == 30
