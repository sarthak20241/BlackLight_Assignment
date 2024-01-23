import pandas as pd
import random
import string
import numpy as np
import sqlite3
from faker import Faker

# Create a Faker instance
faker = Faker()

df = pd.DataFrame()
# Add a column "Name" with 10,000 random names
df['Name'] = [faker.name() for _ in range(10000)]

# Add a new column "UID" with random unique values (letters)
def generate_uid(df_size):
    used_uids = set()
    for i in range(df_size):
        new_uid = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
        while new_uid in used_uids:
            new_uid = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))

        used_uids.add(new_uid)
    return used_uids

df['UID'] = list(generate_uid(len(df)))


df['Score'] = np.random.randint(0, 101, size=len(df))

# Add a new column "Country" with random ISO 2-letter country codes
df['Country'] = [faker.country_code() for _ in range(len(df))]

# Add a new column "TimeStamp" with random timestamps in UTC format
start_date = pd.Timestamp("2024-01-11", tz='UTC')
end_date = pd.Timestamp("2024-01-23", tz='UTC')
df['TimeStamp'] = [faker.date_time_between(start_date, end_date) for _ in range(len(df))]

# Reorder the columns
df = df[['UID', 'Name', 'Score', 'Country', 'TimeStamp']]

# Store the DB File
db_file = "scoreboard.db"
conn = sqlite3.connect(db_file)
df.to_sql("scoreboard_table", con=conn, if_exists="replace", index=False)

print(df)
print(list(df.columns))