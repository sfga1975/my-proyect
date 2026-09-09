import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    (lambda a, b: a - b, (-4, 7), -3),
    (lambda a, b: a + b, (-7, 2), 9),
    (lambda a, b, c, d: min(a, b, c, d), (-3, 1, 5, -2), -2),
    (lambda a, b, c, d, e: max(a, b, c, d, e), (0, -9, 3, 1, -5), 9),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'fabs', None), 'El decorador debe llamarse fabs'


@pytest.mark.dependency(depends=['test_decorator_exists'])
@pytest.mark.parametrize('func, func_args, expected', testdata)
def test_expected(func, func_args, expected):
    assert main.run(func, func_args) == expected
