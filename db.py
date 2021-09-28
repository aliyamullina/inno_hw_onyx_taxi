from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Driver(Base):
    '''Описание БД с данными о водителях.'''

    __tablename__ = 'drivers'

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Идентификатор водителя")
    name = Column(String, nullable=False, comment="Имя водителя")
    car = Column(String, nullable=False, comment="Название машины")


class Client(Base):
    """Описание БД с данными клиентов."""

    __tablename__ = "clients"

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Идентификатор клиента")
    name = Column(String, nullable=False, comment="Имя клиента")
    is_vip = Column(Boolean, nullable=False, comment="Статус клиента")


class Order(Base):
    """Описание БД с данными водителей."""

    __tablename__ = "drivers"

    id = Column(Integer, autoincrement=True, primary_key=True, comment="Идентификатор водителя")
    name = Column(String, nullable=False, comment="Имя водителя")
    car = Column(String, nullable=False, comment="Название машины")

