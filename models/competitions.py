class Competitions:
    def __init__(self, competition_id, competition_code, name, sub_type, type, country_id, country_name, domestic_league_code, confederation, url):
        self.competition_id = competition_id
        self.competition_code = competition_code
        self.name = name
        self.sub_type = sub_type
        self.type = type
        self.country_id = country_id  #Silinmeli?
        self.country_name = country_name
        self.domestic_league_code = domestic_league_code
        self.confederation = confederation
        self.url = url
