import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)), ({8, 9, 4, 7}, {1, 2, 3, 5})),
    (((1, 2), ('|', '@'), ('!', '"')), ({'|', 1, '!'}, {2, '@', '"'})),
]


@pytest.mark.parametrize('input, expected', testdata)
def test_run(input, expected):
    assert main.run(input) == expected
