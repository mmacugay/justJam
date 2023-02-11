import conversation
class Character:
    def __init__ (self, name, jamPotency, personality, relationship):
        self.__name = name
        self.__jamPotency = jamPotency
        self.__personality = personality
        self.__relationship = relationship
        self.__history = 0
        self.__items = ['spoon', 'jar']
        self.__location = 0
    def setName (self, name):
        self.__name = name
    def getName (self):
        return self.__name
    def addJamPotency (self, jam):
        self.__jamPotency += jam
    def getJamPotency (self):
        return self.__jamPotency
    def setPersonality (self, personality):
        self.__personality = personality
    def getPersonality (self):
        return self.__personality
    def setRelationship (self, relationship):
        self.__relationship = relationship
    def addRelationship (self, relationship):
        self.__relationship += relationship
    def getRelationship (self):
        return self.__relationship
    def addHistory (self, history):
        self.__history += history
    def getHistory (self):
        return self.__history
    def addItem (self, item):
        self.__items += item
    def removeItem (self, item):
        for things in self.__items:
            if things == item:
                self.__items[things] = ''
    def isHere(self):
        self.location = 1
    def isNotHere(self):
        self.location = 0
            
def story():
    victorino = Character("Victorino", 2, 0, 10)
    alphonso = Character("Alphonso", 2, 2, 10)
    juliet = Character("Juliet", 1, 1, 100)
    giorno = Character("Giorno", 10, 1, 0)
    bucciarati = Character("Bucciarati", 10, 0, 0)
    mista = Character("Mista", 10, 2, 0)
    king = Character("Konig Reich", 13, 2, 5)
    aldo = Character("Aldo", 5, 0, 10)
    ambro = Character("Ambro", 5, 2, 5)
    russo = Character("Russo", 7, 0, 5)
    julius = Character("Julius Caesar", 15, 0, 0)
    idalia = Character("Idalia", 1, 1, 15)
    beatrix = Character("Beatrix", 5, 0, 6)
    caputia = Character("Caputia", 100, 1, 100)
    pope = Character("The Pope", 50, 1, 50)
    words = ["nothing","happy","grr","wahh","hmph"]
    conversation.talk(ambro, words)

story()
