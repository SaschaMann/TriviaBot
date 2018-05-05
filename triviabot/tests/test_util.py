from triviabot.util import *


def test_no_hl_nick():
    assert no_hl_nick('FooBar') == u'F\u200CooBar'
