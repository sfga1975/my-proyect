import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    ('data/python.input.txt', 'data/python.output.txt', 'data/python.expected.txt'),
    ('data/minizen.input.txt', 'data/minizen.output.txt', 'data/minizen.expected.txt'),
    ('data/something.input.txt', 'data/something.output.txt', 'data/something.expected.txt'),
    ('data/transforma.input.txt', 'data/transforma.output.txt', 'data/transforma.expected.txt'),
]


@pytest.mark.parametrize('input_path, output_path, expected', testdata)
def test_run(input_path, output_path, expected):
    main.run(input_path, output_path)
    assert filecmp.cmp(output_path, expected, shallow=False)
