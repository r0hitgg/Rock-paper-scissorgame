import random

print('''Hii Welcome To The Game Rock,paper,scissor 
      Press r to choose rock 
      press p to choose paper 
      press s to choose scissor''')

def play():
    global userin
    global cpu

    userin = input("Please Enter Your choice::::: ")

    if (userin != "r") and (userin != "p") and (userin != "s"):
        print("please Enter valid input")
        userin = input("Please Enter Your choice::::: ")

    x = ["Rock","Paper","Scissor"]
    cpu = random.choice(x)
    print(cpu)

def winnercheck():
    global nonew
    global cpuwin
    global userwin
    nonew = False
    cpuwin = False
    userwin =False
    if userin == "r":
        if cpu == "Rock":
            nonew = True
        if cpu == "Paper":
            cpuwin = True
        if cpu == "Scissor":
            userwin = True

    if userin == "p":
        if cpu == "Paper":
            nonew = True
        if cpu == "Scissor":
            cpuwin = True
        if cpu == "Rock":
            userwin = True

    if userin == "s":
        if cpu == "Scissor":
            nonew = True
        if cpu == "Rock":
            cpuwin = True
        if cpu == "Paper":
            userwin = True

def result():
    if nonew == True:
        print("No one Win")
    if cpuwin == True:
        print("CPU WINS. Better luck next Time")
    if userwin == True:
        print("Yo win ")

while(True):
    play()
    winnercheck()
    result()

    r = input("Wanna Play Again? press any key for continue playing ,, press n for quit")
    if (r == "n") or (r == "N"):
        break
    else:
        pass
