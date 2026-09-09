import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('data/cistercian.txt', 9, {'the': 20, 'to': 10}),
    ('data/cistercian.txt', 8, {'the': 20, 'of': 8, 'a': 8, 'to': 10, 'you': 8}),
    ('data/cistercian.txt', 7, {'the': 20, 'of': 8, 'in': 7, 'a': 8, 'and': 7, 'to': 10, 'you': 8}),
    (
        'data/cistercian.txt',
        6,
        {'the': 20, 'of': 8, 'in': 7, 'a': 8, 'and': 7, 'what': 6, 'to': 10, 'you': 8},
    ),
    (
        'data/cistercian.txt',
        5,
        {'the': 20, 'of': 8, 'in': 7, 'a': 8, 'for': 5, 'and': 7, 'what': 6, 'to': 10, 'you': 8},
    ),
]


@pytest.mark.parametrize('input_path, lower_bound, expected', testdata)
def test_run(input_path, lower_bound, expected):
    assert main.run(input_path, lower_bound) == expected
