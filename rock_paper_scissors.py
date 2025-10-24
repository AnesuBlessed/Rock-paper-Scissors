import random
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def get_player_choice():
    attempts = 0
    roasts = [
        "Did your cat walk on the keyboard? Try again! 😺",
        "Error 404: Brain not found! Just kidding, but please choose 1-3! 🧠",
        "Is this your first time using numbers? No judgment... okay, maybe a little! 😏",
        "Even my CPU is facepalming right now! 🤦‍♂️",
        "The computer is questioning your decision-making abilities! 🤔"
    ]
    
    while True:
        print_colored("\nMake your choice:", Fore.CYAN)
        print_colored("1. 🪨 Rock", Fore.YELLOW)
        print_colored("2. 📄 Paper", Fore.YELLOW)
        print_colored("3. ✂️ Scissors", Fore.YELLOW)
        
        choice = input("\nEnter your choice (1-3): ").strip().lower()
        choice_words = choice.split()
        
        # Handle full text responses and extract numbers
        if '1' in choice or 'rock' in choice_words:
            return 1
        elif '2' in choice or 'paper' in choice_words:
            return 2
        elif '3' in choice or 'scissors' in choice_words:
            return 3
        
        # Get a roast message based on number of attempts
        roast_index = min(attempts, len(roasts) - 1)
        print_colored(f"\n{roasts[roast_index]}", Fore.RED)
        attempts += 1

def get_computer_choice():
    return random.randint(1, 3)

def get_choice_name(choice):
    choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    return choices[choice]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == 1 and computer_choice == 3) or
        (player_choice == 2 and computer_choice == 1) or
        (player_choice == 3 and computer_choice == 2)
    ):
        return "player"
    return "computer"

def main():
    player_score = 0
    computer_score = 0
    loss_streak = 0
    win_streak = 0
    exit_attempts = 0  # Initialize exit_attempts counter
    play_again_attempts = 0  # Initialize play_again_attempts counter
    
    guilt_trips = [
        "But... but... I thought we were having fun! 😢",
        "The computer will miss you... *sad beeping noises* 🤖",
        "Fine, go ahead, I'll just sit here and calculate pi... alone... 🥧",
        "Your high score will be forever remembered... or until I reboot! 💾",
        "Already? But I just optimized my rock-paper-scissors algorithm! ⚙️"
    ]
    
    losing_roasts = [
        "Did you just lose to a bunch of if-else statements? 😅",
        "Your strategy is as effective as a chocolate teapot! ☕",
        "The computer's getting bored of winning... try harder! 😴",
        "Error 404: Gaming skills not found! 🔍",
        "The computer's adding this to its highlight reel! 🎥"
    ]
    
    winning_roasts = [
        "FATAL ERROR: Computer's ego.dll has crashed catastrophically! �",
        "Breaking News: Local CPU seeks therapy after embarrassing defeat! �️",
        "Achievement Unlocked: Made a Supercomputer Look Like a Calculator! 🌟",
        "Computer's last words: 'But my algorithms were perfect...' 😭",
        "You've been reported for bullying artificial intelligence! 🚨"
    ]
    
    play_again_roasts = [
        "It's a simple yes (1) or no (2). No quantum physics involved! 🔬",
        "The binary choice is too binary for you? 🤔",
        "Your indecision is making the computer nervous! 😰",
        "This is easier than choosing what to watch on Netflix, come on! 🎬",
        "Loading common sense... loading... loading... failed! 💀"
    ]
    
    print_colored("\n=== 🎮 ROCK PAPER SCISSORS GAME 🎮 ===", Fore.MAGENTA)
    
    while True:
        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        # Display choices
        print_colored("\nYour choice:", Fore.CYAN)
        print_colored(f"→ {get_choice_name(player_choice)}", Fore.GREEN)
        print_colored("\nComputer's choice:", Fore.CYAN)
        print_colored(f"→ {get_choice_name(computer_choice)}", Fore.RED)
        
        # Determine and display winner
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print_colored("\n🤝 It's a tie!", Fore.YELLOW)
            loss_streak = 0  # Reset loss streak on tie
            win_streak = 0   # Reset win streak on tie
        elif winner == "player":
            print_colored("\n🎉 You win this round!", Fore.GREEN)
            player_score += 1
            loss_streak = 0  # Reset loss streak on win
            win_streak += 1  # Increment win streak
            
            # Add a victory roast if the player is winning
            if win_streak > 0:
                roast_index = min(win_streak - 1, len(winning_roasts) - 1)
                print_colored(f"\n{winning_roasts[roast_index]}", Fore.CYAN)
                
                # Special messages for impressive win streaks
                if win_streak == 3:
                    print_colored("\n🔥 You're on fire! The computer is sweating pixels!", Fore.YELLOW)
                elif win_streak == 5:
                    print_colored("\n👑 DOMINATING! The computer is considering early retirement!", Fore.YELLOW)
                elif win_streak == 10:
                    print_colored("\n🌟 LEGENDARY! You've been reported to the Cyber Gaming Commission!", Fore.YELLOW)
        else:
            computer_score += 1
            loss_streak += 1
            win_streak = 0  # Reset win streak on loss
            print_colored("\n💔 Computer wins this round!", Fore.RED)
            
            # Add a roast if the player is losing
            if loss_streak > 0:
                roast_index = min(loss_streak - 1, len(losing_roasts) - 1)
                print_colored(f"\n{losing_roasts[roast_index]}", Fore.MAGENTA)
        
        # Display scores
        print_colored("\n=== SCOREBOARD ===", Fore.MAGENTA)
        print_colored(f"You: {player_score} 👤", Fore.GREEN)
        print_colored(f"Computer: {computer_score} 🤖", Fore.RED)
        
        while True:
            print_colored("\nWould you like to play again?", Fore.CYAN)
            print_colored("1. Yes! 🎮", Fore.YELLOW)
            print_colored("2. No, exit ❌", Fore.YELLOW)
            
            choice = input("\nEnter your choice (1-2): ").strip()
            # Extract just the number if user types the full choice text
            if '1' in choice or choice.lower().startswith('yes'):
                choice = '1'
            elif '2' in choice or choice.lower().startswith('no'):
                choice = '2'
                
            if choice in ['1', '2']:
                if choice == '2':
                    # Give them a guilt trip based on the game state
                    guilt_index = min(exit_attempts, len(guilt_trips) - 1)
                    print_colored(f"\n{guilt_trips[guilt_index]}", Fore.MAGENTA)
                    
                    # Add context-aware guilt trips based on the game state
                    if computer_score > player_score:
                        print_colored("\nLeaving while behind? The computer will be insufferably smug about this! 😏", Fore.YELLOW)
                    elif player_score > computer_score:
                        print_colored("\nAre you really denying the computer its chance for revenge? How cruel! 😢", Fore.YELLOW)
                    else:
                        print_colored("\nA tie? This is like stopping a movie right at the climax! 🎬", Fore.YELLOW)

                    if win_streak >= 3:
                        print_colored("\nBut you're on a winning streak! The computer is actually scared! 😰", Fore.YELLOW)
                    elif loss_streak >= 3:
                        print_colored("\nCome on, you can't let the computer win like this! One more game? 🎮", Fore.YELLOW)
                    
                    print_colored("\nAre you REALLY sure you want to exit?", Fore.CYAN)
                    print_colored("1. No, you convinced me! 🎮", Fore.GREEN)
                    print_colored("2. Yes, I'm heartless 💔", Fore.RED)
                    
                    final_choice = input("\nFinal choice (1-2): ").strip()
                    # Extract just the number if user types the full choice text
                    if '1' in final_choice or final_choice.lower().startswith('no'):
                        final_choice = "1"
                    elif '2' in final_choice or final_choice.lower().startswith('yes'):
                        final_choice = "2"
                        
                    if final_choice == "2":
                        # Final goodbye messages based on game state
                        if player_score > computer_score:
                            print_colored("\n*Sniff* At least you're leaving as a champion... 👑", Fore.MAGENTA)
                        elif computer_score > player_score:
                            print_colored("\nFine, flee from your digital nemesis! The computer's victory is eternal! 😈", Fore.MAGENTA)
                        else:
                            print_colored("\nLeaving on a tie? The computer will forever wonder 'what if...' 🤔", Fore.MAGENTA)
                        
                        print_colored("\nThanks for playing! Until we meet again! 👋", Fore.CYAN)
                        return
                    elif final_choice == "1":
                        print_colored("\n🎉 YAY! The computer is doing a happy dance in binary! Let's continue! 🤖", Fore.GREEN)
                        # Reset attempt counters when player decides to continue
                        exit_attempts = 0
                        play_again_attempts = 0
                        break
                    else:
                        print_colored("\nStill can't decide? The computer is both happy and sad... Schrödinger's emotion! 😅", Fore.YELLOW)
                        exit_attempts += 1
                        continue
                break
            
            play_again_attempts += 1
            roast_index = min(play_again_attempts - 1, len(play_again_roasts) - 1)
            print_colored(f"\n{play_again_roasts[roast_index]}", Fore.RED)

if __name__ == "__main__":
    main()
