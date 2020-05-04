from app import db

class Post(db.Model):
    __tablename__ ='profile'
    
    id=db.Column(db.Integer, primary_key=True)
    fName=db.Column(db.String(200))
    lName=db.Column(db.String(200))
    gender=db.Column(db.String(200))
    email=db.Column(db.String(200), unique=True)
    location=db.Column(db.String(200))
    biography=db.Column(db.String(200))

    #date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,fName,lName,gender,email,location,biography):
        self.fName=fName
        self.lName=lName
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
    def __repr__(self):
    
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
        'fName':self.fName,
        'lName':self.lName,
        'gender':self.gender,
        'email':self.email,
        'location':self.location,
        'biography':self.biography
            
        }