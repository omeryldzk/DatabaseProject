from datetime import datetime
from flask import current_app, render_template, redirect, request, url_for,flash,abort
from models.player import Player
from passlib.hash import pbkdf2_sha256 as hasher
from forms import LoginForm 
from models.user import get_user
from flask_login import current_user, logout_user,login_user
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


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
def player_add_page():
    if request.method == "GET":
        values = {"name": "", "age": ""}
        return render_template(
            "player_edit.html",
            min_year=18,
            max_year=49,
            values=values,
        )
    else:
        valid = validate_player_form(request.form)
        if not valid:
            return render_template(
                "player_edit.html",
                min_year=18,
                max_year=49,
                values=request.form,
            )
        name = request.form.data["name"]
        age = request.form.data["age"]
        player = Player(name, age=age)
        db = current_app.config["db"]
        player_key = db.add_player(player)
        return redirect(url_for("player_page", player_key=player_key))
def validate_player_form(form):
    form.data = {}
    form.errors = {}

    form_name = form.get("name", "").strip()
    if len(form_name) == 0:
        form.errors["name"] = "Name can not be blank."
    else:
        form.data["name"] = form_name

    form_age = form.get("age")
    if not form_age:
        form.data["age"] = None
    elif not form_age.isdigit():
        form.errors["year"] = "Age must consist of digits only."
    else:
        age = int(form_age)
        if (age < 18) or (age > 49):
            form.errors["age"] = "Year not in valid range."
        else:
            form.data["age"] = age

    return len(form.errors) == 0

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