from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    
    favoritePeople= db.relationship("FavoritePeople", backref="user")

    def __repr__(self):
        return "<User %r>" % self.email
    
    def serialize(self):
        return {
            "id":self.id,
            "email":self.email,
            "name":self.name
        }
   
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250))

    favoritePeople = db.relationship("FavoritePeople", backref="people")

    def __repr__(self):
        return "<People %r>" % self.name

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "homeworld":self.homeworld,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    
    homeworld_of = db.relationship("people", backref="homeworld")
    favoritePlanet = db.relationship("FavoritePlanet", backref="planets")

    def __repr__(self):
        return "<Planets %r>" % self.name
    
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "terrain":self.terrain,
        }
            

class FavoritePeople(db.Model):   
   __tablename__ = 'favoritePeople'
   id = db.Column(db.Integer, primary_key=True)
   user_id_favorites = db.Column(db.Integer, ForeignKey("users.id"))
   favorite_people_id = db.Column(db.Integer, ForeignKey("people.id"))
   
   def serialize(self):
        return {
            "id":self.id,
            "user_id_favorites":self.user_id_favorites,
            "favorite_people_id":self.favorite_people_id,
        }

class FavoritePlanets(db.Model):   
   __tablename__ = 'favoritePlanets'
   id = db.Column(db.Integer, primary_key=True)
   user_id_favorites = db.Column(db.Integer, ForeignKey("users.id"))
   favorite_planets_id = db.Column(db.Integer, ForeignKey("planets.id"))
  
   def serialize(self):
        return {
            "id":self.id,
            "user_id_favorites":self.user_id_favorites,
            "favorite_planets_id":self.favorite_planets_id,
        }
   
