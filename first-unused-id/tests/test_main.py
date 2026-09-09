import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([3, 1, 8, 4, 9], 2),
    ([7, 2, 12, 21, 5], 1),
    ([1, 2, 3, 5, 10, 7], 4),
    ([4, 3, 2, 1], 5),
    ([9, 5, 1, 2], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20], 11),
]


@pytest.mark.parametrize('ids, expected', testdata)
def test_run(ids, expected):
    assert main.run(ids) == expected
