import time
from playsound import playsound

# System Variables
enableTest=False
playground=0

# Playground
if playground == 1 :
    # playsound('HappyBirthday.mp3')
    import turtle
    turtle.setup(500,500)
    turtle.Screen().bgcolor("blue")
    turtle.shape('turtle')

# Test runtime data
if enableTest == True :
    islName="Test"
    apt1Nick="Andrex"
    apt1Famly="Andrex"
    apt1Gender="male"
    apt1Personal="cool"
    apt1Birth="13/04/2001"
    gameStart=True

# Game Extra Content
marketIntro=f"'Hello! And welcome to the {islName} supermarket. Here are the food categories we sell: Dinners, lunches, deserts and drinks.\nWhat would you like to buy?\n'"
firstMsgKind = f"'Hello! my name is {apt1Nick}. I hope you have a wonderful day. Wait what!!? You look just like me!'"
firstMsgCool = f"'Yo! The name's {apt1Famly}. {apt1Nick} {apt1Famly}. What the-? You look just like me!'"
firstMsgCaut = f"'Wait.. So you're - me?? This is too much. I need a lie down. Now where's my portable mattress? I usually carry it with me everywhere since I'm such a cautious person. Anyway, pleased to meet you.'"
firstMsgEnerg = f"'🎵Laa Dee Daa, Doo Dee dee! I'm so full of energy!🎵 SO pleased to meet you. What wha-? You're like my, my doppleganger!'"
dinners = ['English Breakfast', 'Roast Dinner', 'Lasagne', 'Spaghetti Bolognese', 'Pasta with no sauce', 'Spaghetti with Meatballs', 'Chicken Wings', 'Vegetarian Pie', 'Pasta Pesto', 'Vegetarian meat', 'Pizza']
marketDin = "'We sell English Breakfast, Roast Dinner, Lasagne, Spaghetti Bolognese, Pasta with no sauce, Spaghetti with Meatballs, Chicken Wings, Vegetarian Pie, Pasta Pesto, Vegetarian meat and Pizza. Which dinner do you wish to purchase?'"
marketLunch = "'We sell Sandwiches, Crisps, Sausage Rolls, A range of salads, including Greek Salad, Caesar Salad, Lettuce and Rocket. Which lunch do you wish to purchase?'"
marketDesert= ""

# Intro
if enableTest == False :
    print("Ah yes, paradise. A beautiful island in an alternate dimension. All yours.")
    time.sleep(2.5)
    islName=input("But it needs a name. What will you call it?\n")
    print(islName + " Island! That's a wonderful name!")
    time.sleep(3)
    print("But we're not done yet. Now your paradise needs a resident. Try making them and their personality like yours!")
    time.sleep(2)
    apt1Nick=input("Please enter your lookalike's first name.\n")
    time.sleep(1.6)
    apt1Famly=input("What's their surname?\n")
    time.sleep(1.6)
    apt1Gender=input("What gender are they? Choose between male, female and non-binary")
    time.sleep(1.6)
    apt1Personal=input(f"Now {apt1Nick} needs a personality. How would you describe them? Choose between energetic, kind, cool and cautious.\n")
    time.sleep(2)
    apt1Birth=input(f"When was {apt1Nick} born? Please use UK format, e.g. 13/04/2001\n")
    if apt1Gender == "male" :
        print("Now your lookalike is ready! Let's visit his apartment.\n\n")
    if apt1Gender == "female" :
        print("Now your lookalike is ready! Let's visit her apartment.\n\n")
    if apt1Gender == "non-binary" :
        print("Now your lookalike is ready! Let's visit their apartment.\n\n")
    time.sleep(3)
    gameStart=True

# Game
if gameStart == True :
    if apt1Personal == "energetic" :
        print(firstMsgEnerg)
    if apt1Personal == "cautious" :
        print(firstMsgCaut)
    if apt1Personal == "cool" :
        print(firstMsgCool)
    if apt1Personal == "kind" :
        print(firstMsgKind)
    time.sleep(1.6)
    usrnamecall=input("'Okay, can I call you my lookalike?'\n")
    if usrnamecall == "yes" :
        print("'Okay, my lookalike!'")
    else :
        print("'I'll call you my lookalike anyway.'")
    time.sleep(1.6)
    print("'I'm a bit hungry. Could you get me some food?'\n\n")
    time.sleep(2)
    print(f"Uh oh. It seems like {apt1Nick} is hungry. Luckily for you, I've given you some money to get a supermarket on {islName} Island.\nI hope it will finish building soon.")
    time.sleep(3)
    print("How quick! It's already finished. Let's go inside.\n\n")
    time.sleep(1)
    initBuy=input(marketIntro)
    if initBuy == "dinner" :
        initBuy=input(marketDin)
    if initBuy == "lunch" :
        initBuy=input(marketLunch)
    if initBuy == "desert" :
        initBuy=input()
    if initBuy == "drinks" :
        initBuy=input()
    print(f"You have just bought {apt1Nick}'s first consumable!")
    time.sleep(1)
    print("Let's head back to the apartment building.")
