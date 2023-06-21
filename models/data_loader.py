import csv
from models.database import db
from models.document import Document

from datetime import datetime

FILE_NAME = 'posts.csv'

def load_data_to_database():
    if Document.query.count() > 0:
        print("[Database] Data already loaded")
        return
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            text = row[0]
            created_date = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
            rubrics = row[2].split(',')

            document = Document(
                text=text,
                created_date=created_date,
                rubrics=rubrics
            )

            db.session.add(document)

        db.session.commit()