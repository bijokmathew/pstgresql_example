from sqlalchemy import (
    create_engine, Table, Column, String, Integer, Float, ForeignKey, MetaData
)
db = create_engine("postgresql:///chinook")
metadata = MetaData(db)
art_table = Table("Artist", metadata,
        Column("ArtistId", Integer, primary_key=True),
        Column("Name", primary_key=False)
    )
album_table = Table("Album",metadata,
    Column("AlbumId", Integer,primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("art_table.ArtistId"))
)

with db.connect() as conn:
   # query = art_table.select()
    #query = album_table.select().with_only_columns([album_table.c.Title])
    query = album_table.select().where(album_table.c.ArtistId==51)
    res = conn.execute(query)
    for r in res:
        print(r)