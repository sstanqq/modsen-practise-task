from models.database import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.ARRAY(db.String))
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'Document: {self.text}'
    
    