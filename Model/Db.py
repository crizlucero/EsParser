from couchbase.bucket import Bucket
from uuid import uuid4

class DB:
    conn = None
    db = None

    def __init__(self):
        self.conn = Bucket("couchbase://localhost:8091/default")

    def createDB(self):
        self.db = self.conn.upsert("EsParser")

    def deleteDB(self):
        self.conn.delete("EsParser")

    def saveData(self, document):
        self.conn.upsert('Frase' + str(uuid4()).replace("-",""), document)

    def getData(self):
        return None