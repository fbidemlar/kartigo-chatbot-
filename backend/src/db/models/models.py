from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, BLOB
from sqlalchemy.orm import relationship
from diplom_kartigo.backend.src.db.db import Base, session
from diplom_kartigo.config import settings

from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(Integer, nullable=False, unique=True)
    tg_username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)

    order = relationship('Orders', backref='users')

    @staticmethod
    def get_current(tg_id):
        user = session.query(Users).filter_by(tg_id=tg_id).first()
        return user if user else None

    @classmethod
    def create(cls,
               tg_id: int,
               tg_username: str,
               first_name: str,
               phone_number: str):
        try:
            user = Users.get_current(tg_id)
            if user:
                return user
            else:
                new_user = cls(tg_id=tg_id,
                               tg_username=tg_username,
                               first_name=first_name,
                               phone_number=phone_number)
                session.add(new_user)
                session.commit()
        except Exception as e:
            print("create:", e)
            session.rollback()
        finally:
            session.close()


class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    product = relationship('Products', backref='genre')

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_name = Column(BLOB, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    genre_id = Column(ForeignKey('genres.id'), nullable=False)

    order = relationship('Orders', backref='products')

    @classmethod
    def insert_product(cls,
                       data_name: str,
                       genre: Genres,
                       description: str,
                       price: float):
        try:
            file_path = settings.GENRE_PATH + genre.name + '/' + data_name
            print(file_path)
            with open(file_path, 'rb') as wav:
                wav_data = wav.read()

            new_product = cls(data_name=wav_data,
                              description=description,
                              price=price)
            session.add(new_product)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        finally:
            session.close()

    @staticmethod
    def get_wav(genre_name: str):
        genre = session.query(Genres).filter_by(name=genre_name).first()

        files = session.query(Products).filter(Products.genre_id==genre.id).all()
        return files if files else None

    @staticmethod
    def get_descriptions(genre_name: str):
        from sqlalchemy import select, join

        stmt = (
            select(Products.description)
            .select_from(join(Products, Genres, Products.genre_id == Genres.id))
            .where(Genres.name == genre_name)
        )
        results = session.execute(stmt).all()
        descriptions = [result[0] for result in results]
        return descriptions


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    date = Column(DateTime, nullable=False, unique=True)
    summ = Column(Float, nullable=False, unique=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)

    @staticmethod
    def get_all_by_user(user_id):
        orders = session.query(Orders).filter_by(user_id=user_id).all()
        return orders if orders else None

    @classmethod
    def create(cls,
               product: Products,
               summ: str,
               user: Users):
        try:
            today = datetime.utcnow()
            if product:
                new_order = cls(product_id = product.id,
                                date = today,
                                summ = summ,
                                user_id = user.id)
                session.add(new_order)
                session.commit()
        except Exception as e:
            print("create:", e)
            session.rollback()
        finally:
            session.close()
