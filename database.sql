

-- Table: competitions
CREATE TABLE competitions (
    competition_id INT NOT NULL PRIMARY KEY,
    competition_code VARCHAR(10),
    name VARCHAR(255),
    sub_type VARCHAR(50),
    type VARCHAR(50),
    country_id INT,
    country_name VARCHAR(255),
    domestic_league_code VARCHAR(10),
    confederation VARCHAR(50),
    url VARCHAR(255)
);

-- Table: games
CREATE TABLE games (
    game_id INT PRIMARY KEY,
    competition_id INT REFERENCES competitions(competition_id) ON DELETE CASCADE,
    season VARCHAR(10),
    --round VARCHAR(50),
    date DATE,
    home_club_id INT REFERENCES clubs(club_id) ON DELETE CASCADE,
    away_club_id INT REFERENCES clubs(club_id) ON DELETE CASCADE,
    home_club_goals INT,
    away_club_goals INT,
    home_club_position INT,
    away_club_position INT,
    home_club_manager_name VARCHAR(255),
    away_club_manager_name VARCHAR(255),
    stadium VARCHAR(255),
    attendance INT,
    referee VARCHAR(255),
    url VARCHAR(255),
    --home_club_formation VARCHAR(50),
    --away_club_formation VARCHAR(50),
    home_club_name VARCHAR(255),
    away_club_name VARCHAR(255),
    --aggregate BOOLEAN,
);
-- Table: players
CREATE TABLE player (
    player_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    name VARCHAR(255),
    current_club_name VARCHAR(40) REFERENCES clubs(name) ON DELETE CASCADE,
    current_club_id INT REFERENCES clubs(club_id) ON DELETE CASCADE,
    competition_id VARCHAR(4) REFERENCES competitions(competition_id) ON DELETE CASCADE

    
);
CREATE TABLE goals (
    goal_id VARCHAR(40) PRIMARY KEY,
    date DATE,
    game_id INT REFERENCES games(game_id) ON DELETE CASCADE,
    minute INT,
    club_id INT REFERENCES clubs(club_id) ON DELETE CASCADE,
    player_id INT REFERENCES player(player_id) ON DELETE CASCADE,
    description VARCHAR(45)
);

-- Table: player photo
CREATE TABLE player_photo (
    id INT PRIMARY KEY,
    player_id INT  NOT NULL REFERENCES player(id)
        ON DELETE CASCADE 
		ON UPDATE CASCADE,
    image_url VARCHAR(255),
    url VARCHAR(255),
    FOREIGN KEY (player_id) REFERENCES player(id)
);

-- Table: clubs
CREATE TABLE clubs (
    club_id INT NOT NULL PRIMARY KEY,
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
-- Table player attributes
CREATE TABLE player_attributes (
    id INT PRIMARY KEY,
    player_id INT  NOT NULL REFERENCES player(id)
        ON DELETE CASCADE 
		ON UPDATE CASCADE,
    player_code VARCHAR(20),
    sub_position VARCHAR(50),
    position VARCHAR(50),
    foot VARCHAR(10),
    height_in_cm INT,
    market_value_in_eur DECIMAL(15, 2),
    highest_market_value_in_eur DECIMAL(15, 2),
    contract_expiration_date DATE,
);

-- Table player bio
CREATE TABLE player_bio (
    id INT PRIMARY KEY,
    player_id INT  NOT NULL REFERENCES player(id)
        ON DELETE CASCADE 
		ON UPDATE CASCADE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    name VARCHAR(255),
    country_of_birth VARCHAR(255),
    city_of_birth VARCHAR(255),
    country_of_citizenship VARCHAR(255),
    date_of_birth DATE,
);
