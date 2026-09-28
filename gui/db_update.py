import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

pw = os.getenv("DB_PASSWORD")

DB_CONFIG = dict(
        host = "localhost",
        user = "root",
        password = pw,
        database = "rosdb",
        charset = "utf8"
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)

    def insert_data(self, name, x, y, theta):
        sql = "INSERT INTO turtlepos (id, x, y, theta) values (%s, %s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, x, y, theta))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False
