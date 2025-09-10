import time
import pyfiglet
from random import randint
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
from alive_progress import alive_bar

# Initialize Colorama
init(autoreset=True)

console = Console()

# Banner
banner = pyfiglet.figlet_format("Guess Game")
print(Fore.CYAN + banner)

player_score = 0
computer_score = 0
console.print("[bold green]Welcome to Number Guessing Game 🎯[/bold green]")
while True:
    attempts = 5
    computer = randint(1, 20)

    
    print(Fore.YELLOW + "Guess a number between 1 and 20")
    print(Fore.MAGENTA + "You have 5 attempts!\n")

    # Progress Bar Animation
    with alive_bar(3, title="Thinking...") as bar:
        for i in range(3):
            time.sleep(0.5)
            bar()

    # Game Loop
    for i in range(5):
        try:
            player = int(input(Fore.CYAN + "Enter your guess: "))
        except ValueError:
            print(Fore.RED + "❌ Invalid input! Please enter a number.")
            continue

        # Out of range input
        if player < 1 or player > 20:
            print(Fore.RED + "❌ Only numbers between 1 and 20 are allowed!")
            continue

        if player == computer:
            print(Fore.GREEN + "🎊 Congratulations! You guessed the correct number!")
            player_score += 1
            break
        else:
            if player > computer:
                print(Fore.RED + "📈 Too High! Try again.")
            else:
                print(Fore.BLUE + "📉 Too Low! Try again.")
            attempts -= 1
            print(Fore.YELLOW + f"Attempts left: {attempts}\n")

        if attempts == 0:
            print(Fore.RED + "❌ No attempts left!")
            computer_score += 1
            print(Fore.MAGENTA + f"The number was: {computer}")

    # Show Scores with Rich Table
    table = Table(title="Score Board")
    table.add_column("Player", style="cyan")
    table.add_column("Score", style="green")
    table.add_row("You", str(player_score))
    table.add_row("Computer", str(computer_score))
    console.print(table)

    # Play Again?
    again = input(Fore.CYAN + "Do you want to play again? (y/n): ")
    if again.lower() != "y":
        console.print("[bold yellow]Thanks for playing! 🙏 Goodbye![/bold yellow]")
        break