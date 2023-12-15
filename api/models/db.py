import os

from sqlmodel import Field, Session, SQLModel, create_engine

db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')


engine = create_engine(f'postgresql://{db_user}:{db_password}@postgres:5432/{db_name}')


SQLModel.metadata.create_all(engine)