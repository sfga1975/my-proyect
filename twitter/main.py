from __future__ import annotations

import re
import sqlite3

DB_PATH = ':memory:'

RETWEET_PREFIX = '[RT]'
MAX_TWEET_LENGTH = 280


def create_db(db_path: str = DB_PATH) -> None:
    ...


class User:
    ...


class Tweet:
    ...


class Twitter:
    ...


class TwitterError(Exception):
    ...
