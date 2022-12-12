from sqlalchemy import (
    create_engine, Column, String, Float, Integer, ForeignKey, MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base(db)


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    ArtistId = Column(Integer, ForeignKey(Artist.ArtistId))
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)


artist = session.query(Artist)
for art in artist:
    print(art.ArtistId, art.Name, sep=("!"))

artname = session.query(Artist).filter_by(Name="Queen").first()
print(artname.ArtistId, artname.Name, sep="--")
