from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Master's thesis experiment - The Game
"""


class Constants(BaseConstants):
    name_in_url = 'thesis_game'
    players_per_group = None
    num_rounds = 24


class Subsession(BaseSubsession):
    def creating_session(self):
        print('Creating session', self.round_number)
        self.session.vars['max_rounds'] = 24
        self.session.vars['break_round'] = 24


class Group(BaseGroup):
    def total_players(self):
        for p in self.get_players():
            p.total_players = len(self.get_players())

    def payoff_decrease(self):
        print('Calculating payoff ...')
        for p in self.get_players():
            p.payoff_left = (240 - (self.subsession.round_number*5))

    def chosen_option(self):
        print('Calculating chosen options ...')
        for p in self.get_players():
            if p.chosen_name == 'Tao':
                p.chose_tao = 1
            elif p.chosen_name == 'Eta':
                p.chose_eta = 1

    def confederate_strategy(self):
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        print('Break-round ...')
        if sum_eta <= 1 or sum_tao <= 1:
            print('     !!!Current round is the break round!!!')
            self.get_player_by_id(1).con_strategy = 1
        for p in self.get_player_by_id(1).in_previous_rounds():
            if p.con_strategy == 1:
                print('     !!!Current round is a post-break round!!!')
                self.get_player_by_id(1).con_strategy = 2

    def break_name(self):
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        if self.get_player_by_id(1).con_strategy == 1:
            if sum_tao <= 1:
                print('     Break name is Tao')
                self.get_player_by_id(1).break_name = 1
            elif sum_eta <= 1:
                print('     Break name is Eta')
                self.get_player_by_id(1).break_name = 2
        for p in self.get_player_by_id(1).in_previous_rounds():
            if p.break_name == 1:
                print('     Break name is Tao')
                self.get_player_by_id(1).break_name = 1
            elif p.break_name == 2:
                print('     Break name is Eta')
                self.get_player_by_id(1).break_name = 2

    def confederate_activity(self):
        con_strategy = self.get_player_by_id(1).con_strategy
        sum_eta = sum([p.chose_eta for p in self.get_players()])
        sum_tao = sum([p.chose_tao for p in self.get_players()])
        break_name = self.get_player_by_id(1).break_name
        total_players = self.get_player_by_id(1).total_players
        print('Strategy ...')
        if con_strategy == 0:
            print('     Stage 1:')
            if sum_eta == sum_tao:
                print('     A) Randomly assigning confederates')
                self.get_player_by_id(3).chose_eta = 1
                if total_players > 4:
                    self.get_player_by_id(5).chose_tao = 1
                if total_players > 8:
                    self.get_player_by_id(9).chose_eta = 1
                if total_players > 12:
                    self.get_player_by_id(13).chose_tao = 1
            elif sum_tao > sum_eta:
                print('     B) Assigning more to Tao')
                self.get_player_by_id(3).chose_tao = 1
                if total_players > 4:
                    self.get_player_by_id(5).chose_eta = 1
                if total_players > 8:
                    self.get_player_by_id(9).chose_tao = 1
                if total_players > 12:
                    self.get_player_by_id(13).chose_tao = 1
            elif sum_tao < sum_eta:
                print('     C) Assigning more to Eta')
                self.get_player_by_id(3).chose_eta = 1
                if total_players > 4:
                    self.get_player_by_id(5).chose_tao = 1
                if total_players > 8:
                    self.get_player_by_id(9).chose_eta = 1
                if total_players > 12:
                    self.get_player_by_id(13).chose_eta = 1
        else:
            print('     Stage 2:')
            if break_name == 1:
                print('     A) Everything Tao now')
                self.get_player_by_id(3).chose_tao = 1
                if total_players > 4:
                    self.get_player_by_id(5).chose_tao = 1
                if total_players > 8:
                    self.get_player_by_id(9).chose_tao = 1
                if total_players > 12:
                    self.get_player_by_id(13).chose_tao = 1
            elif break_name == 2:
                print('     B) Everything Eta now')
                self.get_player_by_id(3).chose_eta = 1
                if total_players > 4:
                    self.get_player_by_id(5).chose_eta = 1
                if total_players > 8:
                    self.get_player_by_id(9).chose_eta = 1
                if total_players > 12:
                    self.get_player_by_id(13).chose_eta = 1

    def same_choice(self):
        print('Comparing choices ...')
        total_players = self.get_player_by_id(1).total_players
        total_choices = sum([p.chose_tao for p in self.get_players()])
        if total_choices == 0 or total_choices == total_players:
            print('     !!!Choices are the same!!!')
            self.session.vars['max_rounds'] = self.subsession.round_number
        else:
            print('     Choices are different')

    def assign_names(self):
        print('Calculating chosen names ...')
        for p in self.get_players():
            if 'player_name' in p.participant.vars:
                if p.chose_tao == 1:
                    p.tao_names = p.participant.vars['player_name']
                else:
                    p.eta_names = p.participant.vars['player_name']


class Player(BasePlayer):
    chosen_name = models.StringField(
        choices=['Tao', 'Eta'], initial='X'
    )

    conf_choice = models.StringField(
        choices=['Tao', 'Eta'],
    )

    total_players = models.IntegerField()
    chose_eta = models.IntegerField(initial=0)
    chose_tao = models.IntegerField(initial=0)
    payoff_left = models.IntegerField(initial=240)
    tao_names = models.StringField(initial='')
    eta_names = models.StringField(initial='')
    con_strategy = models.IntegerField(initial=0)
    break_name = models.IntegerField(initial=0)
    timeChoice = models.FloatField()
    timeResults = models.FloatField()