class ClubGames:
    def __init__(self, game_id, club_id, own_goals, own_position, own_manager_name, opponent_id, opponent_goals, opponent_position, opponent_manager_name, hosting, is_win):
        self.game_id = game_id
        self.club_id = club_id
        self.own_goals = own_goals
        self.own_position = own_position
        self.own_manager_name = own_manager_name
        self.opponent_id = opponent_id
        self.opponent_goals = opponent_goals
        self.opponent_position = opponent_position
        self.opponent_manager_name = opponent_manager_name
        self.hosting = hosting
        self.is_win = is_win
