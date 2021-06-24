from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class first_gen(db.Model):
    __tablename__ = 'first_gen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    second_gen = db.relationship('second_gen',backref='first_gen', lazy=True)
    third_gen = db.relationship('third_gen', backref='firt_gen', lazy=True)

    def __repr__(self):
        return '<first_gen %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name" self.last_name,
            "age": self.age
        }

class second_gen(db.Model):
    __tablename__ = 'second_gen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('first_gen.id'), nullable=False)
    third_gen = db.relationship('third_gen', backref='second_gen', lazy=True)

    def __repr__(self):
        return '<Parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.lastname,
            "age": self.age


        }

class Grand_parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    children = db.relationship('Parent', backref='grand_parent', lazy=True)


    

    def __repr__(self):
        return '<Grand_parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age

            # do not serialize the password, its a security breach
        }