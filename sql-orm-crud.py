from sqlalchemy import (
    create_engine, Column, Integer, Float, String, MetaData, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm.session import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base(db)


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Sessiion = sessionmaker(db)
session = Sessiion()
#base.metadata.create_all(db)

bijo = Programmer(
    first_name="Nijo",
    last_name="mathew",
    gender="M",
    nationality="Ind",
    famous_for="noth"
)

session.add(bijo)
session.commit()

Programmers = session.query(Programmer)
for pro in Programmers:
    print(
        pro.id,
        pro.first_name,
        pro.last_name,
        pro.gender,
        pro.famous_for,
        sep="-"
    )