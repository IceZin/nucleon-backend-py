from sqlalchemy import create_engine

from env import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE

engine = create_engine(
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}",
    echo=False
)

from .models import *
from .queries import *