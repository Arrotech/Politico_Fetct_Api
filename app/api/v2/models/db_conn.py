import psycopg2
import os
from psycopg2.extras import RealDictCursor
import json

class Database:
    """Initialization."""

    def __init__(self):
    	self.db_name = os.getenv('DB_NAME')
    	self.db_host = os.getenv('DB_HOST')
    	self.db_user = os.getenv('DB_USER')
    	self.db_password = os.getenv('DB_PASSWORD')
    	self.conn = psycopg2.connect(database=self.db_name,host=self.db_host,user=self.db_user,password=self.db_password)
    	self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        """Create tables."""

        queries = [
        	"""
	        CREATE TABLE IF NOT EXISTS users(
				user_id serial PRIMARY KEY,
				firstname varchar NOT NULL,
                lastname varchar NOT NULL,
				email varchar NOT NULL,
                password varchar NOT NULL,
				phoneNumber varchar NOT NULL,
                passportUrl varchar NOT NULL,
                role varchar NOT NULL,
                date TIMESTAMP
			)""",

            	"""
	        CREATE TABLE IF NOT EXISTS offices(
				office_id serial PRIMARY KEY,
				category varchar NOT NULL,
                name varchar NOT NULL
			)""",


            	"""
	        CREATE TABLE IF NOT EXISTS petitions(
				petition_id serial PRIMARY KEY,
                createdBy varchar NOT NULL,
                office varchar NOT NULL,
                body varchar NOT NULL
			)""",

                """
            CREATE TABLE IF NOT EXISTS parties(
                party_id serial PRIMARY KEY,
                name varchar NOT NULL,
                hqAddress varchar NOT NULL,
                logoUrl varchar NOT NULL
            )""",

            """
            CREATE TABLE IF NOT EXISTS candidates(
                candidate_id serial UNIQUE,
                office integer NOT NULl DEFAULT 0,
                candidate integer NOT NULL DEFAULT 0,
                party integer NOT NULL DEFAULT 0,
                CONSTRAINT office_fk FOREIGN KEY(office) REFERENCES offices(office_id),
                CONSTRAINT candidate_fk FOREIGN KEY(candidate) REFERENCES users(user_id),
                CONSTRAINT party_fk FOREIGN KEY(party) REFERENCES parties(party_id),
                CONSTRAINT candidate_composite_key PRIMARY KEY(office,candidate,party)
                );
            """,

                """
            CREATE TABLE IF NOT EXISTS voters(
                voter_id serial UNIQUE,
                createdBy integer NOT NULL,
                office integer NOT NULL,
                candidate integer NOT NULL,
                CONSTRAINT createdBy_fk FOREIGN KEY(createdBy) REFERENCES users(user_id),
                CONSTRAINT office_fk FOREIGN KEY(office) REFERENCES offices(office_id),
                CONSTRAINT candidate_fk FOREIGN KEY(candidate) REFERENCES candidates(candidate_id),
                CONSTRAINT office_composite_key PRIMARY KEY(createdBy,office,candidate)
            )"""

        ]
        try:
            for query in queries:
            	self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            print(e)

    def create_admin(self):
        """Create a deafult admin user."""

        query = "INSERT INTO users(firstname,lastname,email,password,phoneNumber,passportUrl,role)\
        VALUES('Harun','Gachanja','admin@admin.com','pbkdf2:sha256:50000$7CNfLstB$543e786df1eafa03b81bb9788beb7e50f27f1334c748f2d7cbb23c04f02fd8ff','0722985471','https://www.pivotaltracker.com/n/projects/2284574','admin')"

        self.curr.execute(query)
        self.conn.commit()
        self.curr.close()

    def destroy_table(self):
        """Destroy tables"""

        users = "DROP TABLE IF EXISTS  users CASCADE"
        offices = "DROP TABLE IF EXISTS  offices CASCADE"
        voters = "DROP TABLE IF EXISTS  voters CASCADE"
        petitions = "DROP TABLE IF EXISTS  petitions CASCADE"
        parties = "DROP TABLE IF EXISTS  parties CASCADE"
        candidates = "DROP TABLE IF EXISTS  candidates CASCADE"
        queries = [users, offices, voters, petitions, parties, candidates]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

    def fetch(self, query):
        """Manipulate query."""

        self.curr.execute(query)
        fetch_all = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return fetch_all