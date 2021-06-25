from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class first_gen(db.Model):
    __tablename__ = 'first_gen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    second_gen = db.relationship('second_gen',backref='first_gen', lazy=True)
    third_gen = db.relationship('third_gen', backref='first_gen', lazy=True)
    children_id = db.Column(db.Integer, db.ForeignKey('second_gen.id'), nullable=False)
    grandchildren_id = db.Column(db.Integer, db.ForeignKey('third_gen.id'), nullable=False)

    def __repr__(self):
        return '<first_gen %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "second_gen": list(map(lambda x: x.serialize(), self.second_gen)),
            "third_gen": list(map(lambda x: x.serialize(), self.third_gen)),
        }

class second_gen(db.Model):
    __tablename__ = 'second_gen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('first_gen.id'), nullable=False)
    children_id = db.Column(db.Integer, db.ForeignKey('third_gen.id'), nullable=False)
    third_gen = db.relationship('third_gen', backref='second_gen', lazy=True)
    first_gen = db.relationship('first_gen', backref='second_gen', lazy=True)

    def __repr__(self):
        return '<second_gen %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "third_gen": list(map(lambda x: x.serialize(), self.third_gen)),
            "first_gen": list(map(lambda x: x.serialize(), self.first_gen)),


        }

class third_gen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('second_gen.id'), nullable=False)
    grandparent_id = db.Column(db.Integer, db.ForeignKey('first_gen.id'), nullable=False)
    first_gen = db.relationship('third_gen', backref='first_gen', lazy=True)
    second_gen = db.relationship('first_gen', backref='second_gen', lazy=True)

    def __repr__(self):
        return '<third_gen %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "second_gen": list(map(lambda x: x.serialize(), self.second_gen)),
            "first_gen": list(map(lambda x: x.serialize(), self.first_gen)),

            # do not serialize the password, its a security breach
        }