from tkinter import *
class Speak:
    def __init__ (self):
        self.__stage = 0
        self.__option = 0
        self.__option2 = 0
    def setStage (self, stage):
        self.__stage = stage
    def getStage (self):
        return self.__stage
    def setOption (self, option):
        self.__option = int(option)
    def getOption (self):
        return self.__option
    def likeIt (self, character):
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
    def getResponse (self, character, responses):
        self.likeIt(character)
        self.__option2 = self.__option
        return responses[self.__option][7 + self.__option2]
    def getScene (self, character, responses):
        return responses[character.getHistory()*6][0]
    def getChoices1 (self, character, responses):
        choices = [responses[1 + 6*character.getHistory()][0], responses[2 + 6*character.getHistory()][0], responses[3 + 6*character.getHistory()][0], responses[4 + 6*character.getHistory()][0], responses[5 + 6*character.getHistory()][0]]
        return choices

def talk(character, wordsList):
    juli = Speak()
    topic = juli.getScene(character, wordsList)
    relationshipBefore = character.getRelationship()
    choices = juli.getChoices1(character, wordsList)
    makeChoice(juli, choices)
    response = juli.getResponse(character, wordsList)
    relationshipAfter = character.getRelationship()
    display(topic, relationshipBefore, response, relationshipAfter)

def display(topic, relBef, response, relAft):
    print(topic)
    print(relBef)
    print(response)
    print(relAft)

def choice(choices):
    count = 0
    for option in choices:
        print(choices[count])
        count += 1
    choice = int(input('0-4: '))
    return choice

def makeChoice(conversation, choices):
    conversation.setOption(choice(choices))
