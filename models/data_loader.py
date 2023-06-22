from datetime import datetime
import csv

from models.document import Document
from models.database import db
from search import index_document, search_documents

def load_data_to_database():
    if Document.query.count() > 0:
        print("[Database] Data already loaded")
        return

    with open('posts.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        documents = []

        for row in reader:
            text = row[0]
            created_date = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
            rubrics = row[2].split(',')

            document = Document(
                text=text,
                created_date=created_date,
                rubrics=rubrics
            )

            documents.append(document)

        db.session.add_all(documents)
        db.session.commit()


def load_data_to_elasticsearch():
    documents = Document.query.all()

    if not documents:
        print("[Database] No data to load")
        return

    for document in documents:
        existing_doc = search_documents("posts", f"id:{document.id}")
        if existing_doc:
            print(f"[Elasticsearch] Document with ID {document.id} already exists")
            continue

        print(document.id)    

        index_document("posts", {
            'id': document.id,
            'text': document.text,
        })

    print("[Elasticsearch] Data loaded successfully")