from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class SecondIntro(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13


class SecondIntroC(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 5 or \
               self.player.id_in_group == 9 or self.player.id_in_group == 13


class GameQuestions(Page):
    form_model = 'player'
    form_fields = ['game1', 'game2', 'game3', 'game4', 'game5']


class COL(Page):
    form_model = 'player'
    form_fields = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'con']


class IMPULSE(Page):
    form_model = 'player'
    form_fields = ['IMP1', 'IMP2', 'IMP3', 'IMP4', 'IMP5', 'IMP6', 'IMP7', 'IMP8']


class CPS(Page):
    form_model = 'player'
    form_fields = ['CPS1', 'CPS2', 'CPS3', 'CPS4', 'CPS5', 'CPS6']

class CCW(Page):
    form_model = 'player'
    form_fields = ['CCW1', 'CCW2', 'CCW3', 'CCW4', 'CCW5', 'CCW6', 'CCW7', 'CCW8', 'CCW9', 'CCW10']


class SOB(Page):
    form_model = 'player'
    form_fields = ['SOB1', 'SOB2', 'SOB3', 'SOB4']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['Tao', 'Eta', 'feed1', 'feed2', 'comments', 'know', 'age', 'gender']


class FinalPage(Page):
    pass
    def js_vars(player):
        label = player.participant.code
        player.link = "https://leidenuniv.eu.qualtrics.com/jfe/form/SV_8k6Z3v5xgS6GTMG" + "?ppID=" + str(label)
        return dict(
            link=player.link,
        )


page_sequence = [
    SecondIntro,
    SecondIntroC,
    GameQuestions,
    COL,
    IMPULSE,
    CPS,
    CCW,
    SOB,
    Demographics,
    FinalPage
]
