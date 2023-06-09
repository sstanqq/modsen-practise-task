from elasticsearch import Elasticsearch

# from dotenv import load_dotenv
import os

el_host = os.getenv('ELASTIC_HOST')
el_port = os.getenv('ELASTIC_PORT')
el_user = os.getenv('ELASTIC_USER')
el_password = os.getenv('ELASTIC_PASSWORD')

es = Elasticsearch(
    f'https://{el_host}:{el_port}',
    http_auth=(el_user, el_password),
    verify_certs=False
)

def create_index(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
    else:
        print('Index already created')

def delete_index(index_name):
    es.indices.delete(index=index_name)

def index_document(index_name, document):
    es.index(index=index_name, body=document)

def delete_document(index_name, document_id):
    query = {
        "query": {
            "term": {
                "id": document_id
            }
        }
    }

    response = es.search(index=index_name, body=query)

    if response["hits"]["total"]["value"] > 0:
        document_id = response["hits"]["hits"][0]["_id"]
        es.delete(index=index_name, id=document_id)
    else:
        print("Document not found")

def search_documents(index_name, query):
    body = {
        "query": {
            "match": {
                "text": query
            }
        },
        "size": 20
    }
    result = es.search(index=index_name, body=body)
    return result["hits"]["hits"]

# Для теста
def output_all():
    response = es.search(index='posts', body={'query': {'match_all': {}}})

    hits = response['hits']['hits']
    print('RES: ')
    for hit in hits:
        print(hit['_source'])