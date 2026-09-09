import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([0, 1, 3, 5], [0, 1, 2, 3, 4, 5]),
    ([8, 12], [8, 9, 10, 11, 12]),
    ([0, 1, 1, 2, 2, 4, 6], [0, 1, 1, 2, 2, 3, 4, 5, 6]),
    ([0, 1, 1, 1, 5, 6, 6, 8], [0, 1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8]),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
