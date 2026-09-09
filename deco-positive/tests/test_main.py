import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    (lambda: 1, tuple(), {}, 1),
    (lambda a: a, (2,), {}, 2),
    (lambda a: a, (-2,), {}, None),
    (lambda a, b: a * b, tuple(), dict(a=3, b=7), 21),
    (lambda a, b: a * b, tuple(), dict(a=3, b=-7), None),
]


@pytest.mark.dependency()
def test_decorator_exists():
    assert getattr(main, 'assert_positive', None), 'El decorador debe llamarse assert_positive'


@pytest.mark.dependency(depends=['test_decorator_exists'])
@pytest.mark.parametrize('func, func_args, func_kwargs, expected', testdata)
def test_expected(func, func_args, func_kwargs, expected):
    assert main.run(func, func_args, func_kwargs) == expected
