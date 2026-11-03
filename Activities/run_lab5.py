"""Launch the existing Lab 5 app with Docker's required host and port."""

from app import app
from database import create_db_table


if __name__ == "__main__":
    create_db_table()
    app.run(host="0.0.0.0", port=5000, debug=False)
