from flask import Blueprint, render_template, request, redirect
from models.document import Document
from models.database import db
from search import search_documents, delete_document

# Потом убрать или нет 
from datetime import datetime

# Все руты тут
views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    results = search_documents("posts", query)
    
    # Хз потом может переделаю Главноее что работает
    documents = []
    for result in results:
        document_id = result['_source']['id']
        document = Document.query.get(document_id)
        documents.append(document)
    
    return render_template('index.html', documents=documents, query=query)

@views.route('/delete', methods=['POST'])
def delete():
    document_id = request.form.get('document_id')
    
    if document_id:
        delete_document("posts", document_id)
        document = Document.query.get(document_id)
        db.session.delete(document)
        db.session.commit()
        
    return redirect('/')