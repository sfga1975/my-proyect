import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ((1, 2, 3, 1, 1, 5, 6, 1), 1, 4),
    ((2, 2, 2, 2, 2), 2, 5),
    ((1, 2, 3, 4, 5), 0, 0),
    (tuple(), 1, 0),
    ((1, 2, 3, 4, 5, 5, 5, 5), None, -1),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'mcount', None), 'La función principal debe llamarse mcount'


@pytest.mark.parametrize('items, target, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(items, target, expected):
    result = main.mcount(items, target) if target is not None else main.mcount(items)
    assert result == expected
