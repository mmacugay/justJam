import pygame
import conversation


class Character:
    def __init__(self, name, jamPotency, personality, relationship):
        self.__name = name
        self.__jamPotency = jamPotency
        self.__personality = personality
        self.__relationship = relationship
        self.__history = 0
        self.__items = ['spoon', 'jar']
        self.__location = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def addJamPotency(self, jam):
        self.__jamPotency += jam

    def getJamPotency(self):
        return self.__jamPotency

    def setPersonality(self, personality):
        self.__personality = personality

    def getPersonality(self):
        return self.__personality

    def setRelationship(self, relationship):
        self.__relationship = relationship

    def addRelationship(self, relationship):
        self.__relationship += relationship

    def getRelationship(self):
        return self.__relationship

    def addHistory(self, history):
        self.__history += history

    def getHistory(self):
        return self.__history

    def addItem(self, item):
        self.__items += item

    def removeItem(self, item):
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

    giorno = Character("Giorno", 10, 1, 0)
    bucciarati = Character("Bucciarati", 10, 0, 0)
    mista = Character("Mista", 10, 2, 0)
    king = Character("Konig Reich", 13, 2, 5)
    aldo = Character("Aldo", 5, 0, 10)
    ambro = Character("Ambro", 5, 2, 5)
    russo = Character("Russo", 7, 0, 5)
    juliet = Character("Julius Caesar", 15, 0, 0)
    idalia = Character("Idalia", 1, 1, 15)
    beatrix = Character("Beatrix", 5, 0, 6)
    caputia = Character("Caputia", 100, 1, 100)
    pope = Character("The Pope", 50, 1, 50)
    words = open(r'juliet.txt', 'r').readlines()
    count = 0
    for line in words:
        count += 1
    wordsList = [[]*12]*count
    count = 0
    for stuff in words:
        wordsList[count] = stuff.split('|')
        count += 1
    for conversations in range(0, 1):
        conversation.talk(juliet, wordsList)


class Speak:
    def __init__(self):
        self.__stage = 0
        self.__option = 0
        self.__option2 = 0

    def setStage(self, stage):
        self.__stage = stage

    def getStage(self):
        return self.__stage

    def setOption(self, option):
        self.__option = int(option)

    def getOption(self):
        return self.__option

    def likeIt(self, character):
        if self.__option == 0:                  # Silent
            if character.getPersonality() == 0:
                character.addRelationship(5)

            elif character.getPersonality() == 1:
                character.addRelationship(-5)

            else:
                character.addRelationship(10)
        elif self.__option == 1:                # Ideal
            if character.getPersonality() == 0:
                character.addRelationship(-5)

            elif character.getPersonality() == 1:
                character.addRelationship(15)

            else:
                character.addRelationship(-5)
        elif self.__option == 2:                # Gruff

            if character.getPersonality() == 0:
                character.addRelationship(-10)

            elif character.getPersonality() == 1:
                character.addRelationship(-15)

            else:
                character.addRelationship(10)
        elif self.__option == 3:                # Pess
            if character.getPersonality() == 0:
                character.addRelationship(10)
            elif character.getPersonality() == 1:
                character.addRelationship(-10)
            else:
                character.addRelationship(-5)
        else:                                   # Fact
            character.addRelationship(1)

    def getResponse(self, character, responses):
        self.likeIt(character)
        if self.__stage == 0:
            self.__option2 = self.__option
            option = self.__option
            farness = 1
        else:
            option = self.__option2
            farness = self.__option + 7
        return responses[option + character.getHistory()*6+1][farness]

    def getScene(self, character, responses):
        if character.getHistory() == 0:
            response = responses[0][0]
        else:
            response = responses[character.getHistory()*6][0]
        return response

    def getChoices(self, character, responses):
        if self.__stage == 0:
            choices = []
            for slots in range(0, 5):
                choices.append(
                    responses[slots + character.getHistory()*6+1][0])
        else:
            choices = []
            for slots in range(0, 5):
                choices.append(
                    responses[self.__option2 + character.getHistory()*6+1][slots + 2])
        return choices


words = open(r'juliet.txt', 'r').readlines()
count = 0
for line in words:
    count += 1
wordsList = [[]*12]*count
count = 0
for stuff in words:
    wordsList[count] = stuff.split('|')
    count += 1


name = input("Enter Name")

print("You are", (name), "You live at Colkirk with Juliet your long life childhood friend. You came here after the Jampocalypse. You notice Juliet running towards you")

juliet = Character("Juliet", 1, 1, 100)
conversation.talk(juliet, wordsList)

print("You get stuff for dinner")
# fight goes here toturial


conversation.talk(juliet, wordsList)
