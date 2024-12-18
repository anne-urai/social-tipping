from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Introduction to the Master's thesis experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'thesis_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_player_names(self):
        print('setting player names')
        for player in self.get_players():
            player.participant.vars['player_name'] = player.nick_name


class Player(BasePlayer):

 # Consent #
    consent1 = models.IntegerField(
        choices=[[1, 'Yes']],
        label='I have read and I understand the information provided about this study. I have had the opportunity to ask questions, and those questions has been sufficiently answered.',
        widget=widgets.RadioSelectHorizontal)
    consent2 = models.IntegerField(
        choices=[[1, 'Yes']],
        label='I know that I can stop at any time, for any reason.',
        widget=widgets.RadioSelectHorizontal)
    consent3 = models.IntegerField(
        choices=[[1, 'Yes']],
        label='I understand that my data will not have identifying information on it, only a code number, so people will not know my name or which data belongs to me.',
        widget=widgets.RadioSelectHorizontal)
    consent4 = models.IntegerField(
        choices=[[1, 'Yes']],
        label='I understand that my coded data will be used for scientific research. You can share these data, either directly with other researchers or in a public online repository.',
        widget=widgets.RadioSelectHorizontal)
    optional = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='<b>Optional:</b> <br /> You can contact me in the future for related studies.',
        widget=widgets.RadioSelectHorizontal)
    full_name = models.StringField(
        label='<br />If you have ticked at least the first 4 boxes and want to participate, sign below by typing your name and today’s date. </b> <br /><br /> Full name:',
        blank=False)
    date = models.StringField(
        label='Date:',
        blank=False)   

    nick_name = models.StringField()

    und1 = models.BooleanField()
    und2 = models.BooleanField()
    und3 = models.BooleanField()
    und4 = models.BooleanField()
    und5 = models.BooleanField()
    cund1 = models.BooleanField()
    cund2 = models.BooleanField()
    cund3 = models.BooleanField()
    cund4 = models.BooleanField()
    cund5 = models.BooleanField()

    under = models.BooleanField()
