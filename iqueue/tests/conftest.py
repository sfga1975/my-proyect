import os

import pytest

if os.path.exists('solution.py'):
    from solution import IntegerQueue
else:
    from main import IntegerQueue  # type:ignore


@pytest.fixture
def queue1():
    return IntegerQueue()


@pytest.fixture
def queue2():
    return IntegerQueue(max_size=2)


@pytest.fixture
def queue3():
    s = IntegerQueue(max_size=3)
    s.items = [10, 100, 1000]
    return s


@pytest.fixture
def queue4():
    s = IntegerQueue(max_size=4)
    s.items = [50, 500, 5000, 50_000]
    return s
