from app import electoral_app
from app.api.v2.models.db_conn import Database
import os

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
app = electoral_app(config_name)


@app.cli.command()
def create():
    Database().create_table()

@app.cli.command()
def admin():
    Database().create_admin()

@app.cli.command()
def destroy():
    Database().destroy_table()


if __name__ == "__main__":
    app.run(debug=True)
