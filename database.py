
from models.clubs import Club
from models.competitions import Competitions
from models.game_lineups import GameLineup
from models.games import Games
from models.player import Player
from models.player_bio import PlayerBio
from models.player_attributes import PlayerAttributes
from models.player_photo import PlayerPhoto
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

def get_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                FROM
                    player
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
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        name
    )
    return player

def get_players_of_club(self,club_id):
    players = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
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
                FROM
                    players
                WHERE current_club_id = %s;
            """
            cursor.execute(query,(club_id,))
            for player_id, first_name, last_name, name, last_season, current_club_id, player_code, country_of_birth, city_of_birth, country_of_citizenship, date_of_birth, sub_position, position, foot, height_in_cm, market_value_in_eur, highest_market_value_in_eur, contract_expiration_date, agent_name, image_url, url, current_club_domestic_competition_id, current_club_name in cursor:
                players.append((Players(player_id, first_name, last_name, name, last_season, current_club_id, player_code, country_of_birth, city_of_birth, country_of_citizenship, date_of_birth, sub_position, position, foot, height_in_cm,market_value_in_eur, highest_market_value_in_eur, contract_expiration_date, agent_name, image_url, url, current_club_domestic_competition_id, current_club_name)))
    return players

def add_player(self, player):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO players (first_name, last_name) VALUES (%s, %s)"
            cursor.execute(query, (player.first_name, player.last_name))
            player_key = cursor.lastrowid
    return player_key

def delete_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                DELETE FROM players WHERE (player_id = %s)
            """
            cursor.execute(query, (player_id,))

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
<<<<<<< HEAD

def get_clubs_of_competition(self,competition_id):
    clubs = []
=======
def get_player_bio(self, player_id):
>>>>>>> bfec1f754e41acf360db41eaa13287225af706c7
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
<<<<<<< HEAD
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
                FROM
                    clubs
                WHERE domestic_competition_id = %s ORDER BY club_id;
            """
            cursor.execute(query, (competition_id,))
            for club_id, club_code, name, domestic_competition_id,total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage,national_team_players, stadium_name,stadium_seats,net_transfer_record, coach_name, last_season, url in cursor:
                clubs.append((club_id, Club(club_id, club_code, name, domestic_competition_id, total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name, last_season, url)))
    return clubs
=======
                    first_name,
                    last_name,
                    name,
                    country_of_birth,
                    city_of_birth,
                    country_of_citizenship,
                    date_of_birth
                FROM
                    player_bio
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
                country_of_birth,
                city_of_birth,
                country_of_citizenship,
                date_of_birth
            ) = cursor.fetchone()

    player_bio = PlayerBio(
        player_id,
        first_name,
        last_name,
        name,
        country_of_birth,
        city_of_birth,
        country_of_citizenship,
        date_of_birth
    )
    return player_bio
def get_player_attributes(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    player_code,
                    sub_position,
                    position,
                    foot,
                    height_in_cm,
                    market_value_in_eur,
                    highest_market_value_in_eur,
                    contract_expiration_date
                FROM
                    player_attributes
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                player_code,
                sub_position,
                position,
                foot,
                height_in_cm,
                market_value_in_eur,
                highest_market_value_in_eur,
                contract_expiration_date
            ) = cursor.fetchone()

    player_attributes = PlayerAttributes(
        player_id,
        player_code,
        sub_position,
        position,
        foot,
        height_in_cm,
        market_value_in_eur,
        highest_market_value_in_eur,
        contract_expiration_date
    )
    return player_attributes
def get_player_photo(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    image_url,
                    url
                FROM
                    player_photo
                WHERE
                    player_id = %s;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                image_url,
                url
            ) = cursor.fetchone()

    player_photo = PlayerPhoto(
        player_id,
        image_url,
        url
    )
    return player_photo
>>>>>>> bfec1f754e41acf360db41eaa13287225af706c7

def get_clubs_by_search(self, search_word):
    clubs = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """SELECT * FROM clubs WHERE club_id::text LIKE %s OR club_code LIKE %s OR clubs.name LIKE %s ORDER BY club_id;"""
            search_word = "%" + search_word + "%"
            cursor.execute(query, (search_word, search_word, search_word,))
            if cursor.rowcount == 0:
                return None
            for club_id, club_code, name, domestic_competition_id, total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name, last_season, url in cursor:
                clubs.append((club_id, Club(club_id,club_code, name,domestic_competition_id,total_market_value,squad_size,average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name,last_season, url)))
    return clubs

def add_club(self, club_in):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """INSERT INTO clubs (club_id, club_code, name, domestic_competition_id)
             VALUES (%s, %s, %s, %s) RETURNING club_id"""
            cursor.execute(query, (club_in.club_id, club_in.club_code, club_in.name, club_in.domestic_competition_id))
            club_key = cursor.fetchone()[0]
    return club_key
def delete_club(self, club_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                DELETE FROM clubs WHERE (club_id = %s)
            """
            cursor.execute(query, (club_id,))