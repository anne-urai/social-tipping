#Code that assigns chosen names to a global variable
def assign_name(self):
    for p in self.get_players():
        global chosen_name
        chosen_name = p.chosen_name

#Code that tests whether those names are the same
def test_choice(self):
    if len(set(chosen_name)) == 1:
        print('Choices are the same')
        self.session.vars['max_rounds'] = self.subsession.round_number
    else:
        print('Choices are different')