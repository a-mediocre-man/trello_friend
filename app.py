from .trello_api import TrelloAPI
from .trello_board import TrelloBoard
from .trello_card import TrelloCard
from .trello_list import TrelloList
from .trello_group import TrelloGroup

class App():
    def __init__(self, token, key, secret):
        self.api = TrellAPI()

    def run(self):
        pass


