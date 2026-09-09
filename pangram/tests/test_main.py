import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    ('The quick brown fox jumps over the lazy dog', True),
    ('Sylvia wagt quick den Jux bei Pforzheim', True),
    ('Portez ce whisky au vieux juge blond qui fume', True),
    ('I am not a pangram', False),
    ('aeiou', False),
    ('ºª!|"@·#$%&/()=?¡¿^`+*[]{}', False),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'is_pangram', None), 'La función principal debe llamarse is_pangram'


@pytest.mark.parametrize('text, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_run(text, expected):
    assert main.is_pangram(text) == expected
