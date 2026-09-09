import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([2, 3, 5, 3, 2, 1, 8, 2], 3, 2),
    ([1, 2, 3], 2, -1),
    ([1, 1, 1, 5, 2, 5, 5], 3, 1),
    ([3, 9, 2, 7, 2, 9, 1, 9, 9], 4, 9),
    ([7, 7, 3, 3, 2, 2, 7, 2, 3, 7, 3, 7, 7, 1], 6, 7),
    ([], 5, -1),
]


@pytest.mark.parametrize('numbers, nrep, expected', testdata)
def test_run(numbers, nrep, expected):
    assert main.run(numbers, nrep) == expected
