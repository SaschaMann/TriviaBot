# -*- coding: utf-8 -*-
from pony.orm import *

db = Database()

while True:
    try:
        db.bind(provider='postgres', user='postgres', password='B4DFWh8BRiETpF7wH83JhpT4b3zPKJngYCiBJh2vxdK6h4tqNNRHnuXr7cmNQEgQ', host='postgres', database='postgres')
        break
    except OperationalError:
        pass


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
