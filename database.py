
from models.clubs import Club
from models.competitions import Competitions

from models.game_lineups import GameLineup
from models.games import Games
from models.player_valuations import PlayerValuations
from models.players import Players
import psycopg2 as dbapi2

class Database:
    def __init__(self,db_url):
         self.db_url = db_url

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
def get_player_valuation(self, player_valuation_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    player_id,
                    last_season,
                    datetime,
                    date,
                    dateweek,
                    market_value_in_eur,
                    n,
                    current_club_id,
                    player_club_domestic_competition_id
                FROM
                    player_valuations
                WHERE
                    player_valuation_id = %s;
            """
            cursor.execute(query, (player_valuation_id,))
            if cursor.rowcount == 0:
                return None
            (
                player_id,
                last_season,
                datetime,
                date,
                dateweek,
                market_value_in_eur,
                n,
                current_club_id,
                player_club_domestic_competition_id
            ) = cursor.fetchone()

    player_valuation = PlayerValuations(
        player_valuation_id,
        player_id,
        last_season,
        datetime,
        date,
        dateweek,
        market_value_in_eur,
        n,
        current_club_id,
        player_club_domestic_competition_id
    )
    return player_valuation
def get_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                    last_season,
                    current_club_id,
                    player_code,
                    country_of_birth,
                    city_of_birth,
                    country_of_citizenship,
                    date_of_birth,
                    sub_position,
                    position,
                    foot,
                    height_in_cm,
                    market_value_in_eur,
                    highest_market_value_in_eur,
                    contract_expiration_date,
                    agent_name,
                    image_url,
                    url,
                    current_club_domestic_competition_id,
                    current_club_name
                FROM
                    players
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                first_name,
                last_name,
                name,
                last_season,
                current_club_id,
                player_code,
                country_of_birth,
                city_of_birth,
                country_of_citizenship,
                date_of_birth,
                sub_position,
                position,
                foot,
                height_in_cm,
                market_value_in_eur,
                highest_market_value_in_eur,
                contract_expiration_date,
                agent_name,
                image_url,
                url,
                current_club_domestic_competition_id,
                current_club_name
            ) = cursor.fetchone()

    player = Players(
        player_id,
        first_name,
        last_name,
        name,
        last_season,
        current_club_id,
        player_code,
        country_of_birth,
        city_of_birth,
        country_of_citizenship,
        date_of_birth,
        sub_position,
        position,
        foot,
        height_in_cm,
        market_value_in_eur,
        highest_market_value_in_eur,
        contract_expiration_date,
        agent_name,
        image_url,
        url,
        current_club_domestic_competition_id,
        current_club_name
    )
    return player
def get_club(self, club_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    club_code,
                    name,
                    domestic_competition_id,
                    total_market_value,
                    squad_size,
                    average_age,
                    foreigners_number,
                    foreigners_percentage,
                    national_team_players,
                    stadium_name,
                    stadium_seats,
                    net_transfer_record,
                    coach_name,
                    last_season,
                    url
                FROM
                    clubs
                WHERE
                    club_id = %s;
            """
            cursor.execute(query, (club_id,))
            if cursor.rowcount == 0:
                return None
            (
                club_code,
                name,
                domestic_competition_id,
                total_market_value,
                squad_size,
                average_age,
                foreigners_number,
                foreigners_percentage,
                national_team_players,
                stadium_name,
                stadium_seats,
                net_transfer_record,
                coach_name,
                last_season,
                url
            ) = cursor.fetchone()

    club = Club(
        club_id,
        club_code,
        name,
        domestic_competition_id,
        total_market_value,
        squad_size,
        average_age,
        foreigners_number,
        foreigners_percentage,
        national_team_players,
        stadium_name,
        stadium_seats,
        net_transfer_record,
        coach_name,
        last_season,
        url
    )
    return club
