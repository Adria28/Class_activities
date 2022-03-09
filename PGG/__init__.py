from otree.api import *
c = cu

doc = """
Public good game
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_game'
    players_per_group = 4
    num_rounds = 1
    endowment = cu(20)
    multiplier = 2
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * Constants.multiplier / Constants.players_per_group
    )
    for p in players:
        p.payoff = Constants.endowment - p.contribution + group.individual_share
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    set_payoffs = set_payoffs
class Player(BasePlayer):
    contribution = models.CurrencyField(label='Quants punts vols contribuir?', max=Constants.endowment, min=0)
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    title_text = 'Sala de espera'
    body_text = 'Espera a que els altres participants prenguin la seva decisió.'

class Results(Page):
    form_model = 'player'
page_sequence = [Contribute, ResultsWaitPage, Results]
