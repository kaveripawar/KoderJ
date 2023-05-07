import random
rn=random.randint(1,100)
# print(rn)
ug=None
g=0

while(ug!=rn):
    ug=int(input("Enter choice :"))
    g=g+1
    if(ug==rn):
        print("you win !")
    else:
        if(ug>rn):
            print("you loss! please enter small no")
        else:
             print("you loss! please enter large no")
            
print(f"you guessed the number in {g} guesses ")
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
if(g<hiscore):
    print("you have broken the high score !!!!!")
    with open("hiscore.txt","w") as f:
        f.write(str(g))

    