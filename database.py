
from models.clubs import Club
from models.goals import Goal
from models.competitions import Competitions
from models.games import Games
from models.player import Player
from models.player_bio import PlayerBio
from models.player_attributes import PlayerAttributes
from models.player_photo import PlayerPhoto
import psycopg2 as dbapi2

class Database:
    def __init__(self,db_url):
         self.db_url = db_url
 #######################   COMPETITION   ########################

def get_competition(self, competition_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    competition_code,
                    name,
                    sub_type,
                    type,
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
            country_name,
            domestic_league_code,
            confederation,
            url
        )
        return competition


def get_game(self, game_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT 
                    game_id,
                    competition_id,
                    season,
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
                    home_club_name,
                    away_club_name
                FROM 
                    games
                WHERE (game_id = %s)
            """
            cursor.execute(query, (game_id,))
            if cursor.rowcount == 0:
                return None
            (
                competition_id,
                season,
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
                home_club_name,
                away_club_name
            ) = cursor.fetchone()

    game = Games(
        game_id,
        competition_id,
        season,
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
        home_club_name,
        away_club_name,
    )
    return game

def get_games_of_competition(self, competition_id_in):
    games = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT 
                    *
                FROM 
                    games
                WHERE (games.competition_id = %s)
                """
            cursor.execute(query, (competition_id_in,))
            for game_id, competition_id, season, date, home_club_id, away_club_id, home_club_goals, away_club_goals, home_club_position, away_club_position, stadium, attendance, referee, url, home_club_formation, away_club_formation in cursor:
                games.append(Games(game_id, competition_id, season, date, home_club_id, away_club_id, home_club_goals, away_club_goals, home_club_position, away_club_position,stadium,attendance, referee,url, home_club_formation, away_club_formation))
    return games

def get_games_of_club(self, club_id_in):
    games = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT 
                    *
                FROM 
                    games
                WHERE (games.home_club_id = %s OR games.away_club_id = %s)
                """
            cursor.execute(query, (club_id_in,club_id_in))
            for game_id, competition_id, season, date, home_club_id, away_club_id, home_club_goals, away_club_goals, home_club_position, away_club_position, stadium, attendance, referee, url, home_club_formation, away_club_formation in cursor:
                games.append(Games(game_id, competition_id, season, date, home_club_id, away_club_id, home_club_goals, away_club_goals, home_club_position, away_club_position,stadium,attendance, referee,url, home_club_formation, away_club_formation))
    return games

def add_game(self, game_in):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO games (game_id, competition_id, season, date, home_club_id, away_club_id, home_club_goals, away_club_goals, home_club_position, away_club_position, home_club_manager_name, away_club_manager_name, stadium, attendance, referee, url, home_club_name, away_club_name) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s) RETURNING game_id;"
            cursor.execute(query,(game_in.game_id,game_in.competition_id,game_in.season,game_in.date, game_in.home_club_id, game_in.away_club_id, game_in.home_club_goals, game_in.away_club_goals, game_in.home_club_position, game_in.away_club_position,game_in.home_club_manager_name, game_in.away_club_manager_name, game_in.stadium, game_in.attendance, game_in.referee, game_in.url, game_in.home_club_name, game_in.away_club_name))
            game_key = cursor.fetchone()[0]
    return game_key

def update_game(self,game_id, game_in,):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "UPDATE games SET competition_id = %s, season = %s, date = %s, home_club_id = %s, away_club_id = %s, home_club_goals = %s, away_club_goals = %s, home_club_position =%s, away_club_position =%s,home_club_manager_name = %s, away_club_manager_name = %s, stadium = %s, attendance =%s, referee =%s, url =%s, home_club_name = %s, away_club_name = %s WHERE game_id =%s;"
            cursor.execute(query, (game_in.competition_id, game_in.season, game_in.date, game_in.home_club_id, game_in.away_club_id, game_in.home_club_goals, game_in.away_club_goals, game_in.home_club_position, game_in.away_club_position,game_in.home_club_manager_name, game_in.away_club_manager_name, game_in.stadium, game_in.attendance, game_in.referee, game_in.url,game_in.home_club_name, game_in.away_club_name,game_id))

def delete_game(self, game_no):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "DELETE FROM games WHERE game_id=%s;"
            cursor.execute(query, (game_no,))

def get_goals_of_game(self, game_id_in):
    goals = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "SELECT goal_id, date, game_id, minute, club_name, player_name, description FROM games WHERE game_id=%s;"
            cursor.execute(query, (game_id_in,))
            for goal_id, date, game_id, minute, club_name, player_name, description in cursor:
                goals.append((Goal(goal_id, date, game_id, minute, club_name, player_name, description)))
    return goals

#######################   PLAYERS   ########################

def get_players_of_competition(self, competition_id):
    players = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                        SELECT
                            player_id,
                            first_name,
                            last_name,
                            name,
                            current_club_name,
                            current_club_id,
                            competition_id
                        FROM
                            player
                        WHERE competition_id = %s;
                    """
            cursor.execute(query, (competition_id,))
            for player_id, first_name, last_name, name, current_club_name, current_club_id, competition_id in cursor:
                players.append((Player(player_id, first_name, last_name, name, current_club_name, current_club_id,
                                       competition_id)))
    return players

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
                        current_club_name,
                        current_club_id,
                        competition_id
                    FROM
                        player
                    WHERE current_club_id = %s;
                """
            cursor.execute(query, (club_id,))
            for player_id, first_name, last_name, name, current_club_name, current_club_id, competition_id in cursor:
                players.append((Player(player_id, first_name, last_name, name, current_club_name, current_club_id, competition_id)))
    return players



def get_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    first_name,
                    last_name,
                    name,
                    current_club_name,
                    current_club_id,
                    competition_id
                FROM
                    player
                ORDER BY id;
            """
            cursor.execute(query, (player_id,))
            if cursor.rowcount == 0:
                return None
            (
                first_name,
                last_name,
                name,
                current_club_name,
                current_club_id,
                competition_id,
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        name,
        current_club_name,
        current_club_id,
        competition_id
    )
    return player
def get_players(self):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    id,
                    first_name,
                    last_name,
                    name,
                    current_club_name,
                    current_club_id,
                    competition_id
                FROM
                    player
                ORDER BY id;
            """
            cursor.execute(query)
            if cursor.rowcount == 0:
                return None
            (
                player_id,
                first_name,
                last_name,
                player_name,
                current_club_name,
                current_club_id,
                competition_id,
            ) = cursor.fetchone()

        player = Player(
        player_id,
        first_name,
        last_name,
        player_name,
        current_club_name,
        current_club_id,
        competition_id,
    )
    return player
def get_player_by_name(self, name):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    id,
                    first_name,
                    last_name,
                    name,
                    current_club_name,
                    current_club_id,
                    competition_id
                FROM
                    player
                WHERE
                    name = %s;
            """
            cursor.execute(query, (name,))
            if cursor.rowcount == 0:
                return None
            (
                player_id,
                first_name,
                last_name,
                player_name,
                current_club_name,
                current_club_id,
                competition_id,
            ) = cursor.fetchone()

    player = Player(
        player_id,
        first_name,
        last_name,
        player_name,
        current_club_name,
        current_club_id,
        competition_id,
    )
    return player
def add_player(self, player_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO player (player_id, first_name, last_name, name, current_club_name, current_club_id, competition_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (
                player_data['player_id'],
                player_data['first_name'],
                player_data['last_name'],
                player_data['name'],
                player_data['current_club_name'],
                player_data['current_club_id'],
                player_data['competition_id']
            ))
def update_player(self, player_id, updated_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                UPDATE player
                SET first_name = %s, last_name = %s, name = %s, current_club_name = %s, current_club_id = %s, competition_id = %s
                WHERE player_id = %s;
            """
            cursor.execute(query, (
                updated_data['first_name'],
                updated_data['last_name'],
                updated_data['name'],
                updated_data['current_club_name'],
                updated_data['current_club_id'],
                updated_data['competition_id'],
                player_id
            ))

def delete_player(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = "DELETE FROM player WHERE player_id = %s;"
            cursor.execute(query, (player_id,))


#################### CLUBS ###############################

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

def get_clubs_of_competition(self,competition_id):
    clubs = []
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    *
                FROM
                    clubs
                WHERE domestic_competition_id = %s ORDER BY club_id;
            """
            cursor.execute(query, (competition_id,))
            for club_id, club_code, name, domestic_competition_id,total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage,national_team_players, stadium_name,stadium_seats,net_transfer_record, coach_name, last_season, url in cursor:
                clubs.append((club_id, Club(club_id, club_code, name, domestic_competition_id, total_market_value, squad_size, average_age,foreigners_number, foreigners_percentage, national_team_players, stadium_name, stadium_seats, net_transfer_record, coach_name, last_season, url)))
    return clubs
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
def get_club_name(self, club_id):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = "SELECT name FROM club WHERE (id = %s);"
                cursor.execute(query, (club_id,))
                name = cursor.fetchone()[0]
        return name

def add_club(self, club_in):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """INSERT INTO clubs (club_id, club_code, name, domestic_competition_id)
             VALUES (%s, %s, %s, %s) RETURNING club_id"""
            cursor.execute(query, (club_in.club_id, club_in.club_code, club_in.name, club_in.domestic_competition_id))
            club_key = cursor.fetchone()[0]
    return club_key
def update_club(self, club_id, club):
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = """UPDATE clubs
                SET name = %s, club_code = %s, total_market_value = %s, squad_size = %s, 
                    average_age = %s, foreigners_number = %s, foreigners_percentage = %s,
                    national_team_players = %s, stadium_name = %s, stadium_seats = %s, 
                    net_transfer_record = %s, coach_name = %s, last_season = %s, url = %s
                WHERE club_id = %s;"""
                cursor.execute(query, (club.club_name, club.club_code, club.total_market_value, club.squad_size, club.average_age,
                       club.foreigners_number, club.foreigners_percentage, club.national_team_players,
                       club.stadium_name, club.stadium_seats, club.net_transfer_record, club.coach_name,
                       club.last_season, club.url, club_id))

def get_clubs(self):
        clubs = []
        with dbapi2.connect(self.db_url) as connection:
            with connection.cursor() as cursor:
                query = """
                    SELECT
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
                        clubs;
                """
                cursor.execute(query)
                for (
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
                ) in cursor:
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
                    clubs.append(club)

        return clubs
def delete_club(self, club_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                DELETE FROM clubs WHERE (club_id = %s)
            """
            cursor.execute(query, (club_id,))

            
#######################   PLAYER ATTRIBUTES ########################

def get_player_bio(self, player_id):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                SELECT
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
def add_player_attributes(self, player_attributes_data):
    with dbapi2.connect(self.db_url) as connection:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO player_attributes (player_id, player_code, sub_position, position, foot, height_in_cm, market_value_in_eur, highest_market_value_in_eur, contract_expiration_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (
                player_attributes_data['player_id'],
                player_attributes_data['player_code'],
                player_attributes_data['sub_position'],
                player_attributes_data['position'],
                player_attributes_data['foot'],
                player_attributes_data['height_in_cm'],
                player_attributes_data['market_value_in_eur'],
                player_attributes_data['highest_market_value_in_eur'],
                player_attributes_data['contract_expiration_date']
            ))
            player_key = cursor.fetchone()[0]
    return player_key



