from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

from dotenv import load_dotenv
import os

load_dotenv()

# Получаем значения переменных окружения
db_user = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

db = SQLAlchemy()

def init_db(app):  
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('document'):
            db.create_all()
            
    # В flask shell прописываем db.create_all()
    
