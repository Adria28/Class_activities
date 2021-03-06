from os import environ

SESSION_CONFIGS = [
    dict(
        name='prisoner',
        display_name="Dilema dels presoners",
        app_sequence=['prisoners_dilemma'],
        num_demo_participants=2,
     ),

    dict(
        name='prisoner_2',
        display_name="Dilema dels presoners comunicació",
        app_sequence=['prisoners_dilemma_game'],
        num_demo_participants=2,
    ),
    dict(
        name='public_goods_game',
        display_name="Joc de béns públics",
        app_sequence=['PGG'],
        num_demo_participants=4,
    ),
    dict(
        name='punishment',
        display_name="Joc de béns públics amb càstig",
        app_sequence=['PGG2'],
        num_demo_participants=4,
    )
]

ROOMS = [
    dict(
        name="PD",
        display_name='PD',
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5865393231915'
