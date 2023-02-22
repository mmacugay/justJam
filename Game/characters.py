class Character:
    def __init__ (self, name, jamPotency, personality, relationship, words):
        self.__name = name
        self.__jamPotency = jamPotency
        self.__personality = personality
        self.__relationship = relationship
        self.__history = 0
        self.__items = ['spoon', 'jar']
        self.__location = 0
        self.__words = words
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
    def wordTake(self):
        words = self.__words
        count = 0
        for line in words:
            count += 1
        wordsList = [[]*12]*count
        count = 0
        for stuff in words:
            wordsList[count] = stuff.split('|')
            count += 1
        return wordsList