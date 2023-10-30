import datasets
from langchain.sql import SQLClient
from langchain.sql import SQLChainAgent
from langchain.sql import SQLChainChatbot

sqlchain_chatbot.greet()
sqlchain_dataset = datasets.load_dataset("sqlchain")

sql_client = SQLClient(
    database="my_database",
    host="my_host",
    port=my_port,
    username="my_username",
    password="my_password",
)

sqlchain_agent = SQLChainAgent(sql_client, sqlchain_dataset)

sqlchain_chatbot = SQLChainChatbot(sqlchain_agent)

sql_query = sqlchain_agent.generate_sql("How many users do i have in my firm?")
results = sql_client.execute(sql_query)

sqlchain_chatbot.greet()
sqlchain_chatbot.process_user_input("What is the most active months in the year for the users?")
sqlchain_chatbot.respond()
sqlchain_chatbot.goodbye()