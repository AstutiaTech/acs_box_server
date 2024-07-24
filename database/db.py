from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, mapper
from settings.config import load_env_config
from datetime import datetime, date, timedelta
import urllib.parse

config = load_env_config()

# SQLALCHEMY_DATABASE_URL  = "mysql://" + str(config['database_user']) + ":" + str(config['database_pass']) + "@" + str(config['server']) + "/" + str(config['database']) + "?charset=utf8mb4"

# quoted = urllib.parse.quote_plus(config['database_string'])

# SQLALCHEMY_DATABASE_URL  = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)
# SQLALCHEMY_DATABASE_URL  = 'postgresql://acs_db:5LV1MmnmAwNR4GmSrCj1ZTh6xtcIGGpt@dpg-cnult8qcn0vc73b7hu6g-a/acs_db'
# SQLALCHEMY_DATABASE_URL  = 'postgresql://acs_db_ohtf_user:oQfK7UUBp3gdXGxrbujjVWYNWyg8Rhem@dpg-cpqme3qj1k6c73bj79p0-a/acs_db_ohtf'
SQLALCHEMY_DATABASE_URL  = 'postgresql://astutia_acs:b74sRqqrdgjGvoGEnapNfP92NryLbt7h@dpg-cqgesphu0jms73flifsg-a/astutia_acs'
# SQLALCHEMY_DATABASE_URL  = "mysql://root:@127.0.0.1/puprplepayapp?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=60)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

session = SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

def get_session():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()

def get_laravel_datetime():
    now = datetime.now()
    return now.strftime("%Y/%m/%d %H:%M:%S")

def get_added_laravel_datetime(days=1):
    begin = date.today()
    end = begin + timedelta(days=days)
    return end.strftime("%Y/%m/%d %H:%M:%S")

def compare_laravel_datetime_with_today(datetime_str=None):
    if datetime_str is None:
        return False
    else:
        com_datetime_str = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        dnow = datetime.now()
        if com_datetime_str.time() > dnow.time():
            return True
        else:
            return False