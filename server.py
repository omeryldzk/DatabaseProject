from flask import Flask
from flask_login import LoginManager
import views
from database import Database
from models.user import get_user
from models.players import Player

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
    app.add_url_rule("/players/<int:player_id>", view_func=views.player_page)
    app.add_url_rule("/add_player", view_func=views.add_player_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<int:player_id>/edit", view_func=views.edit_player_page, methods=["GET", "POST"])
    app.add_url_rule("/player_delete/<int:id>/", view_func=views.delete_player_page)
    #######################   PLAYER ATTRIBUTES ########################
    app.add_url_rule("/players_attributes", view_func=views.players_attributes_page,  methods=["GET", "POST"])
    app.add_url_rule("/player_attributes/<int:player_id>", view_func=views.player_attributes_page)
    app.add_url_rule("/add_player_attributes", view_func=views.add_player_attributes_page, methods=["GET", "POST"])
    app.add_url_rule("/players_attributes/<int:player_attributes_id>/edit", view_func=views.edit_player_attributes_page, methods=["GET", "POST"])
    app.add_url_rule("/players_attributes_delete/<int:id>/", view_func=views.delete_player_attributes_page)
    
    app.add_url_rule(
        "/login", view_func=views.login_page, methods=["GET", "POST"]
    )
    app.add_url_rule("/logout", view_func=views.logout_page)
    
    lm.init_app(app)
    lm.login_view = "login_page"
    
    db = Database()
    db.add_player(Player("Ronaldo",age=38))
    app.config["db"] = db
    
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
    
