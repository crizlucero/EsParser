import couchdb

class DB:
    conn = None
    db = None

    def __init__(self):
        self.conn =couchdb.Server("http://example.com:5984/")

    def createDB(self):
        self.db = self.conn.create("EsParser")

    def deleteDB(self):
        self.conn.delete("EsParser")

    def saveData(self, document):
        self.db.save(document)

    def getData(self):
        return None