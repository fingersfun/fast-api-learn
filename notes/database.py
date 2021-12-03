import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
import pymysql
from sqlalchemy.sql import func

from databases import Database

#DATABASE_URL: str = os.getenv("PGSQL_DB_CON")
DATABASE_URL: str = os.getenv("SQLITE_DB_CONN")
#DATABASE_URL: str = os.getenv("MYSQL_DB_CONN")

#DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
#DATABASE_URL: str = 'sqlite:///./notes/notes.db'
#DATABASE_URL: str = 'mysql://root:root@localhost:3306/notesdb'
print(DATABASE_URL)
# SQLAlchemy
#engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
