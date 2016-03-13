from app import create_app
from mongoengine.connection import get_connection
from app.dummies import dummies

app = create_app()


def load_dummies():
    client = get_connection()
    db = client[app.config['DATABASE_NAME']]

    for name in db.collection_names():
        if name in ['note', 'notebook']:
            db.drop_collection(name)

    for name in dummies:
        documents = dummies[name]
        for document in documents:
            db[name].save(document)


def before_scenario(context, scenario):
    load_dummies()
