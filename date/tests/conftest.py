import os

import pytest

if os.path.exists('solution.py'):
    from solution import Date
else:
    from main import Date  # type:ignore


@pytest.fixture
def date1():
    # JUEVES
    return Date(day=1, month=3, year=1979)


@pytest.fixture
def date2():
    # DOMINGO
    return Date(day=24, month=6, year=1984)
