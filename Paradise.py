import time

enableTest=True
# Italic text
txt = '\x1B[3mThis is italic text\x1B[23m'
print(txt)

if enableTest == True :
    islName="Test"
    apt1Nick="Andrex"
    apt1Famly="Andrex"
    apt1Gender="male"
    apt1Personal="cool"
    apt1Birth="13/04/2001"
    gameStart=True

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
    print("Now your lookalike is ready! Let's visit their apartment.\n\n")
    time.sleep(3)
    gameStart=True

if gameStart == True :
    firstMsgKind = f"'Hello! my name is {apt1Nick}. I hope you have a wonderful day. Wait what!!? You look just like me!'"
    firstMsgCool = f"'Yo! The name's {apt1Famly}. {apt1Nick} {apt1Famly}. What the-? You look just like me!'"
    firstMsgCaut = f"'Wait.. So you're - me?? This is too much. I need a lie down. Now where's my portable mattress? I usually carry it with me everywhere since I'm such a cautious person. Anyway, pleased to meet you.'"
    firstMsgEnerg = f"'🎵Laa Dee Daa, Doo Dee dee! I'm so full of energy!🎵 SO pleased to meet you. What wha-? You're like my, my doppleganger!'"
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
    print(f"Uh oh. It seems like {apt1Nick} is hungry. Luckily for you, I've given you some money to get a supermarket on {islName}\nI hope it will finish building soon.")
    time.sleep(3)
    print("How quick! It's already finished. Let's go inside.")
    time.sleep(1)
    