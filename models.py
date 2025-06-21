import sqlalchemy
from database import DATABASE_URL

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("done", sqlalchemy.Boolean, default=False)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
