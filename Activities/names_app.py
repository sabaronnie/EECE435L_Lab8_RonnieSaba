"""Activity 2's names-only API on port 3000."""

from flask import Flask, jsonify

from database import create_db_table, get_users as load_users

app = Flask(__name__)


@app.get("/get_users")
def get_users():
    return jsonify([user["name"] for user in load_users()])


if __name__ == "__main__":
    create_db_table()
    app.run(host="0.0.0.0", port=3000, debug=False)
