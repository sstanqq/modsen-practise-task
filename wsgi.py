from flask import Flask, request
from views import views

from models.database import init_db
from models.document import Document
from models.data_loader import load_data_to_database, load_data_to_elasticsearch
from search import create_index, delete_index

app = Flask(__name__)

init_db(app)

app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    with app.app_context():
        create_index('posts')
        load_data_to_database()
        load_data_to_elasticsearch()
    
    app.run()