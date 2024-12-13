import characters
import conversation
def story():
    #victorinoText = open(r'victorinoText').readlines()
    #victorino = characters.Character("Victorino", 2, 0, 10, victorinoText)
    #alphonsoText = open(r'alphonsoText').readlines()
    #alphonso = characters.Character("Alphonso", 2, 2, 10, alphonsoText)
    julietText = open(r'juliet.txt', 'r').readlines()
    juliet = characters.Character("Juliet", 1, 1, 100, julietText)
    #king = Character("Konig Reich", 13, 2, 5)
    #ambro = Character("Ambro", 5, 2, 5)
    #julius = characters.Character("Julius Caesar", 15, 0, 0)
    caputiaText = open(r'caputia.txt', 'r').readlines()
    caputia = characters.Character("Caputia", 100, 1, 100, caputiaText)
    #pope = Character("The Pope", 50, 1, 50)

    print('In this game, you will be given a scene, along with a list of numbers. These are your choices. Enter the number you would like to say, and enjoy your text adventure.')
    name = input("Enter Name: ")
    print("You are", (name), "You live at Colkirk with Juliet your long life childhood friend. You came here after the Jampocalypse. You notice Juliet running towards you")


    conversation.talk(juliet)

    print('You get stuff for dinner with Juliet. She takes her time shopping, as she slowly hands you bags of food for dinner, along with some other trinkets she finds interesting. Seeing you two with so much stuff, a group of ruffians decide to mess with you, looking for some coin.')

    print("We don't have a fighting system, so, um...you win?") #Fight

    conversation.talk(juliet)


    print("Instead of following Juliet like a puppy, you go off to have fun in the town. What would you like to do?")
    print("1.) Go shopping again. \n 2.) Visit your home. \n 3.) Meet another friend. \n 4.) follow Juliet like a puppy. \n 5.) Stand still.")
    answer = input("Choose a number 1-5")
    print("Okay, okay, I'm just kidding. You actually have no choice, so instead of your answer of '" + answer + ",' you'll just automatically get 4. You meet up with your other friend Caputia, a friend whom you met while learning your trade from your father.")

    conversation.talk(caputia)

    print("So, um...can we pretend you just played a minigame to get a jar of peanut butter? Yeah, thanks.")

    print("Shortly after collecting the peanut butter from the house, you meet up again with Caputia who celebrates. Then the sky darkens, and jam falls from the sky. The people in the village are in panic. The day which the refugees from the jamapocalypse which rocked Italy feared has come.")

    conversation.talk(caputia)


    print("After parting with Caputia, you are left alone. Thrust into the madness of the village, you miraculously come across Juliet.")

    conversation.talk(juliet)

    print("After embarking on an, admittedly forced, adventure with your friend Juliet, the two of you are forced to fend for your lives. You come across a slime.")
    print("You fight!")
    print("Or at least, you were supposed to. We don't have fighting scenes yet.") #Fight
    print("After the gruelling fight, you and Juliet are forced to rest. While resting, a slime comes your way again! Instead of getting into action though, you are both forced to spectate as another person comes in. With the sound of thunder, a man uses a compact-looking crossbow to take out the slime in one shot. This man introduces himself as Alphonso. He tells you about a land called the 'modern world,' and asks for your help.")

    conversation.talk(juliet)

    print("You continue your adventure with Juliet and Alphonso, and as soon as the castle is on the horizon, the three of you meet a new person. This man dresses in flashy clothing, not too different from that of nobles, but colored brown and decorated with dirt. He has a large hat on his head, and two Big Irons on his hip. Just as the two lumps of iron look, he calls them Big Irons as well. Alphonso is instantly impressed by his looks, and dons the look of a child as he interacts with him. Alphonso confesses that he has a love for Wild West shows.")

    conversation.talk(juliet)

    print("From here on the story continues, but the game does not. Consider this a demo, or a random assignment a group of disorganized kids made. Either way, I hope you had fun, and that we got a good grade.")


    
    
story()
