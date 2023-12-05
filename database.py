from models.appearance import Appearance
from models.clubs import Club
from models.competitions import Competitions
from models.game_events import GameEvents
from models.game_lineups import GameLineup
from models.games import Games
from models.player_valuations import PlayerValuations
from models.players import Players
from models.club_games import ClubGames

import psycopg2 as dbapi2

class Database:
    def __init__(self,db_url):
         self.db_url = db_url

    def get_appearance(self, appearance_id):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = """
                    SELECT
                        game_id,
                        player_id,
                        player_club_id,
                        player_current_club_id,
                        date,
                        player_name,
                        competition_id,
                        yellow_cards,
                        red_cards,
                        goals,
                        assists,
                        minutes_played
                    FROM
                        appearance
                    WHERE
                        appearance_id = %s;
                """
                cursor.execute(query, (appearance_id,))
                if cursor.rowcount == 0:
                    return None
                (
                    game_id,
                    player_id,
                    player_club_id,
                    player_current_club_id,
                    date,
                    player_name,
                    competition_id,
                    yellow_cards,
                    red_cards,
                    goals,
                    assists,
                    minutes_played,
                ) = cursor.fetchone()

        appearance = Appearance(
            appearance_id,
            game_id,
            player_id,
            player_club_id,
            player_current_club_id,
            date,
            player_name,
            competition_id,
            yellow_cards,
            red_cards,
            goals,
            assists,
            minutes_played,
        )
        return appearance
def get_competition(self, competition_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    competition_code,
                    name,
                    sub_type,
                    type,
                    country_id,
                    country_name,
                    domestic_league_code,
                    confederation,
                    url
                FROM
                    competitions
                WHERE
                    competition_id = %s;
            """
            cursor.execute(query, (competition_id,))
            if cursor.rowcount == 0:
                return None
            (
                competition_code,
                name,
                sub_type,
                type,
                country_id,
                country_name,
                domestic_league_code,
                confederation,
                url
            ) = cursor.fetchone()

        competition = Competitions(
            competition_id,
            competition_code,
            name,
            sub_type,
            type,
            country_id,
            country_name,
            domestic_league_code,
            confederation,
            url
        )
        return competition
def get_game_event(self, game_event_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    date,
                    game_id,
                    minute,
                    type,
                    club_id,
                    player_id,
                    description,
                    player_in_id,
                    player_assist_id
                FROM
                    game_events
                WHERE
                    game_event_id = %s;
            """
            cursor.execute(query, (game_event_id,))
            if cursor.rowcount == 0:
                return None
            (
                date,
                game_id,
                minute,
                type,
                club_id,
                player_id,
                description,
                player_in_id,
                player_assist_id,
            ) = cursor.fetchone()

    game_event = GameEvents(
        game_event_id,
        date,
        game_id,
        minute,
        type,
        club_id,
        player_id,
        description,
        player_in_id,
        player_assist_id,
    )
    return game_event
def get_game_lineup(self, game_lineup_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    game_id,
                    club_id,
                    type,
                    number,
                    player_id,
                    player_name,
                    team_captain,
                    position
                FROM
                    game_lineups
                WHERE
                    game_lineup_id = %s;
            """
            cursor.execute(query, (game_lineup_id,))
            if cursor.rowcount == 0:
                return None
            (
                game_id,
                club_id,
                type,
                number,
                player_id,
                player_name,
                team_captain,
                position
            ) = cursor.fetchone()

    game_lineup = GameLineup(
        game_lineup_id,
        game_id,
        club_id,
        type,
        number,
        player_id,
        player_name,
        team_captain,
        position
    )
    return game_lineup
def get_game(self, game_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    competition_id,
                    season,
                    round,
                    date,
                    home_club_id,
                    away_club_id,
                    home_club_goals,
                    away_club_goals,
                    home_club_position,
                    away_club_position,
                    home_club_manager_name,
                    away_club_manager_name,
                    stadium,
                    attendance,
                    referee,
                    url,
                    home_club_formation,
                    away_club_formation,
                    home_club_name,
                    away_club_name,
                    aggregate,
                    competition_type
                FROM
                    games
                WHERE
                    game_id = %s;
            """
            cursor.execute(query, (game_id,))
            if cursor.rowcount == 0:
                return None
            (
                competition_id,
                season,
                round,
                date,
                home_club_id,
                away_club_id,
                home_club_goals,
                away_club_goals,
                home_club_position,
                away_club_position,
                home_club_manager_name,
                away_club_manager_name,
                stadium,
                attendance,
                referee,
                url,
                home_club_formation,
                away_club_formation,
                home_club_name,
                away_club_name,
                aggregate,
                competition_type
            ) = cursor.fetchone()

    game = Games(
        game_id,
        competition_id,
        season,
        round,
        date,
        home_club_id,
        away_club_id,
        home_club_goals,
        away_club_goals,
        home_club_position,
        away_club_position,
        home_club_manager_name,
        away_club_manager_name,
        stadium,
        attendance,
        referee,
        url,
        home_club_formation,
        away_club_formation,
        home_club_name,
        away_club_name,
        aggregate,
        competition_type
    )
    return game
