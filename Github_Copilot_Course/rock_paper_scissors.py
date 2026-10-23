"""A simple graphical Rock Paper Scissors game."""
import tkinter as tk
import random


def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def main():
    """Create the game window and run the Rock Paper Scissors game."""
    player_score = 0
    computer_score = 0
    tie_score = 0

    window = tk.Tk()
    window.title("Rock Paper Scissors")
    window.geometry("400x300")

    title_label = tk.Label(
        window, text="Choose your move", font=("Arial", 18, "bold")
    )
    title_label.pack(pady=20)

    result_label = tk.Label(window, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    score_label = tk.Label(
        window,
        text="Scoreboard\nPlayer wins: 0  |  Computer wins: 0  |  Ties: 0",
    )
    score_label.pack(pady=10)

    def play_round(player_choice):
        """Play one round and update the result and score displays."""
        nonlocal player_score, computer_score, tie_score

        computer_choice = get_computer_choice()

        if player_choice == computer_choice:
            result = "It's a tie!"
            tie_score += 1
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors')
            or (player_choice == 'paper' and computer_choice == 'rock')
            or (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            result = "You win this round!"
            player_score += 1
        else:
            result = "Computer wins this round!"
            computer_score += 1

        result_label.config(
            text=f"You chose {player_choice}. Computer chose {computer_choice}.\n"
            f"{result}"
        )

        score_label.config(
            text=(
                "Scoreboard\n"
                f"Player wins: {player_score}  |  "
                f"Computer wins: {computer_score}  |  Ties: {tie_score}"
            )
        )

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    for choice in ['rock', 'paper', 'scissors']:
        tk.Button(
            button_frame,
            text=choice.title(),
            width=10,
            command=lambda selected=choice: play_round(selected),
        ).pack(side=tk.LEFT, padx=5)

    tk.Button(window, text="Quit", width=10,
              command=window.destroy).pack(pady=15)

    window.mainloop()


main()
