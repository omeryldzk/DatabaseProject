from flask import Flask
from flask_login import LoginManager
import views
from database import Database
from models.user import get_user
from models.player import Player

lm = LoginManager()


@lm.user_loader
def load_user(user_id):
    return get_user(user_id)
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
     #######################   PLAYERS   ########################
    app.add_url_rule("/players", view_func=views.players_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<int:competition_id>/", view_func=views.comp_player_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<int:club_id>/", view_func=views.club_player_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<int:player_id>", view_func=views.player_page)
    app.add_url_rule("/add_player", view_func=views.add_player_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<int:player_id>/edit", view_func=views.edit_player_page, methods=["GET", "POST"])
    app.add_url_rule("/player_delete/<int:id>/", view_func=views.delete_player_page)
    #######################   PLAYER ATTRIBUTES ########################
    app.add_url_rule("/players_attributes", view_func=views.players_attributes_page,  methods=["GET", "POST"])
    app.add_url_rule("/player_attributes/<int:player_id>", view_func=views.player_attributes_page)
    app.add_url_rule("/add_player_attributes", view_func=views.add_attributes_page, methods=["GET", "POST"])
    app.add_url_rule("/players_attributes/<int:player_attributes_id>/edit", view_func=views.edit_attributes_page, methods=["GET", "POST"])
    app.add_url_rule("/players_attributes_delete/<int:id>/", view_func=views.delete_attributes_page)
    #######################   PLAYER PHOTOS   ########################
    app.add_url_rule("/players_photos", view_func=views.players_photos_page)
    # app.add_url_rule("/players_photos<int:player_id", view_func=views.player_photo_page)
    #######################   PLAYER BIOS   ########################
    app.add_url_rule("/players_bios", view_func=views.players_bios_page)
    # app.add_url_rule("/players_bios<int:player_id>", view_func=views.player_bio_page)

    #################### CLUBS ###############################
    app.add_url_rule("/clubs", view_func=views.clubs_page, methods=["GET", "POST"])
    app.add_url_rule("/clubs/<int:competition_id>", view_func=views.comp_clubs_page, methods=["GET", "POST"])
    app.add_url_rule("/clubs/<int:club_id>", view_func=views.club_page)
    app.add_url_rule("/clubs/<int:club_id>/edit", view_func=views.club_edit_page, methods=["GET", "POST"])
    app.add_url_rule("/add_club", view_func=views.club_add_page, methods=["GET", "POST"])
    app.add_url_rule("/club_delete/<int:id>/", view_func=views.club_delete_page, methods=["GET", "POST"])
    #################### GAMES ###############################
    app.add_url_rule("/games", view_func=views.games_page, methods=["GET", "POST"])
    app.add_url_rule("/games/<int:club_id>", view_func=views.club_games_page, methods=["GET", "POST"])
    app.add_url_rule("/games/<int:competition_id>", view_func=views.comp_games_page, methods=["GET", "POST"])
    app.add_url_rule("/games/<int:game_id>", view_func=views.game_page)
    app.add_url_rule("/games/<int:game_id>/edit", view_func=views.game_edit_page, methods=["GET", "POST"])
    app.add_url_rule("/add_game", view_func=views.game_add_page, methods=["GET", "POST"])
    app.add_url_rule("/game_delete", view_func=views.game_delete_page)
    #################### SCORES ###############################
    ##app.add_url_rule("/scores/<int:game_id>", view_func=views.scores_page, methods=["GET", "POST"])
    
    app.add_url_rule(
        "/login", view_func=views.login_page, methods=["GET", "POST"]
    )
    app.add_url_rule("/logout", view_func=views.logout_page)
    
    ## user ##
    lm.init_app(app)
    # If a visitor makes a request to a protected page without logging in, we can redirect the request
    # to the login page by setting the login_view property of the login manager 
    lm.login_message = "Please log in to access this page."
    lm.login_message_category = "warning"
    lm.login_view = "login_page"
    
    db_url = "postgres://ylfqputg:xTs4QCLXPs_km6yan6I268VzNUkl3KLb@lucky.db.elephantsql.com/ylfqputg"

    db = Database(db_url)
    app.config["db"] = db
    
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
    