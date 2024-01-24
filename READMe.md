URL: https://blacklight-assignment.onrender.com

**For API calls append appropriate api endpoints to the above url**

API endpoints:

**To Display current week leaderboard (Top 200) :**

/current_week_leaderboard

example: https://blacklight-assignment.onrender.com/current_week_leaderboard

**Display last week leaderboard given a country by the user (Top 200) :**

/last_week_leaderboard/`<country>`  

example: https://blacklight-assignment.onrender.com/last_week_leaderboard/ET


**To fetch user rank, given the userId. :**

/user_rank/`<uid>`

example: https://blacklight-assignment.onrender.com/user_rank/IUHL

**note**
I have taken into account that user may have attempted the game multiple times at different timestamps. Consequently, I have chosen to use the highest scores of each user to determine and display the current week leaderboard, past week leaderboard, and user rank.

The Database is hosted online and a table "scoreboard_table" is created and mock data is generated using python script "create_db.py". 