"""Birthday Paradox Simulation,
Explore the suprising probabilities of the "Birthday Pardox"
Tags: short, math, simulation"""

import random, datetime

def getBirthdays(numberofBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for _ in range(numberofBirthdays):
        #The year is unimportant for our simulation, as long as all birthdays have the same year.
        startofYear = datetime.date(2001, 1, 1)

        #Get a random day into the year:
        randomNumberofDays = datetime.timedelta(random.randint(0, 364))
        birthday = startofYear + randomNumberofDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None #All birthdays are unique, so return None

    #Compare  each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for _, birthdayB in enumerate(birthdays[a +1:]):
            if birthdayA == birthdayB:
                return birthdayA #Return the mathing birthday.
            
#Display the intro:
print("""Birthday Paradox,
      
The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is suprisingly large.
This program does a Monte Carlo simulation that is,repeated random simulations) to expolore this concept.
      
(It's not actually a paradox, it's just a suprising result.)
""")

#Set up a tuple of month names in order:
MONTHS = ('January', 'Febuary', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

while True: #Keep asking until the user enters a valid number:
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #User has entered a valid amount.
print()

#Generate and display the birthdays: 
print("Here are,", numBDays, 'birthdays: ')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Display a coma for each birthday after the first birthday.
        print(', ', end = " ")
    monthName = MONTHS[birthday.month -1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end = "")
print()
print()

#Determine if there are two birthdays that match.
match = getMatch(birthdays)

#Displays the results:
print('In this simulation, ', end = '')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print("There are no matching birthdays.")
print()

#Run through 100,000 simulations: 
print("Generating", numBDays, 'random birthdays 100,000 times.....')
input('Press Enter to begin....')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 #How many simulations had matching birthdays in them.
for i in range (100_000):
    #Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run....')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

#Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people there was a')
print('mathcing birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('That\'s probably more than you would think!  ')