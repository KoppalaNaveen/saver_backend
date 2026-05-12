import os
import json
import firebase_admin

from firebase_admin import credentials, firestore

firebase_credentials = json.loads(
    os.environ["FIREBASE_CREDENTIALS"]
)

cred = credentials.Certificate(firebase_credentials)

firebase_admin.initialize_app(cred)

db = firestore.client()