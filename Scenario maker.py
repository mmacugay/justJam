import random

time = ['Tribal', 'Medieval', 'Victorian', 'Modern', 'Future']
people = ['Deserted place', 'Rural place', 'Suburban place', 'Urban place', 'Mass Congegration of people.']
theme = ['Might Makes right / Survival of the Fittest', 'Run', 'Hide', 'Something is very wrong here / The Power of Friendship', "Let's play a game..."]
cast = ['"Fight me" people', 'Cowards', 'People that act friendly (Something is very wrong here)', 'Overly prideful peeps', 'Aliens?']

print('It is a ' + time[int(random.random()*5)] + ' time')
print('You are in a ' + people[int(random.random()*5)])
print('The philosophy is ' + theme[int(random.random()*5)])
print('Your people are ' + cast[int(random.random()*5)])
