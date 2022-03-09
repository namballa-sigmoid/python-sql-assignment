import logging
from connection import create_connection

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s --> %(funcName)s() --> %(message)s')


class InsertData:
    def __init__(self, user, database, password, host, port):
        connection = create_connection.get_connection(self, database=database, user=user, password=password,
                                                      host=host, port=port)
        cur = connection.cursor()
        try:
            with open("schema.sql", "r") as file:
                queries = file.readlines()
                for query in queries:
                    cur.execute(query)
            logging.info("Schema Created")
        except:
            logging.info("Schema Creation Failed")
        connection.commit()
        connection.close()
        logging.info("Connection Close")


obj = InsertData("namballamukesh", "postgres", "Mukesh@123", "localhost", "5432")

