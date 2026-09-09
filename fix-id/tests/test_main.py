import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        [
            {'id': 1, 'lang': 'English'},
            {'id': 3, 'lang': 'German'},
            {'id': 4, 'lang': 'Italian'},
            {'id': 5, 'lang': 'Portuguese'},
            {'id': 6, 'lang': 'Spanish'},
            {'id': 2, 'lang': 'French'},
        ],
        [
            {'id': 1, 'lang': 'English'},
            {'id': 2, 'lang': 'German'},
            {'id': 3, 'lang': 'Italian'},
            {'id': 4, 'lang': 'Portuguese'},
            {'id': 5, 'lang': 'Spanish'},
            {'id': 6, 'lang': 'French'},
        ],
    ),
    (
        [
            {'id': 4, 'subject': 'Math'},
            {'id': 2, 'subject': 'English'},
            {'id': 9, 'subject': 'Science'},
            {'id': 5, 'subject': 'Computing'},
            {'id': 3, 'subject': 'Physics'},
            {'id': 1, 'subject': 'Law'},
        ],
        [
            {'id': 1, 'subject': 'Math'},
            {'id': 2, 'subject': 'English'},
            {'id': 3, 'subject': 'Science'},
            {'id': 4, 'subject': 'Computing'},
            {'id': 5, 'subject': 'Physics'},
            {'id': 6, 'subject': 'Law'},
        ],
    ),
    (
        [
            {'id': 99, 'name': 'Fred'},
            {'id': 1, 'name': 'John'},
            {'id': 34, 'name': 'Anna'},
            {'id': 7, 'name': 'Susan'},
            {'id': 2, 'name': 'Anthony'},
            {'id': 11, 'name': 'Sarah'},
        ],
        [
            {'id': 1, 'name': 'Fred'},
            {'id': 2, 'name': 'John'},
            {'id': 3, 'name': 'Anna'},
            {'id': 4, 'name': 'Susan'},
            {'id': 5, 'name': 'Anthony'},
            {'id': 6, 'name': 'Sarah'},
        ],
    ),
    (
        [],
        [],
    ),
]


@pytest.mark.parametrize('db, expected', testdata)
def test_run(db, expected):
    assert main.run(db) == expected
