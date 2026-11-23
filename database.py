from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://fernandogonzalesm_db_user:eokh2auZcrFry08H@cluster0.0ghv7fx.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
        return db
    except Exception as e:
        print('Error de conexion con la bdd:', e)
        return None