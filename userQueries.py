from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

USER_SCORE_DATABASE="scoreboard.db"

# Function to establish a database connection
def get_user_score_db_connection():
    conn = sqlite3.connect(USER_SCORE_DATABASE)
    return conn

@app.route('/')
def flask_app():
    return "Hello"

# API endpoint to display the current week leaderboard (Top 200)
@app.route('/api/current_week_leaderboard', methods=['GET'])
def current_week_leaderboard():
    # Assuming TimeStamp is in MySQL timestamp format
    end_date = datetime.utcnow()
    # Assuming the week starts from monday
    start_date = end_date.date() - timedelta(days=end_date.weekday())
    
    query = f"SELECT * FROM scoreboard_table WHERE TimeStamp BETWEEN '{start_date}' AND '{end_date}' " \
            f"ORDER BY Score DESC " \
            f"LIMIT 200"
    conn = get_user_score_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    leaderboard = cursor.fetchall()
    
    return jsonify(leaderboard)


# API endpoint to display last week leaderboard given a country by the user (Top 200)
@app.route('/api/last_week_leaderboard/<country>', methods=['GET'])
def last_week_leaderboard(country):
    # Assuming the new week starts from Monday
    end_date = datetime.utcnow().date() - timedelta(days=datetime.utcnow().weekday())
    start_date = end_date - timedelta(days=7)

    
    query = f"SELECT * FROM scoreboard_table WHERE TimeStamp BETWEEN '{start_date}' AND '{end_date}' AND " \
            f"Country = '{country}' " \
            "ORDER BY Score DESC " \
            "LIMIT 200"
    conn=get_user_score_db_connection()
    cursor=conn.cursor()
    cursor.execute(query)
    leaderboard = cursor.fetchall()
    
    return jsonify(leaderboard)


# API endpoint to fetch user rank given the userId
@app.route('/api/user_rank/<uid>', methods=['GET'])
def user_rank(uid):
    query = f"SELECT COUNT(*)+1 as rank FROM scoreboard_table WHERE Score > (SELECT Score FROM scoreboard_table WHERE UID = '{uid}')"
    conn=get_user_score_db_connection()
    cursor=conn.cursor()
    cursor.execute(query)
    user_rank = cursor.fetchone()
    
    return jsonify(user_rank)


if __name__ == '__main__':
    app.run(debug=True)
