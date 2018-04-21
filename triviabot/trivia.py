# -*- coding: utf-8 -*-
import irc3
from irc3.plugins.command import command
import requests

from .db import *
from .util import no_hl_nick


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
                add_score(mask.nick, 10)
                self.bot.privmsg(target, f'Correct answer "{self.trivia.answer}" by {mask.nick}! New score: {get_score(mask.nick)}🎉')
                self.trivia.reset()

    @command
    def top(self, mask, target, args):
        """Displays the top 10 users

            %%top
        """
        msg = ''
        for nick, score in get_top_users(10):
            msg += f'{no_hl_nick(nick)} ({score}) | '
        yield msg[:-3]

    @command
    def start(self, mask, target, args):
        """Starts a new round of trivia.

            %%start
        """
        if self.trivia.active:
            yield f'Trivia is running already: {self.trivia.question}'
        else:
            self.trivia.active = True
            # self.trivia.question = 'What is love?'
            # self.trivia.answer = '42'
            r = requests.get('http://triviaquestions:8080/v1/random_question').json()
            self.trivia.question = r['question']
            self.trivia.answer = r['answer']
            yield f'{mask.nick} has started a new round of trivia! {self.trivia.question} [{r["patch"]}]'
