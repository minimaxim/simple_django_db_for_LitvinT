from sqlalchemy import Column, Integer, VARCHAR, select, Boolean, BigInteger, SmallInteger, DATETIME
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from loader import DATABASE_URL


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    engine = create_async_engine(f'postgresql+asyncpg://{DATABASE_URL}')
    session = async_sessionmaker(bind=engine)

    def __init__(self, **kwargs) -> None:
        for kw in kwargs.items():
            self.__getattribute__(kw[0])
            self.__setattr__(*kw)

    @staticmethod
    def create_async_session(func):
        async def wrapper(*args, **kwargs):
            async with Base.session() as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_async_session
    async def save(self, session: AsyncSession = None, **kwargs) -> list["Base"]:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_async_session
    async def get(cls, pk: int, session: AsyncSession = None) -> "Base":
        return await session.get(cls, pk)

    @classmethod
    @create_async_session
    async def all(cls, order_by: str = 'id', session: AsyncSession = None, **kwargs) -> list["Base"]:
        return [obj[0] for obj in await session.execute(select(cls).filter_by(**kwargs).order_by(order_by))]

    @create_async_session
    async def delete(self, session: AsyncSession = None) -> None:
        await session.delete(self)
        await session.commit()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)
    is_published = Column(Boolean, default=True)

    def __str__(self):
        return self.name


class User(Base):
    __tablename__: str = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=True)
    username = Column(VARCHAR(128), nullable=True)
    start_name = Column(VARCHAR(128), nullable=True)
    category_name = Column(VARCHAR(128), nullable=True)
    model_name = Column(VARCHAR(128), nullable=True)
    kolvo = Column(VARCHAR(128), nullable=True)
    call_me = Column(VARCHAR(128), nullable=True)
    discont = Column(VARCHAR(5), nullable=True)
    power = Column(VARCHAR(128), nullable=True)
    currency = Column(VARCHAR(5), nullable=True)
    coin = Column(VARCHAR(24), nullable=True)
    cost_electricity = Column(VARCHAR(128), nullable=True)
    hash = Column(VARCHAR(128), nullable=True)
    potreb = Column(VARCHAR(128), nullable=True)
    komm = Column(VARCHAR(128), nullable=True)
    promo = Column(VARCHAR(128), nullable=True)
    date = Column(VARCHAR(28), nullable=True)

    def __str__(self):
        return self.id


class Start(Base):
    __tablename__: str = 'start'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Coin(Base):
    __tablename__: str = 'coins'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Currency(Base):
    __tablename__: str = 'currencies'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Power(Base):
    __tablename__: str = 'powers'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Discont(Base):
    __tablename__: str = 'disconts'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Promo(Base):
    __tablename__: str = 'promocodes'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Application(Base):
    __tablename__: str = 'aplications'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    is_published = Column(Boolean, default=True, nullable=True)


class Admin(Base):
    __tablename__: str ='admin'

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
