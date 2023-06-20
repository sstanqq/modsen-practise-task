from flask import Blueprint, render_template, request
from models.document import Document
from models.database import db

# Потом убрать
from datetime import datetime

# Все руты тут
views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')

# Тест
@views.route('/document')
def create_document():
    # text = request.json['text']
    text = 'Test'
    
    document = Document(['Test'], text, datetime.now)
    
    db.session.add(document)
    db.session.commit()
    
    return f'{document.text}'