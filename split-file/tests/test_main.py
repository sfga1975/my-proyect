import filecmp
import os
from pathlib import Path

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main

testdata = [
    (
        'data/quijote.input',
        '2-17,23-56,71-88',
        (
            'data/quijote.output.2-17',
            'data/quijote.output.23-56',
            'data/quijote.output.71-88',
        ),
    ),
    (
        'data/quijote.input',
        '1-1,3-5,10-12',
        (
            'data/quijote.output.1-1',
            'data/quijote.output.3-5',
            'data/quijote.output.10-12',
        ),
    ),
    (
        'data/quijote.input',
        '10-20,30-40,50-60,70-80,90-100',
        (
            'data/quijote.output.10-20',
            'data/quijote.output.30-40',
            'data/quijote.output.50-60',
            'data/quijote.output.70-80',
            'data/quijote.output.90-100',
        ),
    ),
    (
        'data/quijote.input',
        '1-5',
        ('data/quijote.output.1-5',),
    ),
]


@pytest.mark.parametrize('input_path, ranges, output_paths', testdata)
def test_run(input_path, ranges, output_paths):
    main.run(input_path, ranges)
    for output_path in output_paths:
        assert Path(output_path).exists(), f'El fichero {output_path} no existe'
        expected_path = output_path.replace('output', 'expected')
        assert filecmp.cmp(output_path, expected_path, shallow=False)
