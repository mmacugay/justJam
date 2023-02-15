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
        if self.__stage == 0:
            self.__option2 = self.__option
            option = self.__option
            farness = 1
        else:
            option = self.__option2
            farness = self.__option + 7
        return responses[option + character.getHistory()*6+1][farness]
    def getScene (self, character, responses):
        if character.getHistory() == 0:
            response = responses[0][0]
        else:
            response = responses[character.getHistory()*6][0]
        return response
    def getChoices (self, character, responses):
        if self.__stage == 0:
            choices = []
            for slots in range(0,5):
                choices.append(responses[slots + character.getHistory()*6+1][0])
        else:
            choices = []
            for slots in range(0,5):
                choices.append(responses[self.__option2 + character.getHistory()*6+1][slots + 2])
        return choices

def talk(character, wordsList):
    #Conversation
    juli = Speak()
    topic = juli.getScene(character, wordsList)
    print(topic)
    relationshipBefore = character.getRelationship()
    choices = juli.getChoices(character, wordsList)
    makeChoice(juli, choices)
    response = juli.getResponse(character, wordsList)
    juli.setStage(juli.getStage()+1)
    relationshipAfter = character.getRelationship()
    display(relationshipBefore, response, relationshipAfter)

    relationshipBefore = character.getRelationship()
    choices = juli.getChoices(character, wordsList)
    makeChoice(juli, choices)
    response = juli.getResponse(character, wordsList)
    juli.setStage(0)
    relationshipAfter = character.getRelationship()
    display(relationshipBefore, response, relationshipAfter)
    character.addHistory(1)

    #Stop! This is conversation 2!

    #topic = juli.getScene(character, wordsList)
    #print(topic)
    #relationshipBefore = character.getRelationship()
    #choices = juli.getChoices(character, wordsList)
    #makeChoice(juli, choices)
    #response = juli.getResponse(character, wordsList)
    #juli.setStage(juli.getStage()+1)
    #display(relationshipBefore, response, relationshipAfter)

def display(relBef, response, relAft):
    print(relBef)
    print(response)
    print(relAft)

def choice(choices):
    count = 0
    for option in choices:
        print(choices[count])
        count += 1
    choice = int(input('1-5: '))
    choice -= 1
    return choice

def makeChoice(conversation, choices):
    conversation.setOption(choice(choices))
