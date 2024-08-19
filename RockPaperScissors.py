import random

secimler = ["Rock", "Paper", "Scissors"]

def kullanici_secim():
    secim = input("Choose your weapon: Rock, Paper, or Scissors?\n")
    if secim not in secimler:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return kullanici_secim()
    return secim

def mac():
    secim1 = kullanici_secim()
    
    if secim1 is None:
        return None
    
    blg_secim = random.choice(secimler)
    print(f"You chose: {secim1}")
    print(f"The computer chose: {blg_secim}")
    if secim1 == blg_secim:
        print("It's a tie! Great minds think alike.")
        return 0
    elif (secim1 == "Rock" and blg_secim == "Scissors") or \
        (secim1 == "Paper" and blg_secim == "Rock") or \
        (secim1 == "Scissors" and blg_secim == "Paper"):
        print("You won this round! Well played!")
        return 1
    else:
        print("You lost this round! The computer got lucky.")
        return -1

def game():
    kullanskor = 0
    blgskor = 0
    i = 1
    while True:
        print(f"Round {i} - Fight!")
        sonuc = mac()
        if sonuc is None:
            break
        
        if sonuc == 1:
            kullanskor += 1
        elif sonuc == -1:
            blgskor += 1
        
        if blgskor == 2:
            print("The computer is victorious! Better luck next time!")
            break
        elif kullanskor == 2:
            print("Congratulations! You won the match!")
            break
        else:
            print(f"Score after round {i}: You {kullanskor} - Computer {blgskor}")
        i += 1
    againask()

def againask():
    again = input("Would you like to play? Yes or No\n")
    comp_again = random.choice(["Yes", "No"])
    if again == "Yes" and comp_again == "Yes":
        print("Great! Let's play again!")
        return game()
    elif again == "Yes" and comp_again == "No":
        print("I'm sorry, but I can't play another game right now.")
        return None
    elif again == "No" and comp_again == "Yes":
        print("Oh, backing out, huh? Maybe next time!")
        return None
    elif again == "No" and comp_again == "No":
        print("Thanks for playing! Come back anytime for a rematch.")
        return None
    else:
        print("Invalid response! Please type Yes or No.")
        return againask()

print("Welcome to the ultimate Rock, Paper, Scissors showdown!")
print("Here's how to play:")
print("1. You and the computer will each choose one of three options: Rock, Paper, or Scissors.")
print("2. Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock.")
print("3. The first to win two rounds claims victory!")
print("Are you ready? Let's get started!")
againask()
