from tkinter import *
import conversation
import characters

class Gui:
    julietText = open(r'juliet.txt', 'r').readlines()
    caputiaText = open(r'caputia.txt', 'r').readlines()
    def __init__(self, window):

        self.juliet = characters.Character("Juliet", 1, 1, 100, Gui.julietText)
        self.caputia = characters.Character("Caputia", 100, 1, 100, Gui.caputiaText)

        self.workingConversation = conversation.Speak()
        self.workingCharacter = self.juliet
        
        self.root = window

        self.faceFrame = Frame(self.root)
        self.speechFrame = Frame(self.root)
        self.choiceFrame = Frame(self.root)


        self.name = Label(self.faceFrame, text="Name")

        self.speech = Label(self.speechFrame, text="Stuff", wraplength=200)

        self.choice1 = Button(self.choiceFrame, text="Choice1", command=lambda: self.choice(0), wraplength=200)
        self.choice2 = Button(self.choiceFrame, text="Choice2", command=lambda: self.choice(1), wraplength=200)
        self.choice3 = Button(self.choiceFrame, text="Choice3", command=lambda: self.choice(2), wraplength=200)
        self.choice4 = Button(self.choiceFrame, text="Choice4", command=lambda: self.choice(3), wraplength=200)
        self.choice5 = Button(self.choiceFrame, text="Choice1", command=lambda: self.choice(4), wraplength=200)
        

        self.initialFrame = Frame(self.root)
        self.submitName = Button(self.initialFrame, text="Start", command=self.begin)

        self.submitName.pack(side='right')
        self.initialFrame.pack()
                                 

    def begin(self):
        self.initialFrame.destroy()
        self.talk(self.juliet)

    def talk(self, character):
        #Conversation
        juli = self.workingConversation
        wordsList = character.wordTake()
        self.workingCharacter = character

        self.name.config(text=character.getName())
        topic = juli.getScene(character, wordsList)
        self.speech.config(text = topic)

        choices = juli.getChoices(character, wordsList)
        self.makeChoice(choices)

    def makeChoice(self,option):
        self.choice1.config(text=option[0])
        self.choice2.config(text=option[1])
        self.choice3.config(text=option[2])
        self.choice4.config(text=option[3])
        self.choice5.config(text=option[4])
        self.render()

    def talk2(self):
        #Conversation2
        character = self.workingCharacter
        juli = self.workingConversation
        wordsList = character.wordTake()
    
        response = juli.getResponse(character, wordsList)
        juli.setStage(juli.getStage()+1)
        self.speech.config(text = response)
        

        choices = juli.getChoices(character, wordsList)
        self.makeChoice2(choices)
        
        response = juli.getResponse(character, wordsList)
        juli.setStage(0)
        
        
        character.addHistory(1)
        juli = conversation.Speak()

    def makeChoice2(self,option):
        self.choice1.config(text=option[0])
        self.choice2.config(text=option[1])
        self.choice3.config(text=option[2])
        self.choice4.config(text=option[3])
        self.choice5.config(text=option[4])
        self.render()

    def choice(self, num):
        self.workingConversation.setOption(num)
        self.talk2()
        
    def render(self):
        self.name.pack()
        self.speech.pack()
        self.choice1.pack()
        self.choice2.pack()
        self.choice3.pack()
        self.choice4.pack()
        self.choice5.pack()

        self.faceFrame.pack(side='top')
        self.speechFrame.pack(side='top')
        self.choiceFrame.pack(side='top')
        
