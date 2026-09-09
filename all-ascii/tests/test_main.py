import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('Esto es una frase cualquiera', True),
    ('Esto sólo es una frase cualquiera', False),
    ('This is ASCII', True),
    ('😀', False),
]


@pytest.mark.parametrize('x, expected', testdata)
def test_run(x, expected):
    assert main.run(x) == expected
