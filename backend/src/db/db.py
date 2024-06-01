from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from diplom_kartigo.config import settings

DATABASE_URL = f'sqlite:///{settings.DB_NAME}.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False)

session = Session()

class Base(DeclarativeBase):
    pass