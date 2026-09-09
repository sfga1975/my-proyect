import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (0, 1, 1, 61_000),
    (2, 1, 0, 7_260_000),
    (10, 45, 30, 38_730_000),
]


@pytest.mark.parametrize('hours, minutes, seconds, expected', testdata)
def test_run(hours, minutes, seconds, expected):
    assert main.run(hours, minutes, seconds) == expected
