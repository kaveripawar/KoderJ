import random
while True:
    user_choice=input("Enter teh choice from the given set ( rock,paper,scissors)")
    computer_actions=["rock","paper","scissor"]
    comp_choice=random.choice(computer_actions)
    print(f"\n You choice{user_choice} \n computer choice {comp_choice}.\n")
    if user_choice==comp_choice:
        print(f"Both players selected { user_choice} \n Tie!!!!!")
    elif comp_choice=="rock":
        if user_choice=="scissor":
            print("Rock smashes scissors! You loss!")
        else:
            print("Paper covers rock! You Win")
    elif comp_choice=="scissor":
        if user_choice=="paper":
            print("scissors cuts paper! You loss!")
        else:
            print("Rock smashes scissors! You Win")
    elif comp_choice=="paper":
        if user_choice=="scissor":
            print("scissors cuts paper! You Win !")
        else:
            print("Paper covers rock! You loss")
    play_again=input=("Play again ? (y/n):")
    if play_again.lower()!="y":
        break
    
    #or convert choice into number using random variable
    """randNO=random.randint(1,3)  if randNO==1: comp='rock' like this"""