from ..config import *


def test_db_config():
    assert db_provider is not None
    assert db is not None
    assert all(x in ('user', 'password', 'host', 'port', 'database') for x in db.keys())
