import dotenv
import pymysql
import os

from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain

dotenv.load_dotenv()

db = SQLDatabase.from_uri("mysql://root:admin@127.0.0.1/poppins")
llm = OpenAI(temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run("How many employees are there?")