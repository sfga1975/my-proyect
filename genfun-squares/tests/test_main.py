import os
import types

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, []),
    (10, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]),
    (15, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]),
    (20, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'gen_sq', None), 'La función principal debe llamarse gen_sq'


@pytest.mark.dependency(depends=['test_func_exists'])
def test_func_is_generator():
    assert isinstance(main.gen_sq(0), types.GeneratorType)


@pytest.mark.parametrize('n, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(n, expected):
    assert list(main.gen_sq(n)) == expected
