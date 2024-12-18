from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class information(Page):
    form_model = 'player'


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent1', 'consent2', 'consent3', 'consent4', 'optional', 'full_name', 'date']


class BasicIntro(Page):
    form_model = 'player'
    form_fields = ['nick_name']
    def before_next_page(self):
        self.player.full_name = self.player.nick_name

class GameInstructions(Page):
    pass


class CInstructions(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class Story(Page):
    pass


class TestingUnderstanding1(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['und1']


class TestingUnderstanding1R(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class TestingUnderstanding2(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['und2']


class TestingUnderstanding2R(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class TestingUnderstanding3(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['und3']


class TestingUnderstanding3R(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class TestingUnderstanding4(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['und4']


class TestingUnderstanding4R(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class TestingUnderstanding5(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['und5']


class TestingUnderstanding5R(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class UnderstandGame(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['under']


class SecondInstructions(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13 and self.player.under


class TestingUnderstandingC1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['cund1']


class TestingUnderstandingC1R(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class TestingUnderstandingC2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['cund2']


class TestingUnderstandingC2R(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class TestingUnderstandingC3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['cund3']


class TestingUnderstandingC3R(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class TestingUnderstandingC4(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['cund4']


class TestingUnderstandingC4R(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class TestingUnderstandingC5(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13
    form_model = 'player'
    form_fields = ['cund5']


class TestingUnderstandingC5R(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class WaitingPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_player_names()


page_sequence = [
    information,
    Consent,
    BasicIntro,
    GameInstructions,
    Story,
    CInstructions,
    TestingUnderstanding1,
    TestingUnderstanding1R,
    TestingUnderstanding2,
    TestingUnderstanding2R,
    TestingUnderstanding3,
    TestingUnderstanding3R,
    TestingUnderstanding4,
    TestingUnderstanding4R,
    TestingUnderstanding5,
    TestingUnderstanding5R,
    TestingUnderstandingC1,
    TestingUnderstandingC1R,
    TestingUnderstandingC2,
    TestingUnderstandingC2R,
    TestingUnderstandingC3,
    TestingUnderstandingC3R,
    TestingUnderstandingC4,
    TestingUnderstandingC4R,
    TestingUnderstandingC5,
    TestingUnderstandingC5R,
    UnderstandGame,
    SecondInstructions,
    WaitingPage
]
