import random

options = ["r", "p", "s"]


def main():

    games = 0
    wins = 0
    loses = 0
    ties = 0

    user_choice = ""
    previous_user_choice = ["r"]
    results = [None]

    while user_choice != "quit":

        user_choice = input("Choose: write R for rock, P for paper, and S for scissors,\
            \nor if you want to finish the game write 'quit': ").lower()

        comp_choice = random.choice(options)

        previous_user_choice[0] = user_choice

        if comp_choice == "r" and user_choice == "s":
            result = "You Lose"
            results[0] = result

        elif comp_choice == "r" and user_choice == "p":
            result = "You Win!"
            results[0] = result

        elif comp_choice == "s" and user_choice == "r":
            result = "You Win!"
            results[0] = result

        elif comp_choice == "s" and user_choice == "p":
            result = "You Lose"
            results[0] = result

        elif comp_choice == "p" and user_choice == "s":
            result = "You Win!"
            results[0] = result

        elif comp_choice == "p" and user_choice == "r":
            result = "You Lose"
            results[0] = result

        elif comp_choice == user_choice:
            result = "Tie"
            results[0] = result
        
        elif user_choice == "quit":
            result = None
            results[0] = result
        else:
            result = ""
            results[0] = result

        if results[0] == "You Win!":
            wins += 1

        if results[0] == "You Lose":
            loses += 1

        if results[0] == "Tie":
            ties += 1

        if results[0] == None:
            result = random.choice(options)

        if results[0] == "":
            result = "You wrote a different letter. Please write R, P, S or 'quit' to finish the game"

        if user_choice != "quit":
            games = (wins + loses + ties)

            print(f"ROUND: {games}")
            print(f"You chose: {user_choice.upper()} and the computer chose: {comp_choice.upper()}")
            print(f"RESULT: {result.upper()}")
            print()

        print(f"Wins:{wins} | loses:{loses} | ties:{ties} ")

    total_rounds = wins + loses + ties
    percentage_user = (wins / (wins + loses)) * 100
    percentage_comp = 100 - percentage_user

    print(f"You played a total of {total_rounds} rounds.")
    print(f"You won {wins} times.")
    print(f"You lost {loses} times.")
    print(f"There were {ties} ties.")
    print(f"Which means that you beat the computer {percentage_user:.1f}% of the times")
    print(f"and the computer beat you {percentage_comp:.1f}% o the times.")

def next_choice(results, previous_user_choice):

    if results == "You Win!":
        next_comp_choice = beat_choice(previous_user_choice)

    if results == "You Lose":
        next_comp_choice = previous_user_choice

    if results == "Tie":
        next_comp_choice = beat_choice(previous_user_choice)

    if results == None:
        next_comp_choice = random.choice(options)
    
    if results == "":
        next_comp_choice = random.choice(options)

    return next_comp_choice

def beat_choice(choice):

    next_choice = ""

    if choice == "r":
        next_choice = "p"
    if choice == "p":
        next_choice = "s"
    if choice == "s":
        next_choice = "r"
    return next_choice

if __name__ == "__main__":
    main()