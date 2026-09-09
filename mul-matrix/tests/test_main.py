import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([[1, 2, 3], [4, 5, 6]], [[5, -1], [1, 0], [-2, 3]], [[1, 8], [13, 14]]),
    ([[1, 2, 3], [1, 1, 1], [0, 1, -1]], [[1], [2], [1]], [[8], [4], [1]]),
    ([[9, 7], [3, 2]], [[8, 4], [7, 3]], [[121, 57], [38, 18]]),
    (
        [[9, 1, 8, 4], [3, 8, 2, 8], [5, 5, 2, 6]],
        [[2, 3], [4, 1], [6, 4], [3, 7]],
        [[82, 88], [74, 81], [60, 70]],
    ),
    ([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1], [2, 3]], [[31, 19], [85, 55]]),
    ([[1, 4, 5], [3, 2, 1]], [[4, 3, 2], [5, 6, 8]], None),
]


@pytest.mark.parametrize('A, B, expected', testdata)
def test_run(A, B, expected):
    assert main.run(A, B) == expected
