import sqlite3
class EngineRelational:
    _dbFileName = 'document.db'

    def createDB(self):
        connection = sqlite3.connect(self._dbFileName)

        if connection is None:
            return False

        with open("db.sql") as f:
            connection.executescript(f.read())

        connection.commit()
        connection.close()

        return True

    def populateDBWithData(self):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()

        cur.execute(
            "INSERT INTO tag (name, description) VALUES (?, ?)",
            ("tag_1",
             "Description of tag 1")
        )

        tag_1_id = cur.lastrowid

        cur.execute(
            "INSERT INTO tag (name) VALUES (?)",
            ("tag_2",)
        )

        tag_2_id = cur.lastrowid

        cur.execute(
            "INSERT INTO document (name, description) VALUES (?, ?)",
            ("Document 1",
             "Description of document 1")
        )

        doc_id = cur.lastrowid

        cur.execute("INSERT INTO document_tag (document_id, tag_id) VALUES (?, ?)",
                    (doc_id, tag_1_id))

        cur.execute(
            "INSERT INTO document (name, description) VALUES (?, ?)",
            ("Document 2",
             "Description of document 2")
        )

        doc_id = cur.lastrowid
        cur.execute("INSERT INTO document_tag (document_id, tag_id) VALUES (?, ?)",
                    (doc_id, tag_2_id))

        cur.execute(
            "INSERT INTO document (name, description) VALUES (?, ?)",
            ("Document 3",
             "Description of document 3")
        )

        doc_id = cur.lastrowid
        data = [
            (doc_id, tag_1_id),
            (doc_id, tag_2_id)
        ]
        cur.executemany("INSERT INTO document_tag (document_id, tag_id) VALUES (?, ?)",
                        data)

        connection.commit()
        connection.close()

    def selectDataBasic(self):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()

        for row in cur.execute("SELECT * FROM tag ORDER BY id;"):
            print(row)

        for row in cur.execute("SELECT * FROM document ORDER BY id;"):
            print(row)

        for row in cur.execute("SELECT * FROM document_tag ORDER BY id;"):
            print(row)

        connection.close()

    def addTag(self, name, description):
        connection =sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        print(f"Dodaję tag '{name}' z opisem '{description}'")
        cur.execute("INSERT INTO tag (name, description) VALUES (?, ?)",(name,description))
        tag_id = cur.lastrowid
        connection.commit()
        connection.close()
        return tag_id

#1 dodaj dokument
    def addDoc(self,name,path,description):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        print(f"Dodaje dokument '{name}'w sciezce '{path}' z opisem '{description}'")
        cur.execute("INSERT INTO document (name, path, description) VALUES (?, ?, ?)", (name, path, description))
        doc_id = cur.lastrowid
        connection.commit()
        connection.close()
        return doc_id

    def removeTag(self,name):
        connection =sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        print(f"Usuwam tag '{name}'")
        cur.execute("DELETE FROM tag WHERE (name)=(?)",(name,))
        connection.commit()
        connection.close()

    def removeDoc(self,name):
        connection =sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        print(f"Usuwam dokument '{name}'")
        cur.execute("DELETE FROM document WHERE (name)=(?)",(name,))
        connection.commit()
        connection.close()

    def assignTagstoDoc(self,doc_id, tag_ids):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        for tag_id in tag_ids:
            cur.execute("SELECT * FROM tag WHERE id = ?", (tag_id,))
            existing_tag = cur.fetchone()
            if existing_tag:
                cur.execute("INSERT INTO document_tag (document_id,tag_id) VALUES (?,?)",(doc_id,tag_id))
            else:
                print(f"Tag o id {tag_id} nie istnieje.")
        connection.commit()
        connection.close()

    def searchDocbyTags(self, tag_name):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        print(f"Searching documents for tag: {tag_name}")
        cur.execute("SELECT document.name, document.description FROM document_tag JOIN document ON document_tag.document_id = document.id JOIN tag ON document_tag.tag_id = tag.id WHERE tag.name = ?",(tag_name,))
        result = cur.fetchall()
        connection.commit()
        connection.close()
        return result

    def availiableTags(self):
        connection = sqlite3.connect(self._dbFileName)
        cur = connection.cursor()
        text = \
'''
------------------------------------------
Wyświetlam dostępne tagi:
        
'''
        print(text)
        for row in cur.execute("SELECT * FROM tag ORDER BY id"):
            print(row)
        print("------------------------------------------")
        print(""
              ""
              "")
        connection.commit()
        connection.close()













