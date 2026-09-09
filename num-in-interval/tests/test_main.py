import inspect
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    (3, 2, 5, True),
    (10, 10, 10, True),
    (-1, -10, 10, True),
    (5, 0, 1, False),
]


@pytest.mark.dependency()
def test_func_signature():
    sig = inspect.signature(main.in_range)
    assert main.in_range.__name__ == 'in_range', 'La función debe llamarse in_range'
    assert len(sig.parameters) == 3, 'La función debe tener exactamente 3 parámetros'
    assert sig.parameters['value'].kind == inspect.Parameter.POSITIONAL_ONLY, (
        'El primer parámetro debe ser solo posicional'
    )


@pytest.mark.parametrize('value, lower_limit, upper_limit, expected', testdata)
@pytest.mark.dependency(depends=['test_func_signature'])
def test_run(value, lower_limit, upper_limit, expected):
    assert main.in_range(value, lower_limit, upper_limit) == expected
