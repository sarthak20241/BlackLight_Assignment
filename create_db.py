import pandas as pd
import random
import string
import numpy as np
from faker import Faker
from sqlalchemy import create_engine

# Create a Faker instance
faker = Faker()

df = pd.DataFrame()

# Add a column "Name" with 3000 random names
df['Name'] = [faker.name() for _ in range(3000)]

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

# Add a new column "Country" with random ISO 2-letter country codes
df['Country'] = [faker.country_code() for _ in range(len(df))]

df = pd.concat([df] * 4, ignore_index=True)

df['Score'] = np.random.randint(0, 101, size=len(df))

# Add a new column "TimeStamp" with random timestamps in UTC format
start_date = pd.Timestamp("2024-01-11", tz='UTC')
end_date = pd.Timestamp("2024-01-23", tz='UTC')
df['TimeStamp'] = [faker.date_time_between(start_date, end_date) for _ in range(len(df))]

# Reorder the columns
df = df[['UID', 'Name', 'Score', 'Country', 'TimeStamp']]

# MySQL database connection settings
mysql_user = 'sql6679428'
mysql_password = 'mCIfQpDS8u'
mysql_host = 'sql6.freesqldatabase.com'
mysql_database = 'sql6679428'

# Create a SQLAlchemy engine and connect to MySQL
engine = create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}")

# Store the DataFrame in MySQL
df.to_sql("scoreboard_table", con=engine, if_exists="replace", index=False)

print(df)
print(list(df.columns))
