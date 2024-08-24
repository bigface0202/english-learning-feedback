import os
import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseAdapter:
    def __init__(self) -> None:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def set_data(self, collection_name: str, document_id: str, data: dict) -> None:
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.set(data)

    def get_data(self, collection_name: str, document_id: str) -> dict:
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    
    def update_data(self, collection_name: str, document_id: str, data: dict) -> None:
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.update(data)
    
    def delete_data(self, collection_name: str, document_id: str) -> None:
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc_ref.delete()
