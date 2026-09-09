import filecmp
import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    ('data/data1.input.txt', 'data/data1.output.txt', 'data/data1.expected.txt'),
    ('data/data2.input.txt', 'data/data2.output.txt', 'data/data2.expected.txt'),
    ('data/data3.input.txt', 'data/data3.output.txt', 'data/data3.expected.txt'),
]


@pytest.mark.parametrize('input_path, output_path, expected', testdata)
def test_run(input_path, output_path, expected):
    main.run(input_path, output_path)
    filecmp.cmp(output_path, expected, shallow=False)
