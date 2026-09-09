import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, '1'),
    (10, '10'),
    (100, '100'),
    (1000, '1,000'),
    (10000, '10,000'),
    (100000, '100,000'),
    (1000000, '1,000,000'),
    (10000000, '10,000,000'),
    (100000000, '100,000,000'),
]


@pytest.mark.parametrize('number, expected', testdata)
def test_run(number, expected):
    assert main.run(number) == expected
