from models.database import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.ARRAY(db.String))
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'Document: {self.text}'
    
    def __init__(self, _rubrics, _text, _created_date):
        self.rubrics = _rubrics
        self.text = _text
        self.created_date = _created_date
    