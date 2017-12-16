# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3


@irc3.plugin
class MyPlugin:
    requires = [
        'irc3.plugins.core',
        'irc3.plugins.command',
    ]

    def __init__(self, bot):
        self.bot = bot
        self.log = self.bot.log

    def connection_made(self):
        pass

    def server_ready(self):
        pass

    def connection_lost(self):
        pass

    @irc3.event(irc3.rfc.JOIN)
    def greet(self, mask, channel, **kwargs):
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, f'Hallå {mask.nick}!')
        else:
            self.bot.privmsg(channel, 'Hej hej!')

    @command
    def echo(self, mask, target, args):
        """Echo command
            %%echo <message>...
        """
        yield ' '.join(args['<message>'])
