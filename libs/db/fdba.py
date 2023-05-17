import firebase_admin
from firebase_admin import credentials,db

def getRoot():
        cred = credentials.Certificate("F:/SW/data/pythondb-d8569-firebase-adminsdk-ved43-eb7053ff67.json")
        name= firebase_admin.initialize_app(cred,{
            'databaseURL':'https://pythondb-d8569-default-rtdb.firebaseio.com/'
            })
        return db.reference('/')