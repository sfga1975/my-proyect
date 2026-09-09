import os

import pytest

if os.path.exists('solution.py'):
    from solution import IntegerStack
else:
    from main import IntegerStack  # type:ignore


@pytest.fixture
def stack1():
    return IntegerStack()


@pytest.fixture
def stack2():
    return IntegerStack(max_size=2)


@pytest.fixture
def stack3():
    s = IntegerStack(max_size=3)
    s.items = [10, 100, 1000]
    return s


@pytest.fixture
def stack4():
    s = IntegerStack(max_size=4)
    s.items = [50, 500, 5000, 50_000]
    return s
