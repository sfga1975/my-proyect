import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (6, 226.08),
    (7, 307.72),
    (8, 401.92),
]


@pytest.mark.parametrize('z, expected', testdata)
def test_run(z, expected):
    assert main.run(z) == expected
