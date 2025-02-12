from app.main import create_app, db
from flask_migrate import Migrate
import logging
logging.basicConfig(level=logging.DEBUG)

app = create_app()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(
        host=app.config["FLASK_HOST"],
        port=app.config["FLASK_PORT"],
        ssl_context="adhoc",
        debug=app.config["DEBUG"],
    )
