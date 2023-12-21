

-- Table: competitions
CREATE TABLE competitions (
    competition_id INT PRIMARY KEY,
    competition_code VARCHAR(10),
    name VARCHAR(255),
    sub_type VARCHAR(50),
    type VARCHAR(50),
    country_name VARCHAR(255),
    domestic_league_code VARCHAR(10),
    confederation VARCHAR(50),
    url VARCHAR(255)
);

-- Table: games
CREATE TABLE games (
    game_id INT PRIMARY KEY,
    competition_id INT REFERENCES competitions(competition_id),
    season VARCHAR(10),
    round VARCHAR(50),
    date DATE,
    home_club_id INT REFERENCES clubs(club_id),
    away_club_id INT REFERENCES clubs(club_id),
    home_club_goals INT,
    away_club_goals INT,
    home_club_position INT,
    away_club_position INT,
    stadium VARCHAR(255),
    attendance INT,
    referee VARCHAR(255),
    url VARCHAR(255),
    home_club_formation VARCHAR(50),
    away_club_formation VARCHAR(50),
    aggregate BOOLEAN,
);

-- Table: game_lineups
CREATE TABLE game_lineups (
    game_lineups_id INT PRIMARY KEY,
    game_id INT REFERENCES games(game_id),
    club_id INT REFERENCES clubs(club_id),
    type VARCHAR(50),
    number INT,
    player_id INT REFERENCES players(player_id),
    team_captain BOOLEAN,
    position VARCHAR(50)
);

-- Table: players
CREATE TABLE player (
    player_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    last_season VARCHAR(10),
    current_club_id INT REFERENCES clubs(club_id),
    country_of_birth VARCHAR(255),
    country_of_citizenship VARCHAR(255),
    date_of_birth DATE,
    position VARCHAR(50),
    foot VARCHAR(10),
    height_in_cm INT,
    market_value_in_eur DECIMAL(15, 2),
    highest_market_value_in_eur DECIMAL(15, 2),
    contract_expiration_date DATE,
    image_url VARCHAR(255),
    url VARCHAR(255),

);
-- Table: clubs
CREATE TABLE clubs (
    club_id INT PRIMARY KEY,
    club_code VARCHAR(10),
    name VARCHAR(255),
    domestic_competition_id INT REFERENCES competitions(competition_id),
    total_market_value DECIMAL(15, 2),
    squad_size INT,
    average_age DECIMAL(5, 2),
    foreigners_number INT,
    foreigners_percentage DECIMAL(5, 2),
    national_team_players INT,
    stadium_name VARCHAR(255),
    stadium_seats INT,
    net_transfer_record DECIMAL(15, 2),
    coach_name VARCHAR(255),
    last_season VARCHAR(10),
    url VARCHAR(255)
);

