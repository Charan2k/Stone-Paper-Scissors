import random

print("Welcome to Stone Paper Scissors Game:\n You will be judged in the best of 10 basis")
choices = ["s","p","c"]
comp_score = human_score = 0
count = 10

print("s - for snake \n press p - for paper \n press c - for scissors\n")
while count > -1:
    comp = random.choice(choices)
    human = input("Enter your choice: ").lower()
    if human in choices:
        if comp == "s":
            if human == "p":
                print(f"Your choice: {human} \t Computer Choice: {comp}")
                print("You Won this round")
                human_score += 1
            elif human == "c":
                comp_score += 1
                print("You lost this round")
            else:
                print("Tie")
            
                
        if comp == "p":
            if human == "c":
                print(f"Your choice: {human} \t Computer Choice: {comp}")
                print("You Won this round")
                human_score += 1
            elif human == "s":
                comp_score += 1
                print("You lost this round")
            else:
                print("Tie")
           
        
        if comp == "c":
            if human == "s":
                print(f"Your choice: {human} \t Computer Choice: {comp}")
                print("You Won this round")
                human_score += 1
            elif human == "p":
                comp_score += 1
                print("You lost this round")
            else:
                print("Tie")
                
                
        count = count - 1
        
    else:
        print("Wrong Choice, please choose again.")

print(f"Your Score is {human_score} \n Computer Score is {comp_score}")
if human_score > comp_score:
    print("Congrats. You have won this game.")
elif human_score == comp_score:
    print("Huhhh. It's a Tie.")
else:
    print("Ooops. You have Lost this Game.\n Better luck next time.")   
#print(comp)
