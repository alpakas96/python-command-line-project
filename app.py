import random

cards = []

def add_card():
    front = input("Enter the front of the card: ")
    back = input("Enter the back of the card: ")
    card = {
        "front": front,
        "back": back,
        "correct_attempts": 0,
        "incorrect_attempts": 0
    }
    cards.append(card)

def start_training_session():
    num_cards = int(input("Enter the number of cards you'd like to review: "))
    for i in range(num_cards):
        card = random.choice(cards)
        print("Front:", card["front"])
        user_answer = input("Back: ")
        if user_answer == card["back"]:
            print("Correct!")
            card["correct_attempts"] += 1
        else:
            print("Incorrect.")
            card["incorrect_attempts"] += 1

def main_loop():
    print("Welcome to the flashcard app!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a card")
        print("2. Start a training session")
        print("3. Quit")
        choice = input("> ")
        if choice == "1":
            add_card()
        elif choice == "2":
            start_training_session()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_loop()
