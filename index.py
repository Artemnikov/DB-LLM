
import os
import random
from faker import Faker

os.environ['OPENAI_API_KEY'] = ".........."
import mysql.connector
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from datetime import datetime, timedelta

DATABASE = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "name": os.getenv("DB_NAME")
}
num_users = 100

def generate_users():
    fake = Faker()
    conn = mysql.connector.connect(**DATABASE)
    cursor = conn.cursor()

    for _ in range(num_users):
        username = fake.user_name()
        password = fake.password()
        created_at = fake.date_time_between(start_date="-1 year", end_date="now")
        last_login = created_at + timedelta(days=random.randint(1, 365))
        purchases = random.randint(0, 10)
        last_purchase = created_at + timedelta(days=random.randint(1, 365))
    
    query = "INSERT INTO users (username, password, created_at, last_login, purchases, last_purchase) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, password, created_at, last_login, purchases, last_purchase)
    cursor.execute(query, values)
    
    conn.commit()
    cursor.close()
    conn.close()


# Connect to the database and execute the SQL script
# TODO - make it create dummy data for SQL
if os.getenv("GENERATE_DATA") == "True":

# Create the agent executor
db = SQLDatabase.from_uri("sqlite:///./Chinook.db")
toolkit = SQLDatabaseToolkit(db=db)
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

