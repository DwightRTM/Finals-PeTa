import random

def rock_paper_scissors():
    moves = ["rock", "paper", "scissors"]
    player_moves = [random.choice(moves) for _ in range(2)]
    bot_moves = [random.choice(moves) for _ in range(2)]

    print("Your moves:", player_moves)
    print("Bot moves:", bot_moves)

    # Adding dotted animation for Rock-Paper-Scissors (of course from our friendly neighborhood Chatgpt)
    for _ in range(1):
        print("""
            Rock:
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            -.__(___)

            Paper:
                _______
            ---'    ____)__
                    ______)
                    _______)
                    _______)
            ---.__________)

            Scissors:
                _______
            ---'   ____)__
                    ______)
                __________)
                (____)
            ---__(___)
            """)
    print()

    print("Minus One!")
    print(" Choose one of your moves to keep: ")
    while True:
        try:
            chosen_move = input("Enter 1 for the first move or 2 for the second move: ")
            if chosen_move in ["1", "2"]:
                player_move = player_moves[int(chosen_move) - 1]
                break
            else:
                 print("Invalid input. Please try again.")
        except (KeyboardInterrupt, NameError, ValueError):
            print("Error: Invalid Input. Please enter 1 or 2.")

    bot_move = random.choice(bot_moves)
    print(f"You chose {player_move}, Bot chose {bot_move}.")

    if player_move == bot_move:
        return "tie"
    elif (
        (player_move == "rock" and bot_move == "scissors") or
        (player_move == "paper" and bot_move == "rock") or
        (player_move == "scissors" and bot_move == "paper")):
        return "player"
    else:
        return "bot"
    
def russian_roulette():
    chamber = ["empty", "empty", "empty", "empty", "empty", "bullet"]
    random.shuffle(chamber)
    print("Spinning the revolver...")

    for i in range(1):
        print(r"""
                                    ______,________________________
                _______           /   ________________           `\
                |       |_________|  |                /       |
                | .---. '---------'  |               |-------------'
                | |   |               |_______________\
                | |   |              / .---. .---. .---.
                `.|   |             | |   | |   | |   |
                `---'             `-|   |-|   |-|   |
                                    |___| |___| |___|
                                    '---' '---' '---'
        """)
    print()

    return chamber[0] == "bullet"

def main_game():
    player_lives = 1
    bot_lives = 1
    round_number = 1

    while player_lives > 0 and bot_lives > 0:
        print(f"\n=== Round {round_number} ===")
        print(f"Your Lives: {player_lives}, Bot Lives: {bot_lives}")

        winner = rock_paper_scissors()

        if winner == "tie":
                print("It's a tie! No one takes a shot this round.")
        elif winner == "player":
            print("You won! Bot takes the revolver.")
            if russian_roulette():
                print("Bang! The bot loses a life.")
                bot_lives -= 1
            else:
                    print("Click. The bot is safe this round.")
        else:
            print("You lost! You take the revolver.")
            while True:
                try:
                    choice = input("Do you shoot yourself (y/n)? ").lower()
                    if choice not in ["y", "n"]:
                        print("Invalid choice. Please enter 'y' or 'n'.")
                        continue

                    if choice == "y":
                        if russian_roulette():
                            print("Bang! You lose a life.")
                            player_lives -= 1
                        else:
                            print("Click. You're safe! You gain a reward.")
                            if player_lives == 1:
                                player_lives += 1
                                print("Reward: Extra life gained!")
                    else:
                        print("You chose to fire at the bot.")
                        if russian_roulette():
                            print("Bang! The bot loses a life.")
                            bot_lives -= 1
                        else:
                            print("Click. The bot is safe this round.")
                    break
                except (KeyboardInterrupt, NameError, ValueError):
                        print("Error: Invalid input. Please try again.")
        
        if round_number % 6 == 0:
            print("revolver reset after six rounds")
        
        # Ask the player if they want to exit the game
        while True:
            try:
                exit_choice = input("Do you want to exit the game? (y/n): ").lower()
                if exit_choice == "y":
                    print("You chose to exit the game. Goodbye!")
                    return
                elif exit_choice == "n":
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
            except (KeyboardInterrupt, NameError, ValueError):
                print("Error: Invalid input. Please try again.")

        round_number += 1

        print(" ====Game Over!====")
        if player_lives > 0:
            print("===============================\n")
            print("===Congratulations! You won.===")
            print("===============================\n")
        else:
            print("====================================\n")
            print("You lost. womp womp. Better luck next time.")
            print("====================================\n")
    
# Start the game    
main_game()    
