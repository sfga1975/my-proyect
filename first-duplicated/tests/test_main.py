import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([2, 3, 5, 3, 2], 3),
    ([3, 7, 2, 9, 1, 9, 9], 9),
    (['x', 'y', 'z', 'y', 'x'], 'y'),
    ([1, 1, 1, 5, 2, 5, 5], 1),
    ([1, 2, 3], None),
    ([], None),
]


@pytest.mark.parametrize('items, expected', testdata)
def test_run(items, expected):
    assert main.run(items) == expected
