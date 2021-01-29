from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def engine_connector():
    ## Function that serves as a connector to the database
    load_dotenv()
    passwd = os.getenv('MySQLPass')

    mysql_url = f'mysql+mysqldb://root:{passwd}@localhost'
    engine = create_engine(mysql_url)
    
    return engine.connect()   