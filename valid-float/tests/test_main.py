import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = (
    ('3', False),
    ('3.14', True),
    ('3.54_000_321', True),
    ('0.5', True),
    ('0,5', False),
    ('.5', True),
    (',5', False),
    ('-0.5', True),
    ('-0,5', False),
    ('-.5', True),
    ('-5', False),
    ('-5.', True),
    ('-5,', False),
    ('34_,', False),
    ('34_.,', False),
    ('_,', False),
    ('._,', False),
    ('3e2', True),
    ('3e2.5', False),
    ('3e2,5', False),
    ('-', False),
    ('+', False),
    ('11_345.879', True),
    ('11_345,879', False),
)


@pytest.mark.parametrize('number, expected', testdata)
def test_run(number, expected):
    assert main.run(number) == expected
