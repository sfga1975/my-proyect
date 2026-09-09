import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/lorem.txt', (7, 232, 1470)),
    ('data/emojis.txt', (1, 5, 26)),
]


@pytest.mark.parametrize('input_path, expected', testdata)
def test_run(input_path, expected):
    assert main.run(input_path) == expected
