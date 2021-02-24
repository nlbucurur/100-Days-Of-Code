"""Blackjack game."""

import random
# from replit import clear
from art import logo

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

end_game = False


def deal_card():
    """Deal Card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = []
    card.append(random.choice(cards))
    return card


def calculate_score(card_list):
    """Calculate score."""
    score = sum(card_list)
    if 11 in card_list and 10 in card_list and len(card_list) == 2:
        return 0
    elif 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
        return score
    else:
        return score


def finish_proof(user_cards, user_score, computer_cards, computer_score):
    """Proof."""
    if (len(user_cards) == 2 and user_score == 0) or user_score > 21:
        end_game = True
        return end_game
    elif (len(computer_cards) == 2 and computer_score == 0) or computer_score > 21:
        end_game = True
        return end_game
    else:
        end_game = False
        return end_game


def compare(user_score, computer_score):
    """Compare scores."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


want_game = input("Dou you want to play blackjack. Type 'y' or 'n'. ")

if want_game == 'y':
    #clear()
    while not end_game:
        print(logo)

        user_cards = []
        computer_cards = []

        for n in range(2):
            user_cards += deal_card()
            computer_cards += deal_card()

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards {user_cards}, current score: {user_score}")
        # print(computer_cards)
        # if user_score == 0 or computer_score == 0:
        #  compare(user_score, computer_score)
        #  end_game = True

        print(f"computer's first card: {computer_cards[0]}")

        another = True
        while another:
            if user_score != 0 and computer_score != 0:
                want_other_card = input("Do you want to draw another card? Type 'y' or 'n'. ")

                if want_other_card == "y":
                    new_user_cards = user_cards + deal_card()
                    user_score = calculate_score(new_user_cards)
                    print(new_user_cards)
                    print(user_score)
                    if finish_proof(new_user_cards, user_score, computer_cards, computer_score):
                        another = False
                        compare(user_score, computer_score)
                        end_game = True
                        user_cards = new_user_cards
                    elif want_other_card == 'n':
                        another = False
                else:
                    another = False

        compu_another = True
        while compu_another:
            if 0 < computer_score < 17 and 0 < user_score <= 21:
                new_computer_cards = computer_cards + deal_card()
                new_computer_score = calculate_score(new_computer_cards)

                computer_cards = new_computer_cards
                computer_score = new_computer_score
            else:
                compu_another = False
        print(f"\nYour final hand: {user_cards}, final score: {user_score}.")
        print(f"Computer's final hand {computer_cards}, final score: {computer_score}.")
        print(compare(user_score, computer_score))

        next = input("Do you want to restart the game? Type 'y' or 'n': ")

        #if next == 'y':
            #clear()
        if next == 'n':
            end_game = True
else:
    print("Goodbye.")
