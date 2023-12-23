from datetime import datetime
from flask import current_app, render_template, redirect, request, url_for,flash,abort
from passlib.hash import pbkdf2_sha256 as hasher
from forms import LoginForm,PlayerAttributesForm,PlayerForm,ClubForm
from psycopg2 import Error, errors
from models.user import get_user
from models.player import Player
from models.clubs import Club
from models.competitions import Competitions
from models.game_lineups import GameLineup
from models.games import Games
from models.player_bio import PlayerBio
from models.player_attributes import PlayerAttributes
from models.player_photo import PlayerPhoto
from flask_login import current_user, logout_user,login_user,login_required
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

################################ PLAYER ########################################

@login_required
def add_player_page():
    if not current_user.is_admin:
        abort(401)  # “Unauthorized” error

    form = PlayerAttributesForm()
    db = current_app.config["db"]

    if form.validate_on_submit():
        name = form.data["name"]
        first_name = form.data["first_name"]
        last_name = form.data["last_name"]

        player = Player(
            id=0,  # Assuming you set id to 0 for a new player
            name=name,
            first_name=first_name,
            last_name=last_name,
        )

        try:
            db.add_player(player)  # Adjust this based on your actual method to add a player
        except Error as e:
            if isinstance(e, errors.ForeignKeyViolation):
                flash("There is no related team!", "danger")
                return render_template("add_player.html", form=form)
            # Handle other errors as needed

        flash("Player is added.", "success")
        return redirect(url_for("players_page"))

    return render_template("add_player.html", form=form)
@login_required
def delete_player_page(id):
    if not current_user.is_admin:
        abort(401) # “Unauthorized” error
    db = current_app.config["db"]
    db.delete_player(id)
    players = db.get_players()
    flash("Player deleted","success ")
    return render_template("players.html", players = players)

@login_required
def edit_player_page(player_id):
    if not current_user.is_admin:
        abort(401)  # “Unauthorized” error
    db = current_app.config["db"]
    player = db.get_player(player_id)
    if player is None:
        abort(404)
    form = PlayerForm()
    if form.validate_on_submit():
        name = form.data["name"]
        first_name = form.data["first_name"]
        last_name = form.data["last_name"]
        updated_player = Player(
            id=player.id,
            name=name,
            first_name=first_name,
            last_name=last_name,
        )
        try:
            db.update_player(player_id, updated_player)  
        except Error as e:
            if isinstance(e, errors.UniqueViolation):
                flash("Values must be unique!", "danger")
            return render_template("player_edit.html", form=form)
        flash("Player is updated.", "success")
        return redirect(url_for("player_page", player_id=player_id))
    form.name.data = player.name
    form.first_name.data = player.first_name
    form.last_name.data = player.last_name
    return render_template("player_edit.html", form=form)
def players_page():
    db = current_app.config["db"]
    if request.method == "GET":
        players = db.get_players()
        return render_template("players.html", players=sorted(players))
    else:
        form_player_keys = request.form.getlist("player_keys")
        for form_player_keys in form_player_keys:
            db.delete_player(int(form_player_keys))
        return redirect(url_for("players_page"))
    
def player_page(player_key):
    db = current_app.config["db"]
    player = db.get_player(player_key)
    return render_template("player.html", player=player)
################################ PLAYER ATTRIBUTES ########################################
def players_attributes_page():
    db = current_app.config["db"]
    if request.method == "GET":
        player_attributes = db.get_players_attributes()
        return render_template("player_attributes.html", player_attributes=player_attributes)
    else:
        player_attributes_to_delete = request.form.get("player_attributes_to_delete")
        db.delete_player_attributes(int(player_attributes_to_delete))
        flash("Player attributes are deleted.", "success")
        return redirect(url_for("players_attributes_page"))
def player_attributes_page(player_id):
    db = current_app.config["db"]
    player_attributes = db.get_player_attributes(player_id)
    if player_attributes is None:
        abort(404)  #HTTP “Not Found” (404) error.
    return render_template("individual_player_attributes.html", player_attributes=player_attributes)
@login_required
def edit_attributes_page(attributes_id):
    if not current_user.is_admin:
        abort(401)  # “Unauthorized” error

    db = current_app.config["db"]
    attributes = db.get_player_attributes(attributes_id)

    if attributes is None:
        abort(404)

    form = PlayerAttributesForm()

    if form.validate_on_submit():
        # Adjust the form field names based on your actual form structure
        sub_position = form.data["sub_position"]
        position = form.data["position"]
        foot = form.data["foot"]
        height_in_cm = form.data["height_in_cm"]
        market_value_in_eur = form.data["market_value_in_eur"]
        highest_market_value_in_eur = form.data["highest_market_value_in_eur"]
        contract_expiration_date = form.data["contract_expiration_date"]

        updated_attributes = PlayerAttributes(
            id=attributes.id,
            player_code=attributes.player_code,
            sub_position=sub_position,
            position=position,
            foot=foot,
            height_in_cm=height_in_cm,
            market_value_in_eur=market_value_in_eur,
            highest_market_value_in_eur=highest_market_value_in_eur,
            contract_expiration_date=contract_expiration_date,
        )

        try:
            db.update_player_atr(attributes_id, updated_attributes)
        except Error as e:
            if isinstance(e, errors.UniqueViolation):
                flash("Values must be unique!", "danger")
            return render_template("attributes_edit.html", form=form)

        flash("Attributes are updated.", "success")
        return redirect(url_for("attributes_page", attributes_id=attributes_id))

    form.sub_position.data = attributes.sub_position
    form.position.data = attributes.position
    form.foot.data = attributes.foot
    form.height_in_cm.data = attributes.height_in_cm
    form.market_value_in_eur.data = attributes.market_value_in_eur
    form.highest_market_value_in_eur.data = attributes.highest_market_value_in_eur
    form.contract_expiration_date.data = attributes.contract_expiration_date

    return render_template("attributes_edit.html", form=form)

@login_required
def delete_attributes_page(attributes_id):
    if not current_user.is_admin:
        abort(401)  # “Unauthorized” error

    db = current_app.config["db"]
    attributes = db.get_player_attributes(attributes_id)

    if attributes is None:
        abort(404)

    try:
        db.delete_player_attributes(attributes_id)
    except Error as e:
        flash("Error deleting attributes.", "danger")
        return redirect(url_for("attributes_page", attributes_id=attributes_id))

    flash("Attributes deleted.", "success")
    return redirect(url_for("attributes_page"))

@login_required
def add_attributes_page():
    if not current_user.is_admin:
        abort(401)  # “Unauthorized” error

    form = PlayerAttributesForm()
    db = current_app.config["db"]

    if form.validate_on_submit():
        # Adjust the form field names based on your actual form structure
        player_code = form.data["player_code"]
        sub_position = form.data["sub_position"]
        position = form.data["position"]
        foot = form.data["foot"]
        height_in_cm = form.data["height_in_cm"]
        market_value_in_eur = form.data["market_value_in_eur"]
        highest_market_value_in_eur = form.data["highest_market_value_in_eur"]
        contract_expiration_date = form.data["contract_expiration_date"]

        attributes = PlayerAttributes(
            id=0,  # Assuming you set id to 0 for a new set of attributes
            player_code=player_code,
            sub_position=sub_position,
            position=position,
            foot=foot,
            height_in_cm=height_in_cm,
            market_value_in_eur=market_value_in_eur,
            highest_market_value_in_eur=highest_market_value_in_eur,
            contract_expiration_date=contract_expiration_date,
        )

        try:
            db.add_player_attributes(attributes)
        except Error as e:
            flash("Error adding attributes.", "danger")
            return render_template("attributes_add.html", form=form)

        flash("Attributes added.", "success")
        return redirect(url_for("attributes_page"))

    return render_template("attributes_add.html", form=form)

def players_photos_page():
    db = current_app.config["db"]
    player_photos = db.get_player_photo()
    return render_template("player_photos.html", player_photos=player_photos)

def players_bios_page():
    db = current_app.config["db"]
    player_bios = db.get_player_bio()
    return render_template("player_bios.html", player_bios=player_bios)

################################ CLUBS ########################################

def clubs_page(competition_id):
    db = current_app.config["db"]
    if request.method == "GET":
        clubs = db.get_clubs_of_competition(competition_id)
        return render_template("clubs.html", clubs=clubs)
    else:
        search = request.form.get("search")
        if search:
            clubs = db.get_clubs_by_search(search)
            if clubs == None:
                flash("NO RESULTS FOUND", "warning")
                clubs = db.get_clubs_of_competition(competition_id)
                return render_template("clubs.html", clubs=clubs)
            else:
                flash("RESULTS FOUND:", "success")
                return render_template("clubs.html", clubs=clubs)
        if not current_user.is_admin:
            abort(401)
        form_club_id_list = request.form.getlist("club_ids")
        for form_club_id in form_club_id_list:
            db.delete_club(int(form_club_id))
            flash("Club has been deleted", "success")
        return redirect(url_for("clubs_page"))
def club_page(club_id):
    db = current_app.config["db"]
    club = db.get_club(club_id)
    if club is None:
        abort(404)  #HTTP “Not Found” (404) error.
    return render_template("club_spesific.html", club=club)

@login_required
def club_add_page():
    # Check if the current user is an admin
    if not current_user.is_admin:
        abort(401)  # Unauthorized error

    # Create an instance of the ClubEditForm
    form = ClubForm()

    # Access the database from the Flask app configuration
    db = current_app.config["db"]

    # Validate the form on submission
    if form.validate_on_submit():
        # Extract form data
        club_code = form.data["clubCode"]
        name = form.data["name"]
        domestic_competition_id = form.data["domesticCompetitionId"]
        total_market_value = form.data["totalMarketValue"]
        squad_size = form.data["squadSize"]
        average_age = form.data["averageAge"]
        foreigners_number = form.data["foreignersNumber"]
        foreigners_percentage = form.data["foreignersPercentage"]
        national_team_players = form.data["nationalTeamPlayers"]
        stadium_name = form.data["stadiumName"]
        stadium_seats = form.data["stadiumSeats"]
        net_transfer_record = form.data["netTransferRecord"]
        coach_name = form.data["coachName"]
        last_season = form.data["lastSeason"]
        url = form.data["url"]

        # Create a Club instance
        club = Club(
            club_id=0,
            club_code=club_code,
            name=name,
            domestic_competition_id=domestic_competition_id,
            total_market_value=total_market_value,
            squad_size=squad_size,
            average_age=average_age,
            foreigners_number=foreigners_number,
            foreigners_percentage=foreigners_percentage,
            national_team_players=national_team_players,
            stadium_name=stadium_name,
            stadium_seats=stadium_seats,
            net_transfer_record=net_transfer_record,
            coach_name=coach_name,
            last_season=last_season,
            url=url
        )

        try:
            # Add the Club to the database
            db.add_club(club)
        except Error as e:
            if isinstance(e, errors.ForeignKeyViolation):
                flash("There is an issue with foreign key constraints!", "danger")
            return render_template("club_add.html", form=form)
        
        flash("Club added successfully!", "success")
        return redirect(url_for("clubs_page"))

    return render_template("club_add.html", form=form)

@login_required
def club_edit_page(club_id):
    # Check if the current user is an admin
    if not current_user.is_admin:
        abort(401)  # Unauthorized error

    # Access the database from the Flask app configuration
    db = current_app.config["db"]

    # Retrieve the club from the database
    club = db.get_club(club_id)

    # Check if the club exists
    if not club:
        flash("Club not found!", "danger")
        return redirect(url_for("clubs_page"))

    # Create an instance of the ClubEditForm and populate it with the current club data
    form = ClubForm(obj=club)

    # Validate the form on submission
    if form.validate_on_submit():
        # Update club data with form data
        form.populate_obj(club)

        try:
            # Update the Club in the database
            db.update_club(club_id,club)
        except Error as e:
            if isinstance(e, errors.ForeignKeyViolation):
                flash("There is an issue with foreign key constraints!", "danger")
            return render_template("club_edit.html", form=form, club_id=club_id)

        flash("Club updated successfully!", "success")
        return redirect(url_for("clubs_page"))

    return render_template("club_edit.html", form=form, club_id=club_id)

@login_required
def club_delete_page(club_id):
    # Check if the current user is an admin
    if not current_user.is_admin:
        abort(401)  # Unauthorized error

    # Access the database from the Flask app configuration
    db = current_app.config["db"]

    # Retrieve the club from the database
    club = db.get_club(club_id)

    # Check if the club exists
    if not club:
        flash("Club not found!", "danger")
        return redirect(url_for("clubs_page"))

    # Delete the Club from the database
    db.delete_club(club_id)

    flash("Club deleted successfully!", "success")
    return redirect(url_for("clubs_page"))
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = get_user(username)
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))