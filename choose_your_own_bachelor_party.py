# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:53:27 2015

@author: spark
"""

"""
Boot into shell mode
Modify your file /etc/default/grub with

GRUB_CMDLINE_LINUX_DEFAULT="text"
and do sudo update-grub. The machine will boot in text mode.

To start the graphical interface you do
sudo service lightdm start
"""

"""
Cheat codes
snooze 20 minutes: fuck off
refresh options: fuck that
bring up random options: bored
"""

import time
import os
import re
import select
import sys
import random


TEXT_DISPLAY_TIME = 2
debug = False

# print a block of text to the screen with word wrap
def wrapPrint(strs):
    for x in strs.splitlines():
        print '\n'.join(line.strip() for line in re.findall(r'.{1,80}(?:\s+|$)', x))

def printWrongChoice():
    wrongMessages = ['Pick a letter, dumbass!', 'Jim decided to get one of his brothers to help him with this tricky typing thing.', 'Try again', 'That wasn\'t one of the options', 'Invalid cheat code', 'Keep trying']
    random.shuffle(wrongMessages)
    os.system('clear')
    wrapPrint(wrongMessages[0])
    print "\n"
    # TODO add more messages

# prompt for random adventure
def randomAdventure(endTime):   
    # clear screen 
    os.system('clear')
    os.system('say "bong bong bong bong bong"')
    
    # List of activities
    randomActivities = ['play Battle for Middle Earth', 'play Age of Empires', 'play Poker', 'play Pairs', 'play Pitch' ,'play Can Jam', 'play Polish Horseshoes', 'hit balls at a Driving Range', 'play Frisbee Golf', 'play shuffleboard', 'play Bumper pool', 'play spikeball', 'eat my shorts', 'turn steve into a Newt', 'play Calvinball', 'play True Americans', 'piss in the dirt and play in the mud', 'play 2 on 2 quidditch', 'play 2 on 2 telephone', 'play 2v2 trivia: colors that are red', 'play 2v2 trivia: current black presidents', 'play 2v2 trivia: will this hurt if you put it in your mouth?']

    # Random adventure message 
    # TODO make several messages that are randomly selected
    wrapPrint("For his next adventure, Jim decided to \n")
    
    # shuffle activities
    random.shuffle(randomActivities)    
    
    # Prompt first three options 
    message_prompt = "a) " + randomActivities[0] + "\nb) "  + randomActivities[1] + "\nc) "  + randomActivities[2]  + "\nd) " + randomActivities[3] + "\ne) "  + randomActivities[4]  + "\nf) drink a beer\n"
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c') and (choice.lower() != 'd') and(choice.lower() != 'e') and(choice.lower() != 'f') and (choice.lower() != 'fuck that')):
        printWrongChoice()
        choice = raw_input(message_prompt)
    if (choice.strip() == 'fuck that'):
        os.system('clear')
        print "fucking it!"
        time.sleep(1)
        randomAdventure(endTime)
    elif (choice == 'a'):
        os.system('clear')
        print "Go " + randomActivities[0]
        time.sleep(TEXT_DISPLAY_TIME) 
    elif (choice == 'b'):
        os.system('clear')
        print "Go " + randomActivities[1]
        time.sleep(TEXT_DISPLAY_TIME) 
    elif (choice == 'c'):
        os.system('clear')
        print "Go " + randomActivities[2]
        time.sleep(TEXT_DISPLAY_TIME) 
    elif (choice == 'd'):
        os.system('clear')
        print "Go " + randomActivities[3]
        time.sleep(TEXT_DISPLAY_TIME) 
    elif (choice == 'e'):
        os.system('clear')
        print "Go " + randomActivities[4]
        time.sleep(TEXT_DISPLAY_TIME)
    elif (choice == 'f'):
        os.system('clear')
        print "Go drink a beer!!"
        time.sleep(TEXT_DISPLAY_TIME) 
        randomAdventure(endTime)
    else:
        os.system('clear')
        print "Error"
        time.sleep(TEXT_DISPLAY_TIME)
        randomAdventure(endTime)
    
    # back to adventure screen
    adventureScreen(endTime)
        
def adventureScreen(endTime):
    os.system('clear')
    print "Adventure!!"
    if (debug):
        startTime = time.time()
        while (time.time() < (startTime + 10)):
            i, o, e = select.select( [sys.stdin], [], [], 10 )
            if (i):
                cheatCode = sys.stdin.readline()
                time.sleep(TEXT_DISPLAY_TIME) 
                if (cheatCode.strip() == 'bored'):
                    randomAdventure(endTime)  
    else:
        while (time.time() < time.mktime(endTime)):
            i, o, e = select.select( [sys.stdin], [], [], 10*60 )
            if (i):
                cheatCode = sys.stdin.readline()
                time.sleep(TEXT_DISPLAY_TIME) 
                if (cheatCode.strip() == 'bored'):
                    randomAdventure(endTime)  

def breakfastPrompt():
    os.system('say "OK ass hat, rise and shine!"')
    print "Where do you want to to get your bacon?\n"
    choiceA = "cook it\n"
    choiceB = "make a restaurant cook it\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB 
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b')):
        if (choice.lower() == 'fuck off'): # snooze 20 minutes
            # clear screen
            os.system('clear')
            
            print "Adventure!!!"
            time.sleep(20*60) 
            os.system('say "Are you hungry yet?"')
        printWrongChoice()
        choice = raw_input(message_prompt)
    # home
    if (choice.lower() == 'a'):
        print "What do you want with your bacon?\n"
        choiceA = "pancakes!\n"
        choiceB = "waffles!\n"
        choiceC = "french toast!\n"
        choiceD = "omelettes!\n"
        choiceE = "cake!\n"
        message_prompt = "a) " + choiceA + "b) "  + choiceB  + "c) "  + choiceC + "d) "  + choiceD + "e) "  + choiceE
        choice = raw_input(message_prompt)
        while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c') and (choice.lower() != 'd') and (choice.lower() != 'e')):
            printWrongChoice()
            choice = raw_input(message_prompt)
        
        # return to adventure screen
        
    #restaurant
    else:
        os.system('clear')
        print "Jim decided to go to:\n" 
        choiceA = "Mystery Breakfast at Awesome little diner \n"
        choiceB = "Breakfast Burrito\n"
        choiceC = "Non mystery breakfast at awesome little diner\n"
        message_prompt = "a) " + choiceA + "b) "  + choiceB  + "c) "  + choiceC 
        choice = raw_input(message_prompt)
        while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c')):
            printWrongChoice()
            choice = raw_input(message_prompt)
        os.system('clear')
        print "Good choice!"
        time.sleep(TEXT_DISPLAY_TIME)

def introMessage():
    #Intro message
    # program starts at 5am, June 20, 2014
    os.system('say "Knock knock. Wake up, Jim."')
    time.sleep(2)
    os.system('say "Wake up! Wake up! Wake up! Are you up yet? If you are, say SHUT UP."')
    time.sleep(2)
    os.system('say "ha ha ha you thought we made voice recognition software for a silly bachelor party program? anyway, wake up!"')
    message_intro = "Jim was awoken at an ungodly hour to discover that his asshole brothers and his 'friend' Will had wrangled him into some kind of stupid Choose-Your-Own-Adventure game for his bachelor party.  What the hell is wrong with those guys!?\n\nHe decided to...\n\n"
    choiceA = "spring out of bed and engage in a naked Jello wrestling match with Will\n"
    choiceB = "go back to sleep\n"
    choiceC = "eat bacon!\n"
    choiceBeer = "drink a beer\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB + "c) " + choiceC + "d) " + choiceBeer
    wrapPrint(message_intro)
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c')):
        #Drink a beer
        if (choice.lower() == 'd'):
            # clear screen
            os.system('clear')
            
            print "Drink a beer!"
            time.sleep(TEXT_DISPLAY_TIME)
            
            # clear screen
            os.system('clear')
            
            print "And then?\n"
        elif (choice.lower() == 'fuck off'): # snooze 20 minutes
            # clear screen
            os.system('clear')
            
            print "Adventure!!!"
            if (debug):
                time.sleep(10) 
            else:
                time.sleep(20*60) 
            os.system('say "Wake up, lazy! It\'s time for adventures"')
        else:
            print printWrongChoice()
        choice = raw_input(message_prompt)
    
    
    # clear screen
    os.system('clear')
    
    breakfast_chosen = False
    
    # Jello wrestle
    if (choice.lower() == 'a'):
        print "OK!  Let\'s do this!!!!" 
        time.sleep(TEXT_DISPLAY_TIME)
        
    # Go back to sleep
    elif (choice.lower() == 'b'):
        print "Good choice.  Sweet dreams!"
        time.sleep(TEXT_DISPLAY_TIME)
    
    # Eat breakfast
    elif (choice.lower() == 'c'):
        # prompt home/restaurant
        breakfast_chosen = True
        breakfastPrompt()
    
    else:
        print "Error"
        time.sleep(TEXT_DISPLAY_TIME)
        introMessage()
    
    return breakfast_chosen

def lunchPrompt():
    os.system('clear')
    os.system('say "bong bong bong bong bong"')
    time.sleep(5)
    os.system('say "Hey, get over here!"')

    print "After a morning of adventuring, Jim started to get hungry again.\n"
    choiceA = "He decided to grill up some delicious burgers.\n"
    choiceB = "He couldn't take the smell of his brothers and Will in confined \nquarters anymore, so he decided to go out to a restaurant.\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB 
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b')):
        if (choice.lower() == 'fuck off'): # snooze 20 minutes
            # clear screen
            os.system('clear')
            
            print "Adventure!!!"
            if (debug):
                time.sleep(10) 
            else:
                time.sleep(20*60) 
            os.system('say "Are you hungry yet?"')
        printWrongChoice()
        choice = raw_input(message_prompt)
    # home
    if (choice.lower() == 'a'):
        wrapPrint('What are you waiting for.. go make the damn burgers!')
        # return to adventure screen
        
    #restaurant
    else:
        print "Jim decided to go to:?\n" # TODO
        choiceA = "Hibachi/Sushi\n"
        choiceB = "Awesome kinda creepy italian place\n"
        choiceC = "Good mexican food\n"
        choiceD = "Smoke House that is supposed to be awesome\n"
        choiceE = "Drive around and pick a restaurant that looks good\n"
        message_prompt = "a) " + choiceA + "b) "  + choiceB  + "c) "  + choiceC + "d) "  + choiceD + "e) "  + choiceE
        choice = raw_input(message_prompt)
        while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c') and (choice.lower() != 'd') and (choice.lower() != 'e')):
            printWrongChoice()
            choice = raw_input(message_prompt)
        #choices
        #prompt
        # return to adventure screen


def dinnerPrompt():
    os.system('clear')
    os.system('say "bong bong bong bong bong"')
    time.sleep(5)
    os.system('say "HEY come back its eating time!"')

    print "After an afternoon of playing this stupid game, \nJim started to get hungry again.\n"
    choiceA = "He decided to grill up some delicious burgers.\n"
    choiceB = "He couldn't take the monotony of being in the \nhouse and decided to go out for dinner.\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB 
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b')):
        if (choice.lower() == 'fuck off'): # snooze 20 minutes
            # clear screen
            os.system('clear') 
            
            print "Adventure!!!"
            if (debug):
                time.sleep(10) 
            else:
                time.sleep(20*60) 
            os.system('say "Are you hungry yet?"')
        printWrongChoice()
        choice = raw_input(message_prompt)
    # home
    if (choice.lower() == 'a'):
        os.system('say "you dont need to wait for my permission, go eat!"')

        wrapPrint('What are you waiting for.. go make the damn burgers!')
        # return to adventure screen
        
    #restaurant
    else:
        print "Jim decided to go to:\n" # TODO
        choiceA = "Hibitchi/Sushi!\n"
        choiceB = "Awesome kinda creepy italian place!\n"
        choiceC = "Good mexican food!\n"
        choiceD = "Smoke House that is supposed to be awesome!\n"
        choiceE = "Drive around and pick a restaurant that looks good!\n"
        message_prompt = "a) " + choiceA + "b) "  + choiceB  + "c) "  + choiceC + "d) "  + choiceD + "e) "  + choiceE
        choice = raw_input(message_prompt)
        while ((choice.lower() != 'a') and (choice.lower() != 'b') and (choice.lower() != 'c') and (choice.lower() != 'd') and (choice.lower() != 'e')):
            printWrongChoice()
            choice = raw_input(message_prompt)
        #choices
        #prompt
        # return to adventure screen

def escapeRoomPrompt():
    os.system('clear')
    os.system('say "ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha!"')

    print "Uh oh, Scott and Steve have that glint in their eyes again.  Now what?\n"
    choiceA = "Walk to sketchy building as it starts to get dark and hope not to get mugged!\n"
    choiceB = "Lube up with vaseline before walking to sketchy building as it starts to get \ndark to make for easy escapes in case of mugging\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB 
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b')):
        printWrongChoice()
        choice = raw_input(message_prompt)
    # home
    #wrapPrint("The first hint is ..." )
    # TODO what the hell is the first hint?  
        
def stripperPrompt():
    os.system('clear')
    os.system('say "bong bong bong bong bong"')
    time.sleep(5)
    os.system('say "Hey baby, are you, RNA helicase? Because I would love to unzip your jeans."')

    print "What's that you say?  What do you mean this isn't a proper bachelor party!?\n\nLet\'s crank this party up a notch."
    choiceA = "Get a stripper!\n"
    choiceB = "Get a beer and a stripper!\n"
    message_prompt = "a) " + choiceA + "b) "  + choiceB 
    choice = raw_input(message_prompt)
    while ((choice.lower() != 'a') and (choice.lower() != 'b')):
        os.system('clear')
        print "You can't get out of that this easily...\n"
        choice = raw_input(message_prompt)
    time.sleep(TEXT_DISPLAY_TIME)
    os.system('say "Allll right.  Bow chicka bow oooowwwww!"')
    wrapPrint("Allll right.  Bow chicka bow boooowwwww") 
    time.sleep(TEXT_DISPLAY_TIME)    

# clear screen
os.system('clear')

#define times
#tm_year=2015, tm_mon=6, tm_mday=17, tm_hour=0, tm_min=3, tm_sec=58, tm_wday=2, tm_yday=168, tm_isdst=1
# 8:00 AM
TIME_630  = (2015, 6, 20, 6, 30, 00, 5, 171, 1) # 6:30 am
TIME_930  = (2015, 6, 20, 9, 30, 00, 5, 171, 1) # 9:30 am
TIME_1030 = (2015, 6, 20, 10, 30, 00, 5, 171, 1) # 10:30 am
TIME_1200 = (2015, 6, 20, 12, 00, 00, 5, 171, 1) # 12:00 pm
TIME_1300 = (2015, 6, 20, 13, 00, 00, 5, 171, 1) # 1:00 pm
TIME_1700 = (2015, 6, 20, 17, 00, 00, 5, 171, 1) # 5:00 pm
TIME_1800 = (2015, 6, 20, 18, 00, 00, 5, 171, 1) # 6:00 pm
TIME_1900 = (2015, 6, 20, 19, 00, 00, 5, 171, 1) # 7:00 pm
TIME_2000 = (2015, 6, 20, 20, 00, 00, 5, 171, 1) # 8:00 pm
TIME_2100 = (2015, 6, 20, 21, 00, 00, 5, 171, 1) # 9:00 pm
TIME_2200 = (2015, 6, 20, 22, 00, 00, 5, 171, 1) # 10:00 pm
TIME_2300 = (2015, 6, 20, 23, 00, 00, 5, 171, 1) # 11:00 pm
TIME_2330 = (2015, 6, 20, 23, 30, 00, 5, 171, 1) # 11:30 pm
TIME_TMRW = (2015, 6, 21, 23, 30, 00, 5, 171, 1) # 11:30 pm

# Intro message - 5:00 am
breakfast_chosen = introMessage()

# Did we eat breakfast?
if (breakfast_chosen):
    adventureScreen(TIME_630)
else:
    # Adventure screen until 9:30
    adventureScreen(TIME_930)
    os.system('clear')
    print "Time for breakfast!\n\n"
    breakfastPrompt()
    adventureScreen(TIME_1030)

# 10:30 am Random adventure after breakfast
randomAdventure(TIME_1200)

# 12:00 pm Eat lunch
lunchPrompt()
adventureScreen(TIME_1700)
randomAdventure(TIME_1900)

# 7:00 pm Escape the Room
escapeRoomPrompt()
adventureScreen(TIME_2100)

# 9:00 pm Eat Dinner
dinnerPrompt()
adventureScreen(TIME_2200)
randomAdventure(TIME_2300)

#11pm prompt for stripper
stripperPrompt()
adventureScreen(TIME_2330)
randomAdventure(TIME_TMRW)

exit() 
