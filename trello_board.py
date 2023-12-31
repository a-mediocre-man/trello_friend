class TrelloBoard:
    def __init__(self, data: dict):
        self.id = data['id']
        self.node_id = data['nodeId']
        self.name = data['name']
        self.desc = data['desc']
        self.desc_data = data['descData']
        self.closed = data['closed']
        self.date_closed = data['dateClosed']
        self.id_organization = data['idOrganization']
        self.id_enterprise = data['idEnterprise']
        self.limits = data['limits']
        self.pinned = data['pinned']
        self.starred = data['starred']
        self.url = data['url']
        self.prefs = data['prefs']
        self.short_link = data['shortLink']
        self.subscribed = data['subscribed']
        self.label_names = data['labelNames']
        self.power_ups = data['powerUps']
        self.date_last_activity = data['dateLastActivity']
        self.date_last_view = data['dateLastView']
        self.short_url = data['shortUrl']
        self.id_tags = data['idTags']
        self.date_plugin_disable = data['datePluginDisable']
        self.creation_method = data['creationMethod']
        self.ix_update = data['ixUpdate']
        self.template_gallery = data['templateGallery']
        self.enterprise_owned = data['enterpriseOwned']
        self.id_board_source = data['idBoardSource']
        self.premium_features = data['premiumFeatures']
        self.id_member_creator = data['idMemberCreator']
        self.memberships = data['memberships']

    def __repr__(self):
        return f'<TrelloBoard {self.name} ({self.id})>'
