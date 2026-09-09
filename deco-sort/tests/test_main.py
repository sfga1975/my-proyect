import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    (lambda: [2, 1, 3], [], True, [1, 2, 3]),
    (lambda: [2, 1, 3], [], False, [3, 2, 1]),
    (lambda: [], [], True, []),
    (lambda: [1, 1, 1], [], True, [1, 1, 1]),
    (lambda a, b: [a, b], {'a': 2, 'b': 1}, True, [1, 2]),
    (lambda a, b, c, d: [d, c, b, a], {'a': 2, 'b': 1, 'c': 4, 'd': 3}, True, [1, 2, 3, 4]),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'sort', None), 'El decorador debe llamarse sort'


@pytest.mark.parametrize('func, func_args, asc, expected', testdata)
def test_expected(func, func_args, asc, expected):
    assert main.run(asc, func, func_args) == expected
