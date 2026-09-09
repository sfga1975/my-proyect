import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, 10, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (0, 2, 0.25, [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]),
    (0, 1, 0.21, [0, 0.21, 0.42, 0.63, 0.84]),
    (-3.25, 0, 0.5, [-3.25, -2.75, -2.25, -1.75, -1.25, -0.75, -0.25]),
    (7, 12, 4.2, [7, 11.2]),
    (0, 1, 1, [0]),
    (0, 0, 1, []),
]


@pytest.mark.parametrize('start, stop, step, expected', testdata)
def test_run(start, stop, step, expected):
    assert main.run(start, stop, step) == expected
