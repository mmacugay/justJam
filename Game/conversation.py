class Speak:
    def __init__ (self):
        self.__stage = 0
        self.__option = 0
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
        return responses[self.__stage * 5 + self.__option]

def talk(character, wordsList):
    WRYY = Speak()
    print(character.getName())
    print(character.getRelationship())
    WRYY.setOption(input('0-4: '))
    print(WRYY.getResponse(character, wordsList))
    print(character.getRelationship())
          
    
    
