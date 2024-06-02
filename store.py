from engine_relational import EngineRelational

class Store:
    _engine = None

    def __init__(self):
        self._engine = EngineRelational()

    def createDB(self):
        print("Create")
        self._engine.createDB()

    def loadData(self):
        print("Load")
        self._engine.populateDBWithData()

    def selectData(self):
        print("Select")
        self._engine.selectDataBasic()

    def addTag(self, name, description):
        self._engine.addTag(name, description)

    def addDoc(self,name,path,description):
        self._engine.addDoc(name,path,description)

    def removeTag(self, name):
        self._engine.removeTag(name)

    def removeDoc(self, name):
        self._engine.removeDoc(name)

    def assignTagstoDoc(self, doc_id, tag_id):
        self._engine.assignTagstoDoc(doc_id,tag_id)

    def availiableTags(self):
        self._engine.availiableTags()

    def searchDocbyTags(self,tag_name):
        self._engine.searchDocbyTags(tag_name)