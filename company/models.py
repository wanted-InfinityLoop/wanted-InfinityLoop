from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    column        = ['id', 'name']
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String(32), nullable=False, unique=True)
    
    # def __init__(self, name=None):
    #     self.name=name

company_countries = db.Table('company_countries', 
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
    db.Column('country_id', db.Integer, db.ForeignKey('countries.id')),
    db.Column('translated_name', db.String(32), nullable=False)
)

class Country(db.Model):
    __tablename__ = 'countries'
    column        = ['id', 'name']
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String(32), nullable=False, unique=True)
    company       = db.relationship('Company', secondary='companies', lazy='subquery',
        backref=db.backref('countries', lazy=True))

country_tags = db.Table('country_tags',
    db.Column('country_id', db.Integer, db.ForeignKey('countries.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('translated_tag', db.String(32), nullable=False)
)

class Tag(db.Model):
    __tablename__ = 'tags'
    column        = ['id', 'name']
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String(32), nullable=False, unique=True)

company_tags = db.Table('company_tags',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)