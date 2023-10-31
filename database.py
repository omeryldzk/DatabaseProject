from models.player import Player


class Database:
    def __init__(self):
        self.players = {}
        self._last_player_key = 0

    def add_player(self, player):
        self._last_player_key += 1
        self.players[self._last_player_key] = player
        return self._last_player_key

    def delete_player(self, player_key):
        if player_key in self.players:
            del self.players[player_key]

    def get_player(self, player_key):
        player = self.players.get(player_key)
        if player is None:
            return None
        player_ = Player(player.name, age=player.age)
        return player_

    def get_players(self):
        players = []
        for player_key, player in self.players.items():
            player_ = Player(player.name, age=player.age)
            players.append((player_key, player_))
        return players