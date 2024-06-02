import sys
from store import Store

def processCommandLine():
    if len(sys.argv) == 1:
        return

    store = Store()

    commandsList = sys.argv
    nAll = len(commandsList)
    listOfSwitches = ["-test", "-add", "-tag", "-show", "-remove", "-doc", "-name",
                      "-desc", "-h", "-assign", "-path", "-doc_id", "-tag_id", "-search"]
    commandsListTmp = []

    for index, item in enumerate(commandsList):
        if item in listOfSwitches:
            commandsListTmp.append({"key": item, "start": index, "end": index})

    commandsList = commandsListTmp

    n = len(commandsList)

    for i in range(n - 1):
        if commandsList[i]["start"] + 1 < commandsList[i + 1]["start"]:
            commandsList[i]["start"] += 1
            commandsList[i]["end"] = commandsList[i + 1]["start"] - 1

            if commandsList[i]["start"] > commandsList[i]["end"]:
                commandsList[i]["start"] = None
                commandsList[i]["end"] = None

    if commandsList[n - 1]["start"] < nAll:
        commandsList[n - 1]["start"] += 1
        commandsList[n - 1]["end"] = nAll - 1

        if commandsList[n - 1]["start"] > commandsList[n - 1]["end"]:
            commandsList[n - 1]["start"] = None
            commandsList[n - 1]["end"] = None

    commandsDict = {}
    for command in commandsList:
        key = command["key"]
        if command["start"] is None:
            args = None
        else:
            args = sys.argv[command["start"]:command["end"] + 1]
        commandsDict[key] = args
        if key == "-desc":
            args = ' '.join(args)



    print(commandsList)
    print(commandsDict)

    if "-test" in commandsDict:
        store.createDB()
        store.loadData()
        store.selectData()
    elif "-show" in commandsDict:
        store.selectData()
    elif "-add" in commandsDict:
        if "-tag" in commandsDict:
            if "-name" in commandsDict:
                name = ' '.join(commandsDict["-name"]) if "-name" in commandsDict and commandsDict["-name"] else None
                if "-desc" in commandsDict:
                    description = ' '.join(commandsDict["-desc"]) if "-desc" in commandsDict and commandsDict["-desc"] else None
                else:
                    description = None
                store.addTag(name, description)
            else:
                print("Zapomniałeś podać nazwę (opcja -name).")
                print("Użyj opcji -h aby wyświetlić pomoc.")
    elif "-h" in commandsDict:
        text = \
        '''
        ----------------------------------------------------------------
        -show
            Show all information about database
        -tag
            Display availiable tags
        -add -tag -name NAME [-desc DESCRIPTION]
            Add tag
        -remove -tag -name NAME 
            Remove tag
        -remove -doc -name NAME
            Remove doc
        -search -tag -name
            Search documents by tag
        -add -doc -name NAME -path PATH [-desc DESCRIPTION]
            Add doc
        -assign -tag -tag_id TAG_ID -doc -doc_id DOC_ID
            Assign tag to document
        -test 
            Execute test
        ----------------------------------------------------------------
        '''
        print(text)
    if "-add" in commandsDict:
        if "-doc" in commandsDict:
            if "-name" in commandsDict:
                name = ' '.join(commandsDict["-name"]) if "-name" in commandsDict and commandsDict["-name"] else None
                if "-path" in commandsDict:
                    path = commandsDict["-path"][0] if "-path" in commandsDict and commandsDict["-path"] else None
                    if "-desc" in commandsDict:
                        description = ' '.join(commandsDict["-desc"]) if "-desc" in commandsDict and commandsDict["-desc"] else None
                    else:
                        description = None
                    store.addDoc(name, path, description)
                else:
                    print("Zapomniałeś podać ścieżkę (opcja -path).")
                    print("Użyj opcji -h aby wyświetlić pomoc.")
            else:
                print("Zapomniałeś podać nazwę (opcja -name).")
                print("Użyj opcji -h aby wyświetlić pomoc.")
            #---------------- opcja remove ---------------


    if "-remove" in commandsDict:
        if "-tag" in commandsDict:
            if "-name" in commandsDict:
                name = ' '.join(commandsDict["-name"]) if "-name" in commandsDict and commandsDict["-name"] else None
                store.removeTag(name)
            else:
                print("Zapomniałeś podać nazwę (opcja -name).")
                print("Użyj opcji -h aby wyświetlić pomoc.")


    if "-remove" in commandsDict:
        if "-doc" in commandsDict:
            if "-name" in commandsDict:
                name = ' '.join(commandsDict["-name"]) if "-name" in commandsDict and commandsDict["-name"] else None
                store.removeDoc(name)
            else:
                print("Zapomniałeś podać nazwę (opcja -name).")
                print("Użyj opcji -h aby wyświetlić pomoc.")

    if "-assign" in commandsDict:
        if "-tag" in commandsDict:
            if "-tag_id" in commandsDict:
                tag_id = commandsDict["-tag_id"][0] if "-tag_id" in commandsDict and commandsDict["-tag_id"] else None
                if "-doc" in commandsDict:
                    if "-doc_id" in commandsDict:
                        doc_id = commandsDict["-doc_id"][0] if "-doc_id" in commandsDict and commandsDict["-doc_id"] else None
                        store.assignTagstoDoc(doc_id, tag_id)

    if "-search" in commandsDict:
        if "-tag" in commandsDict:
            if "-name" in commandsDict:
                tag_name = ' '.join(commandsDict["-name"]) if "-name" in commandsDict and commandsDict["-name"] else None
                result = store.searchDocbyTags(tag_name)
                if result:
                    print("Wyniki wyszukiwania: ")
                    for row in result:
                        print(row)
                else:
                    print("Brak wyników wyszukiwania")
            else:
                print("Zapomniałeś podać nazwę (opcja -name).")
                print("Użyj opcji -h aby wyświetlić pomoc.")


def printWelcome():
    text = \
'''
Welcome to relational based document store system.
Run with -h to get help info.
'''
    store=Store()
    print(text)
    store.availiableTags()



if __name__ == '__main__':
    printWelcome()
    processCommandLine()




