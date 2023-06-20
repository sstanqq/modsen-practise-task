from flask import Flask, request
from views import views

from models.database import init_db
from models.document import Document

app = Flask(__name__)

init_db(app)

app.register_blueprint(views, url_prefix='/')


if __name__ == '__main__':
    app.run()