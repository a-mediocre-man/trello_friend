class TrelloList:
    def __init__(self, data: dict):
        self.id = data['id']
        self.name = data['name']
        self.closed = data['closed']
        self.id_board = data['idBoard']
        self.pos = data['pos']
        self.subscribed = data['subscribed']
        self.soft_limit = data['softLimit']
        self.status = data['status']

    def __repr__(self):
        return f'<TrelloList {self.name} {self.id}>'
