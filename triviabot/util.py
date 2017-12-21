def no_hl_nick(nick):
    return nick[:1] + u'\u200C' + nick[1:]
