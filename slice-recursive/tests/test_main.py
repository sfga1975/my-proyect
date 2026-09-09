import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        'La felicidad no es algo que viene hecho. Proviene de tus propias acciones',
        10,
        [
            'La felicid',
            'ad no es a',
            'lgo que vi',
            'ene hecho.',
            ' Proviene ',
            'de tus pro',
            'pias accio',
            'nes',
        ],
    ),
    (
        'Si crees que eres demasiado pequeño para hacer la diferencia, intenta dormir con un mosquito',
        20,
        [
            'Si crees que eres de',
            'masiado pequeño para',
            ' hacer la diferencia',
            ', intenta dormir con',
            ' un mosquito',
        ],
    ),
    (
        'El amor es la ausencia de juicio',
        5,
        [
            'El am',
            'or es',
            ' la a',
            'usenc',
            'ia de',
            ' juic',
            'io',
        ],
    ),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(main, 'rslice', None), 'La función principal debe llamarse rslice'


@pytest.mark.parametrize('text, wsize, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(text, wsize, expected):
    assert main.rslice(text, wsize) == expected
