
def get_triangle_side(s_value: str) -> float:
    """
    Value error. The value must be a float type.
    >>> get_triangle_side('asd')
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'asd'

    The normal work with float.
    >>> get_triangle_side('1.12')
    1.12

    The normal work with integer.
    >>> get_triangle_side('2')
    2.0

    Value error. The value must be more than zero.
    >>> get_triangle_side('0')
    Traceback (most recent call last):
    ...
    ValueError: The value must be more than zero
    """
    num = float(s_value)

    if num <= 0:
        raise ValueError('The value must be more than zero')
    else:
        return num


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

