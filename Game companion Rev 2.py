import time, random, os, Graphics

def points():
    os.system('cls')
    print(Graphics.Currentpoints)
    print(" ", Team1Name, "Points:", Team1Points)
    print(" ", Team2Name, "points:", Team2Points)
    time.sleep(5)
    menu()

def entrypass():
    global Team1Points
    global Team2Points
    os.system('cls')
    print(Graphics.Editpoints)
    print(" You are about to edit data. \n \n Press any button to edit score only \n Press E to full edit \n")
    L = input(" user: ")
    if L == "E" or L == "e":
        entry()
    elif L == "":
        os.system('cls')
        print(Graphics.Warning)
        print(" you are editing data")
        Team1Points = input(" Team 1 Points: ")
        Team2Points = input(" Team 2 Points: ")
        entrycheck()

def entry():
    global Team1Name
    global Team2Name
    global Team1Points
    global Team2Points
    os.system('cls')
    print(Graphics.Warning)
    print(" you are editing data")
    Team1Name = input(" Team 1 Name: ")
    Team2Name = input(" Team 2 Name: ")
    Team1Points = input(" Team 1 Points: ")
    Team2Points = input(" Team 2 Points: ")
    entrycheck()

def stage1():
    try: 
        print(Graphics.Gamecompanion)
        print(" Welcome to Game companion \n", Graphics.Rever)
        time.sleep(3)
        print(" \n Press N to exit, or press any key to get started")
        A = input(" user: ")
        if A == "N" or A == "n":
            stageExist()
        else:
            fsetup()
    except:
        print(" You are missing textual graphics module - pyfiglet, to install pyfiglet type:")
        print(" \"python - m install pyfiglet \"")
        time.sleep(3)
        print("\n  closing program")
        time.sleep(2)
        exit()

def menu():
    os.system('cls')
    print(Graphics.Menu)
    print(" Welcome to Game companion, main menu")
    time.sleep(1)
    print(" 1. Current Points \n 2. Edit Data \n 3. Flip a coin \n 4. Terminate program")
    B = input(" user: ")
    if B == "1" or B == "1.":
        points()
    elif B == "2" or B == "1.":
        entrypass()
    elif B == "3" or B == "3.":
        coins()
    elif B == "4" or B == "4.":
        stageExist()
    else:
        nodata()

def nodata():
    os.system('cls')
    print(Graphics.Warning)
    print(" You have left data empty")
    time.sleep(3)
    menu()

def entrycheck():
    try:
        if Team1Name == "":
            entryerror()
        elif Team2Name == "":
            entryerror()
        else:
            menu()
    except:
        entry()
    
def entryerror():
    os.system('cls')
    print(Graphics.Warning)
    print("You have left required data empty")
    time.sleep(3)
    entry()

def fsetup():
    os.system('cls')
    print(Graphics.Warning)
    print(" this is first time setup")
    time.sleep(3)
    entry()

def exitstage():
    try:
        Countdown = 10
        while Countdown > 0:
            os.system('cls') 
            print(Graphics.Finalpoints)
            print(" ", Team1Name, "Points:", Team1Points)
            print(" ", Team2Name, "points:", Team2Points)
            print("\n Closing program in", Countdown)
            time.sleep(1)
            Countdown = Countdown - 1
            if Countdown == 5:
                exiting(Countdown)
    except:
        exiting(Countdown)

def exiting(t):
    while t > 0:
        os.system('cls')
        print(Graphics.Bye)
        print("\n Closing program in", t)
        time.sleep(1)
        t = t - 1
        if t == 0:
            os.system('cls')
            print(Graphics.Bye)
            print(" Gamecompanion By Marcus Allison")
            print(Graphics.Rever)
            print("\n Terminated program")
            os._exit(1)

def toss():
    return random.choice(["Heads", "Tails"])

def coins():
    D = 3
    while D >= 0:
        os.system('cls')
        print(Graphics.Cointoss)
        print(D)
        time.sleep(1)
        D = D - 1
        if D == 0:
            os.system('cls')
            print(Graphics.Cointoss)
            print(" flipping coin")
            time.sleep(3)
            break
    os.system('cls')
    print(Graphics.Cointoss)
    t1 = toss()
    t2 = toss()
    t3 = toss()
    print(t1, t2, t3)
    time.sleep(5)
    os.system('cls')
    menu()

def stageExist():
    os.system('cls')
    print(Graphics.Warning)
    print("\n Are you sure you would like to terminate the program? \n Y: terminate \n N: back to menu")
    d = input("user: ")
    if d == "Y" or d == "y":
        os.system('cls')
        exitstage()
    elif d == "N" or d =="n":
        entrycheck()
    else: 
        os.system('cls')
        stageExist()

stage1()