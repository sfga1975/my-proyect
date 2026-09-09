from __future__ import annotations

import sqlite3

DB_PATH = ':memory:'

TASK_DONE_SYMBOL = '[X]'
TASK_PENDING_SYMBOL = '[ ]'


def create_db(db_path: str = DB_PATH) -> None:
    ...


class Task:
    ...


class ToDo:
    ...
