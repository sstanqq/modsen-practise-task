from flask import Flask, request
from views import views

from models.database import init_db
from models.document import Document
from models.data_loader import load_data_to_database

app = Flask(__name__)

init_db(app)

app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    with app.app_context():
        # Ебашим данные из post.csv в бд
        load_data_to_database()
    app.run()