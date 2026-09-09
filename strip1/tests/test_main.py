import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('What can I do', 'hat can I d'),
    ('Only when I sleep', 'nly when I slee'),
    ('Runaway', 'unawa'),
    ('Happiness', 'appines'),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
