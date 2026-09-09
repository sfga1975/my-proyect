import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('3,2', '1x^3'),
    ('12,5', '2x^6'),
    ('20,1', '10x^2'),
    ('40,3', '10x^4'),
    ('90,2', '30x^3'),
]


@pytest.mark.parametrize('poly, expected', testdata)
def test_run(poly, expected):
    assert main.run(poly) == expected
