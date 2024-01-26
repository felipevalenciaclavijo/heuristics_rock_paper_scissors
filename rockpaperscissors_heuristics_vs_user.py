import random

# options available when playing rock, paper, and scissors
options = ["r", "p", "s"]


def main():

    # variables referenced to count total games played, wins, loses, and ties
    rounds = 0
    wins = 0
    losses = 0
    ties = 0

    # variable used to avoid reference errors:
    user_choice = ""
    # This is the list that is going to be changing each round,
    # storing user's previous choice:
        # Since in round 1 there's no previous user choice, I decided to
        # tell my AI to always think that in Round 0 the user chose Rock
    previous_user_choice = ["r"]

    # This is the list that is going to be changing each round,
    # storing round's result:
    results = [None]

    # This going to loop until the user writes 'quit' to finish the game:
    while user_choice != "quit":

        user_choice = input("Choose: write R for rock, P for paper, and S for scissors,\
            \nor if you want to finish the game write 'quit': ").lower()

        # comp_choice calls the next_choice function to determine what to choose:
        comp_choice = next_choice(results[0], previous_user_choice[0])

        # previous_user_choice rewrites the list with the current user choice:
        previous_user_choice[0] = user_choice

        if comp_choice == "r" and user_choice == "s":
            result = "You Lose"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == "r" and user_choice == "p":
            result = "You Win!"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == "s" and user_choice == "r":
            result = "You Win!"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == "s" and user_choice == "p":
            result = "You Lose"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == "p" and user_choice == "s":
            result = "You Win!"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == "p" and user_choice == "r":
            result = "You Lose"
            # result rewrites previous result:
            results[0] = result

        elif comp_choice == user_choice:
            result = "Tie"
            # result rewrites previous result:
            results[0] = result
        
        elif user_choice == "quit":
            result = None
            # result rewrites previous result to None in order to avoid
            # unwanted calculations below:
            results[0] = result
        # if the user writes something different that r, p, s, or 'quit'
        else:
            result = ""
            # result rewrites previous result to Blank in order to avoid
            # unwanted errors when the AI is making choices:
            results[0] = result

        # the following conditional statements help to keep record of
        # total wins, losses, and ties:
        if results[0] == "You Win!":
            wins += 1

        if results[0] == "You Lose":
            losses += 1

        if results[0] == "Tie":
            ties += 1

        # This one was made for the initial choice because there wasn't a
        # previous round at the beggining of the game, so it simply starts
        # with a random choice:
        if results[0] == None:
            result = random.choice(options)

        # this condition was made in order to handle mistakes when writing
        # user's input:
        if results[0] == "":
            result = "You wrote a different letter. Please write R, P, S or 'quit' to finish the game"

        # this one keeps record of the total rounds played and it prints each round report:
        if user_choice != "quit":
            rounds = (wins + losses + ties)

            print(f"ROUND: {rounds}")
            print(f"You chose: {user_choice.upper()} and the computer chose: {comp_choice.upper()}")
            print(f"RESULT: {result.upper()}")
            print()

        # also prints the cummulative results as rounds continue:
        print(f"Wins:{wins} | losses:{losses} | ties:{ties} ")

    # computes the percentage of wins for the user and the computer:
    percentage_user = (wins / (wins + losses)) * 100
    percentage_comp = 100 - percentage_user

    # prints the total of rounds played, wins, losses, ties,
    # percentage of wins for user and for computer:
    print(f"You played a total of {rounds} rounds.")
    print(f"You won {wins} times.")
    print(f"You lost {losses} times.")
    print(f"There were {ties} ties.")
    print(f"Which means that you beat the computer {percentage_user:.1f}% of the times")
    print(f"and the computer beat you {percentage_comp:.1f}% o the times.")

def next_choice(result, previous_user_choice):
    """"This function determines what is the optimal choice to make based
    on each round result and the previous user's choice.
    Parameters:
        result: The result of the round
        previous_user_choice: the previous user choice that was stored in
        the previous round
    returns: the next choice for the AI to make."""
    if result == "You Win!":
        # calls the beat_choice function to determine the next_comp_choice:
        next_comp_choice = beat_choice(previous_user_choice)

    if result == "You Lose":
        # selects the previous_user_choice as the next_comp_choice:
        next_comp_choice = previous_user_choice

    if result == "Tie":
        # calls the beat_choice function to determine the next_comp_choice:
        next_comp_choice = beat_choice(previous_user_choice)

    if result == None:
        # to handle the first round this one also calls a random choice:
        next_comp_choice = random.choice(options)
    
    if result == "":
        # to handle typos from the user, it will again restart the process
        # by choosing a random choice and from there it will continue
        # making decisions based on the previous one:
        next_comp_choice = random.choice(options)

    return next_comp_choice

def beat_choice(choice):
    """"This function helps to determine what beats what.
    Parameters:
        choice: The choice made. It can be r, p, or s.
    returns: the option that will beat the choice."""
    beat_choice = ""

    if choice == "r":
        beat_choice = "p"
    if choice == "p":
        beat_choice = "s"
    if choice == "s":
        beat_choice = "r"
    
    return beat_choice

if __name__ == "__main__":
    main()