from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Žan Mlakar'

doc = """
Questionnaires and demographics for thesis.
"""


class Constants(BaseConstants):
    name_in_url = 'thesisquestiondemo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Manipulation checks and game-related questions #
    def gmq(x):
        return models.IntegerField(
            choices=[[1, 'Strongly disagree'], [2, 'Disagree'], [3, 'Neither agree nor disagree'], [4, 'Agree'],
                     [5, 'Strongly agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    game1 = gmq('My New Product endorsements were impulsive.')
    game2 = gmq('I felt like I was being judged by the other participants.')
    game3 = gmq('When making my New Product endorsements, I felt limited by what other employees endorsed.')
    game4 = gmq('I felt a pressure to conform to the majority.')
    game5 = gmq('I thought a lot about the optimal New Product endorsement in each round.')


    # Collectivism scale & Consistency#
    def COL(x):
        return models.IntegerField(
            choices=[[1, 'Totally disagree'], [2, 'Disagree'], [3, 'Neither agree nor disagree'],
                     [4, 'Agree'], [5, 'Totally agree']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    col1 = COL('All individuals in a society are closely related to each other.')
    col2 = COL('Individuals may not be able to survive if there is no group or country.')
    col3 = COL('To ensure group interests are met, self-interests must be sacrificed.')
    col4 = COL('An individual’s talents can be realized only through teamwork/group collaboration.')
    col5 = COL('Individuals should be unconditionally submissive to the group and nation.')
    col6 = COL('The value of a person is determined primarily by assessments of oneself that are made by others and the society.')
    col7 = COL('Every one of us must consult others about how best to act and behave.')
    col8 = COL('It is much more important to help others than it is to mind your own business.')
    col9 = COL('One must conform to the opinion of the majority in work and daily life.')
    con = COL('I make an effort to appear consistent to others.')

    # Impulsivity #
    def IMPULSE(x):
        return models.IntegerField(
            choices=[[1, 'Never'], [2, 'Occasionally'],
                     [3, 'Often'], [4, 'Always']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    IMP1 = IMPULSE('I plan tasks carefully.')
    IMP2 = IMPULSE('I do things without thinking.')
    IMP3 = IMPULSE('I don’t “pay attention”.')
    IMP4 = IMPULSE('I am self-controlled.')
    IMP5 = IMPULSE('I concentrate easily.')
    IMP6 = IMPULSE('I am a careful thinker.')
    IMP7 = IMPULSE('I say things without thinking.')
    IMP8 = IMPULSE('I act on the spur of the moment.')

    #Climate policy support
    def CPS(x):
        return models.IntegerField(
            choices=[[1, '0-10%'], [2, '10-20%'], [3, '20-30%'], [4, '30-40%'], [5, '40-50%'],
            [6, '50-60%'], [7, '60-70%'], [8, '70-80%'], [9, '80-90%'], [10, '90-100%']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    CPS1 = CPS('I support raising carbon taxes on gas/fossil fuels/coal.')
    CPS2 = CPS('I support increasing the use of sustainable energy such as wind and solar energy.')
    CPS3 = CPS('I support increasing taxes on airline companies to offset carbon emissions.')
    CPS4 = CPS('I support protecting forested and land areas.')
    CPS5 = CPS('I support investing more in green jobs and businesses.')
    CPS6 = CPS('I support increasing taxes on carbon intense foods (for example meat and dairy).')

    # Climate Change Worry Scale #
    def CCW(x):
        return models.IntegerField(
            choices=[[1, 'Never'], [2, 'Rarely'], [3, 'Sometimes'], [4, 'Often'],
                     [5, 'Always']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    CCW1 = CCW('I worry about climate change more than other people.')
    CCW2 = CCW('Thoughts about climate change cause me to have worries about what the future may hold.')
    CCW3 = CCW('I tend to seek out information about climate change in the media (e.g., TV, newspapers, internet).')
    CCW4 = CCW('I tend to worry when I hear about climate change, even when the effects of climate change may be some time away.')
    CCW5 = CCW('I worry that outbreaks of severe weather may be the result of a changing climate.')
    CCW6 = CCW('I worry about climate change so much that I feel paralyzed in being able to do anything about it.')
    CCW7 = CCW('I worry that I might not be able to cope with climate change.')
    CCW8 = CCW('I notice that I have been worrying about climate change.')
    CCW9 = CCW('Once I begin to worry about climate change, I find it difficult to stop.')
    CCW10 = CCW('I worry about how climate change may affect the people I care about.')
    
    # Second-order Belief in Climate Change #
    def SOB(x):
        return models.IntegerField(
            choices=[[1, '0-10%'], [2, '10-20%'], [3, '20-30%'], [4, '30-40%'], [5, '40-50%'],
            [6, '50-60%'], [7, '60-70%'], [8, '70-80%'], [9, '80-90%'], [10, '90-100%']],
            label=x,
            widget=widgets.RadioSelect,
            blank=True)
    SOB1 = SOB('Feel at least “somewhat” worried about climate change.')
    SOB2 = SOB('Would support a policy raising carbon taxes on fossil fuel companies.')
    SOB3 = SOB('Would support a 100-percent renewable energy mandate requiring electric utilities to produce 100% of their electricity from renewable energy sources by the year 2035.')
    SOB4 = SOB('Would support generating renewable energy (solar and wind).')

    # Demographics & final questions #
    Tao = models.StringField(label='What can you tell us about the characteristics of the product Tao?',
                            blank=False)
    Eta = models.StringField(label='What can you tell us about the characteristics of the product Eta?',
                            blank=False)
    feed1 = models.StringField(label='Was the presentation of information before and during the game clear?',
                            blank=True)
    feed2 = models.StringField(label='Did you find any part of the game instructions to be (too) complex?',
                            blank=True)
    comments = models.StringField(label='Do you have any final thoughts on the experiment or anything you would like to share with the experimenters?',
                            blank=True)
    know = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='Do you personally know any of the participants that entered the lab at the same time as you?',
        widget=widgets.RadioSelectHorizontal)
    age = models.IntegerField(
        label='What is your current age (in years)?',
        blank=True)
    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer not to declare'],
        label='What is your gender?',
        widget=widgets.RadioSelectHorizontal)
    

