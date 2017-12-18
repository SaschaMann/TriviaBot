# -*- coding: utf-8 -*-
import irc3
from irc3.plugins.command import command


class TriviaGame:
    def __init__(self):
        self.active = False
        self.question = None
        self.answer = None

    def check_answer(self, guess):
        return self.active and guess.lower() == self.answer

    def reset(self):
        self.question = self.answer = None
        self.active = False


@irc3.plugin
class Trivia:
    requires = [
        'irc3.plugins.core',
        'irc3.plugins.command',
    ]

    def __init__(self, bot):
        self.bot = bot
        self.log = self.bot.log
        self.trivia = TriviaGame()

    def connection_made(self):
        pass

    def server_ready(self):
        pass

    def connection_lost(self):
        pass

    @irc3.event(irc3.rfc.PRIVMSG)
    def on_message(self, target, mask, data, **kwargs):
        if self.trivia.active:
            if data == self.trivia.answer.lower():
                self.bot.privmsg(target, f'Correct answer "{self.trivia.answer}" by {mask.nick}! 🎉')
                self.trivia.reset()

    @command
    def start(self, mask, target, args):
        """Starts a new round of trivia.

            %%start
        """
        if self.trivia.active:
            yield f'Trivia is running already: {self.trivia.question}'
        else:
            self.trivia.active = True
            self.trivia.question = 'What is love?'
            self.trivia.answer = '42'
            yield f'{mask.nick} has started a new round of trivia! {self.trivia.question}'
