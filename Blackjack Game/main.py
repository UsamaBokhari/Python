import random

import clear

from art import logo


def game():
    print(logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(card):
        if sum(card) == 21 and len(sum(card)) == 2:
            return 0
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
        return sum(card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, score: {user_score}")
        print(f"computer first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user = input("Do you want to draw anoter card? 'y' or 'n': ")
            if user == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("Draw")
        elif computer_score == 0:
            print("User loses")
        elif user_score == 0:
            print("User wins")
        elif user_score > 21:
            print("User loses")
        elif computer_score > 21:
            print("Computer loses")
        elif user_score > computer_score:
            print("You win")
        else:
            print("You lose")

    compare(user_score, computer_score)


game()
again_play = input("Do you want to play again? 'y' or 'n': ")
if again_play == 'y':
    clear()
    game()