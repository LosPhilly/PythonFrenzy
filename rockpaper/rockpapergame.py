import random
 
def rock_paper_scissors():
    player_wins = 0
    computer_wins = 0
    ties = 0

    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

    paper = """
        _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

    scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """
    while True:
        # game logic goes here
        player_move = input("Enter your move (rock, paper, scissors): ")
        computer_move = random.choice(["rock", "paper", "scissors"])

        if player_move == computer_move:
            ties += 1
            print("Tie!")
        elif (player_move == "rock" and computer_move == "scissors") or (player_move == "paper" and computer_move == "rock") or (player_move == "scissors" and computer_move == "paper"):
            player_wins += 1
            print("You win!")
            if player_move == "scissors":
                print(scissors)
            if player_move == "paper":
                print(paper)
            
        else:
            computer_wins += 1
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() == "no":
            print("Thanks for playing! Final score: You:", player_wins, "Computer:", computer_wins, "Ties:", ties)
            break

rock_paper_scissors()
