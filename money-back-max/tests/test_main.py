import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (20, {5: 3, 2: 7, 1: 3}, {5: 3, 2: 2, 1: 1}),
    (7, {2: 1, 1: 3, 0.5: 10}, {2: 1, 1: 3, 0.5: 4}),
    (13.50, {5: 20, 2: 1, 0.5: 7}, {5: 2, 2: 1, 0.5: 3}),
    (11, {0.10: 2, 0.5: 10, 2: 7}, {2: 5, 0.5: 2.0}),
    (0, {0.5: 5, 0.20: 5, 0.10: 5}, {}),
    (4.75, {1: 5, 5: 5, 0.20: 5}, None),
    (10, {5: 1, 2: 10}, None),
]


@pytest.mark.parametrize('to_give_back, available_currencies, expected', testdata)
def test_run(to_give_back, available_currencies, expected):
    assert main.run(to_give_back, available_currencies) == expected
