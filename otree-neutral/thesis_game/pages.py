from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    def is_displayed(self):
        return not self.player.id_in_group == 3 and not self.player.id_in_group == 5 and not \
                    self.player.id_in_group == 9 and not self.player.id_in_group == 13\
                    and self.subsession.round_number <= self.session.vars['max_rounds']

    def vars_for_template(self):
        if self.round_number == 1:
            return {'group_payoff': self.player.payoff_left}
        else:
            return {'group_payoff': self.player.in_round(self.round_number - 1).payoff_left}

    form_model = 'player'
    form_fields = ['chosen_name','timeChoice',]

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.subsession.round_number <= self.session.vars['max_rounds']

    def after_all_players_arrive(self):
        self.group.total_players()
        self.group.payoff_decrease()
        self.group.chosen_option()
        self.group.confederate_strategy()
        self.group.break_name()
        self.group.confederate_activity()
        self.group.same_choice()
        self.group.assign_names()


class Results(Page):
    def is_displayed(self):
        return self.subsession.round_number <= self.session.vars['max_rounds']

    def vars_for_template(self):
        return {
            'chose_tao':
                round((sum([p.chose_tao for p in self.group.get_players()]) / self.player.total_players) * 100, 2),
            'chose_eta':
                round((sum([p.chose_eta for p in self.group.get_players()]) / self.player.total_players) * 100, 2),
            'names_tao':
                ([p.tao_names for p in self.group.get_players() if p.tao_names is not None]),
            'names_eta':
                ([p.eta_names for p in self.group.get_players() if p.eta_names is not None])
        }
    form_model = 'player'
    form_fields = ['timeResults',]


class QuestionC(Page):
    def is_displayed(self):
        return (self.player.id_in_group == 3 or self.player.id_in_group == 5 or
                self.player.id_in_group == 9 or self.player.id_in_group == 13) \
                and self.subsession.round_number <= self.session.vars['max_rounds']

    form_model = 'player'
    form_fields = ['conf_choice','timeChoice',]


page_sequence = [
    Choice,
    QuestionC,
    ResultsWaitPage,
    Results
]
