from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Avengers(db.Model):
    __tablename__ = "avengers"
    id = db.Column("id", db.Integer, primary_key=True)
    url = db.Column("url", db.String)
    name = db.Column("name", db.String)
    appearances = db.Column("appearances", db.Integer)
    gender = db.Column("gender", db.String)
    year = db.Column("year", db.Integer)
    years_since_joining = db.Column("years_since_joining", db.Integer)
    note = db.Column("notes", db.String)


class TestModel(db.Model):
    __tablename__ = "test"
    id = db.Column("id", db.Integer, primary_key=True)
    url = db.Column("url", db.String)
    name = db.Column("name", db.String)
    appearances = db.Column("appearances", db.Integer)
    gender = db.Column("gender", db.String)
    year = db.Column("year", db.Integer)
    years_since_joining = db.Column("years_since_joining", db.Integer)
    note = db.Column("notes", db.String)
