from pathlib import Path

import pytest


@pytest.fixture(scope='session', autouse=True)
def clean_up():
    for file in Path('data').glob('*output*'):
        file.unlink(missing_ok=True)
    yield
