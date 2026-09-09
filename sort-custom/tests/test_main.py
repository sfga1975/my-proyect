import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 2, 9, 7, 1, 8], [1, 2, 4, 7, 8, 9]),
    ([21, 11, 5, 34, 42, 7, 16, 3, 51, 18], [3, 5, 7, 11, 16, 18, 21, 34, 42, 51]),
    ([3, 2, 2, 5, 7, 1, 7, 9, 2, 9, 9, 4], [1, 2, 2, 2, 3, 4, 5, 7, 7, 9, 9, 9]),
    ([1, 0], [0, 1]),
    ([0], [0]),
]


@pytest.mark.parametrize('numbers, expected', testdata)
def test_run(numbers, expected):
    assert main.run(numbers) == expected
