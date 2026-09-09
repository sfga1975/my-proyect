import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('1abc2', (1, 2)),
    ('pqr3stu8vwx', (3, 8)),
    ('a1b2c3d4e5f', (1, 5)),
    ('treb7uchet', (7, 7)),
    ('TORm3NT4', (3, 4)),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
