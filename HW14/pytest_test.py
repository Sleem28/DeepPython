import pytest
from .doctest_func import get_triangle_side


def test_convert_string_to_float():
    with pytest.raises(ValueError):
        get_triangle_side('asd')


def test_normal_work_with_float():
    assert get_triangle_side('1.12') == 1.12, 'Normal work with the float type'


def test_normal_work_with_integer():
    assert get_triangle_side('2') == 2.0, 'Normal work with the integer type'


def test_value_more_zero():
    with pytest.raises(ValueError):
        get_triangle_side('0')


if __name__ == '__main__':
    pytest.main()

