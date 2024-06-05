import random
import os
import time
def arcade_screen():
    border = '''
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                ░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░              │
│                ██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗              │
│                ██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║              │
│                ██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║              │
│                ╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝              │
│                ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░              │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
'''
    print(border)
# Function to print ASCII art on the arcade screen
def print_arcade_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen
    print(arcade_screen)

# ASCII art for the cards
card_art = {
    'Hearts': '''
        ┌─────────┐
        │ {}      │
        │         │
        │    {}   │
        │         │
        │      {} │
        └─────────┘
    ''',
    'Diamonds': '''
        ┌─────────┐
        │ {}      │
        │   {}    │
        │         │
        │    {}   │
        │      {} │
        └─────────┘
    ''',
    'Clubs': '''
        ┌─────────┐
        │ {}      │
        │         │
        │    {}   │
        │         │
        │      {} │
        └─────────┘
    ''',
    'Spades': '''
        ┌─────────┐
        │ {}      │
        │   {}    │
        │    {}   │
        │   {}    │
        │      {} │
        └─────────┘
    '''
}

# Function to print card on the arcade screen
def print_card(card):
    print(card_art[card[1]].format(card[0], card[0], card[0], card[0], card[0]))
# Function to print message on the arcade screen
def print_message(message):
    print("\n" + message.center(50) + "\n")
# Function to create a new user account and save to a file
def create_user():
    print_message("Create a New User Account")
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")
    
    with open("user_data1.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    
    print_message("User account created successfully!")
    time.sleep(0.2)
    return username
# Function to sign in
def sign_in():
    print_message("Sign In")
    username = input("Enter your Username: ")
    
    found_username = False
    with open("user_data1.txt", "r") as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                stored_username, _ = line.strip().split(":")
                if username == stored_username:
                    found_username = True
                    break
    
    if not found_username:
        print_message("Username not found.")
        time.sleep(0.2)
        return None
    
    password = input("Enter your Password: ")
    
    with open("user_data1.txt", "r") as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    print_message("Sign-in successful!")
                    time.sleep(0.2)
                    return username
    
    print_message("Incorrect password.")
    time.sleep(0.2)
    return None

def initial_menu():
    while True:
        print("\nWelcome to the Sign-In System")
        print("1. Sign in")
        print("2. Create a new user account")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == '2':
            return create_user()
        elif choice == '1':
            username = sign_in()
            if username:
                return username
        elif choice == '3':
            print("Exiting the program.")
            quit()
        elif choice == "07":
            username = "freddie"
            game_selection_menu(username)
        else:
            print("Invalid choice. Please select a valid option.")

def main_menu(username):
    while True:
        print("\nScoreboard Options:")
        print("1. Add Score")
        print("2. Get Score")
        print("3. Display Scores")
        print("4. Play Again")
        print("5. Quit")
        print("\n")
        print("\n")
        print("\n")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            current_score = scoreboard.get_score(username)
            new_score = pot
            if new_score < current_score:
                print("\n")
                print("\n")
                print("\n")
                confirm = input("Warning: Adding this score will lower your logged score. Do you want to proceed? (yes/no): ").lower()
                if confirm not in ['yes', 'y']:
                    continue
            scoreboard.add_score(username, new_score)
            print("\n")
            print("\n")
            print("\n")
            print("\nScore added successfully!")
            print("\n")
            print("\n")
            print(f"Your current pot: £{pot}")
            print(f"Logged pot: £{scoreboard.get_score(username)}")
        elif choice == "2":
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print(f"Your current pot: £{pot}")
            print(f"Logged pot: £{scoreboard.get_score(username)}")
        elif choice == "3":
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            scoreboard.display_scores(username)
            print("\n")
            print("\n")
            print("\n") 
            print(f"Your current pot: £{pot}")
            print(f"Logged pot: £{scoreboard.get_score(username)}")
        elif choice == "4":
            play_again_menu(username)
        elif choice == "5":
            print("Goodbye!")
            quit()
        else:
            print("\n")
            print("\nInvalid choice. Please try again.")
            print("\n")

def play_game(username):
    global pot
    pot = 100
    while pot > 0:
        blackjack()
        print("\n")
        print(f"Your current pot: £{pot}")
        print(f"Logged pot: £{scoreboard.get_score(username)}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                if pot == 0:
                    pot = 100
                    
                break
            else:
                print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.")

        if play_again in ['no', 'n']:
            main_menu(username)

def play_again_menu(username):
    while True:
        print("\nPlay Again Options:")
        print("1. Stay Signed In")
        print("2. Re-Sign In")
        print("3. Quit")
        choice = input("Please select an option: ")

        if choice == '1':
            game_selection_menu(username)
        elif choice == '2':
            username = initial_menu()
            game_selection_menu(username)
        elif choice == '3':
            print("Goodbye!")
            quit()
        else:
            print("Invalid choice. Please select a valid option.")

def game_selection_menu(username):
    while True:
        print("\nGame Selection Menu:")
        print("1. Play Blackjack")
        print("2. Play Roulette")
        print("3. Play Poker")
        print("4. ~~SECRET~~")
        choice = input("Please select a game: ")

        if choice == '1':
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            play_blackjack(username)
        elif choice == '2':
            play_roulette(username)
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            #print("Russian Roulette is currently under construction.")
            game_selection_menu(username)
        elif choice == '3':
            print("\n")
            print("\n")
            print("\n")
            print("Poker is currently under construction.")
            print("\n")
            print("\n")
            print("\n")
        elif choice == '4':
            print("~~~~~~~~ YOU FOUND THE EASTER EGG! ~~~~~~~~")
            time.sleep(1.2)
            print("Welcome to the Mystery Python Game!")
            print("Try to guess the secret number.")

            secret_number = random.randint(1, 100)
            attempts = 0

            while True:
                guess = int(input("Enter your guess (between 1 and 100): "))
                attempts += 1

                if guess < secret_number:
                    print("\n")
                    print("\n")
                    print("\n")
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("\n")
                    print("\n")
                    print("\n")
                    print("Too high! Try again.")
                else:
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts!")
                    game_selection_menu(username)
                    

# Initialize deck
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Initialize pot
pot = 100

# Define functions
def deal_card(deck):
    return deck.pop()

def calculate_score(hand):
    score = sum(values[card[0]] for card in hand)
    for card in hand:
        if card[0] == 'Ace' and score > 21:
            score -= 10  # Change the value of Ace from 11 to 1
    return score

def blackjack():
    print("██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ░░░░░██╗░█████╗░░█████╗░██╗░░██╗")
    print("██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ░░░░░██║██╔══██╗██╔══██╗██║░██╔╝")
    print("██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ░░░░░██║███████║██║░░╚═╝█████═╝░")
    print("██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ██╗░░██║██╔══██║██║░░██╗██╔═██╗░")
    print("██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗")
    print("╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    # Initialize deck and shuffle
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

    # Place a bet
    global pot
    while True:
        try:
            bet = int(input(f"Your current pot: £{pot}\nPlace your bet: £"))

            if 0 < bet <= pot:
                break
            else:
                print("Invalid bet. Please bet an amount within your current pot.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric bet.")

    # Deal initial cards
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player's turn
    player_score = calculate_score(player_hand)
    while player_score < 21:
        print("\nYour hand:")
        for card in player_hand:
            print_card(card)
        print(f"Total: {player_score}")
        action = input("Do you want to 'hit' or 'stand'? (h/s): ").lower()
        if action in ['hit', 'h']:
            player_hand.append(deal_card(deck))
            player_score = calculate_score(player_hand)
        elif action in ['stand', 's']:
            break

    # Dealer's turn
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card(deck))
        dealer_score = calculate_score(dealer_hand)

    # Display final hands and result
    print("\nYour hand:")
    for card in player_hand:
        print_card(card)
    print(f"Total: {player_score}")

    print("\nDealer's hand:")
    for card in dealer_hand:
        print_card(card)
    print(f"Total: {dealer_score}")

    if player_score > 21:
        print(f"\nBust! You went over 21. You lose £{bet}.")
        pot -= bet
    elif dealer_score > 21:
        print(f"\nDealer busts! You win £{bet*2}.")
        pot += bet
    elif player_score > dealer_score:
        print(f"\nYou win £{bet*2}.")
        pot += bet
    elif player_score < dealer_score:
        print(f"\nDealer wins. You lose £{bet}.")
        pot -= bet
    else:
        print(f"\nIt's a tie! Your bet of £{bet} is returned to the pot.")

def roulette():
    print("\n")
    print("\n")
    print("\n")
    print("\n")    
    print("██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗")
    print("██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝")
    print("██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░")
    print("██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░")
    print("██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗")
    print("╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    global pot
    while True:
        try:
            bet = int(input(f"Your current pot: £{pot}\nPlace your bet: £"))
            if 0 < bet <= pot:
                break
            else:
                print("Invalid bet. Please bet an amount within your current pot.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric bet.")

    # Player chooses a number
    print("\n")
    print("\n")
    while True:
        try:
            chosen_number = int(input("Choose a number between 0 and 6: "))
            if 0 <= chosen_number <= 6:
                break
            else:
                print("Invalid choice. Please choose a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 0 and 6.")

    # Spin the roulette wheel
    winning_number = random.randint(1, 6)
    print(f"The winning number is: {winning_number}")

    if chosen_number == winning_number:
        winnings = bet * 6
        print(f"Congratulations! You win £{winnings}.")
        pot += winnings
    else:
        print(f"Sorry, you lose £{bet}.")
        pot -= bet

def play_blackjack(username):
    global pot
    while pot > 0:
        blackjack()
        print("\n")
        print(f"Your current pot: £{pot}")
        print(f"Logged pot: £{scoreboard.get_score(username)}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                if pot == 0:
                    pot = 100
                break
            else:
                print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.")

        if play_again in ['no', 'n']:
            main_menu(username)

def play_roulette(username):
    global pot
    while pot > 0:
        roulette()
        print("\n")
        print(f"Your current pot: £{pot}")
        print(f"Logged pot: £{scoreboard.get_score(username)}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                if pot == 0:
                    pot = 100
                break
            else:
                print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.")

        if play_again in ['no', 'n']:
            main_menu(username)

class Scoreboard:
    def __init__(self):
        self.scores = {}
        self.filename = "scores.txt"

    def add_score(self, player, score):
        self.scores[player] = score  # Replace the old score with the new score
        self.save_scores()

    def get_score(self, player):
        return self.scores.get(player, 0)

    def display_scores(self, current_player=None):
        if not self.scores:
            print("No scores to display.")
        else:
            print("\n")
            print("Top Five Scores:")
            sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
            for i, (player, score) in enumerate(sorted_scores[:5]):
                print(f"{i + 1}. {player}: {score}")

            if current_player and current_player not in [player for player, score in sorted_scores[:5]]:
                player_rank = sorted_scores.index((current_player, self.scores[current_player])) + 1
                print(f"\nYour Rank: {player_rank}, Your Score: {self.scores[current_player]}")

    def save_scores(self):
        with open(self.filename, "w") as file:
            for player, score in self.scores.items():
                file.write(f"{player}:{score}\n")

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    player, score = line.strip().split(":")
                    self.scores[player] = int(score)

if __name__ == "__main__":
    scoreboard = Scoreboard()
    scoreboard.load_scores()
    username = initial_menu()
    game_selection_menu(username)
