
import random as rn




lives = 3
points_by_bot = 0
point_by_you = 0

print("rock paper scissor")
print("you have 3 lives")

while lives>=0:
    choice_available = ['rock', 'paper', 'scissor']
    ask = input("whats your choice ").lower()
    choice_by_bot = rn.choice(choice_available)
    print(choice_by_bot)
    if choice_by_bot == ask:
        print("null")
        points_by_bot+=0
        point_by_you+=0

    elif choice_by_bot == "rock" and ask == "scissor":
        print("bot wins")
        points_by_bot+=1
        lives-=1

    elif choice_by_bot == "rock" and ask == "paper":
        print("you win")
        point_by_you+=1
                        
    elif choice_by_bot == "paper" and ask == "scissor":
        print("you win")
        point_by_you+=1
                        
    elif choice_by_bot == "paper" and ask == "rock":
        print("bot wins")
        points_by_bot+=1
        lives-=1

    elif choice_by_bot == "scissor" and ask == "rock":
        print("you win")

    elif choice_by_bot == "scissor" and ask == "paper":
        print("bot wins")
        points_by_bot+=1
        lives-=1

    elif ask != "rock" or "paper" or "scissor":
        print("wrong input")

    print("you scored : ", point_by_you)
    print("bot scored : ", points_by_bot)

