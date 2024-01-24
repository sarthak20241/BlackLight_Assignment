URL: https://blacklight-assignment.onrender.com

# For API calls append appropriate api endpoints to the above url

API endpoints:

To Display current week leaderboard (Top 200) 
/current_week_leaderboard

Display last week leaderboard given a country by the user (Top 200)
/last_week_leaderboard/<country>

To fetch user rank, given the userId.
/user_rank/<uid>

# note
I have taken into account that users may have attempted the game at different timestamps. Consequently, I have chosen to use the highest scores of each user to determine and display the current week leaderboard, past week leaderboard, and user rank.