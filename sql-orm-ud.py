from sqlalchemy import (
    create_engine, Column, Integer, Float, String, MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base(db)


class Football(base):
    __tablename__ = "Football"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

messi = Football(
    first_name="hijo",
    last_name="thomas",
    gender="M",
    nationality="Ind"
)

session.add(messi)
#session.commit()

programmers = session.query(Football)
for pr in programmers:
    print(pr.id, pr.first_name, pr.last_name, pr.gender, pr.nationality, sep="/")
    if pr.id == 8:
        pr.first_name = "ronado"
    elif pr.id == 9:
        pr.first_name = "kissan"
    session.commit()
fname = input("Enter fisrt name")
lname = input("Enter lst name")
stris = session.query(Football).filter_by(first_name=fname, last_name=lname).first()
if stris is not None:
    print("palyer found")
    an = input("Do u want to D (y/n)")
    if an.lower() == "y":
        session.delete(stris)
        session.commit()
        print("Delted")
    else:
        print("not Deleted")
else:
    print("player not found")

