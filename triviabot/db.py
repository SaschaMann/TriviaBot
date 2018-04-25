# -*- coding: utf-8 -*-
import time

from pony.orm import *
from .config import db as db_config
from .config import db_provider

db = Database()

while True:
    try:
        db.bind(db_provider, **db_config)
        break
    except OperationalError:
        time.sleep(1)


class User(db.Entity):
    nick = Required(str)
    score = Required(int)


@db_session
def find_or_create_user(nick):
    user = User.get(nick=nick)
    if not user:
        user = User(nick=nick, score=0)
    return user


@db_session
def add_score(nick, score):
    user = find_or_create_user(nick)
    user.score += score


@db_session
def get_score(nick):
    return find_or_create_user(nick).score


@db_session
def get_top_users(n):
    return [(nick, score) for (nick, score) in select((u.nick, u.score) for u in User).order_by(-2)[:n]]


db.generate_mapping(create_tables=True)
