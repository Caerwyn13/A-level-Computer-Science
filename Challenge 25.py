import random

suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
dealt_cards = []  # Holds dealt cards so cards aren't dealt twice


def generate_card() -> list:
    """Generates a unique card in the form [VALUE, "SUIT"]."""
    while True:
        card = [random.randint(1, 11), suits[random.randint(0, 3)]]
        if card not in dealt_cards:
            dealt_cards.append(card)
            return card


def calculate_hand_value(hand):
    """Calculates the hand value, treating Aces as 11 or 1."""
    value = sum(card[0] if card[0] != 1 else 11 for card in hand)  # Treat each Ace initially as 11
    aces = sum(1 for card in hand if card[0] == 1)

    while value > 21 and aces > 0:  # Convert Ace(s) from 11 to 1 if over 21
        value -= 10
        aces -= 1

    return value


def hit(hand):
    """Deals a new card to the specified hand."""
    hand.append(generate_card())


def display_hand(hand, hide_first_card=False):
    """Returns a string representation of the hand, optionally hiding the first card."""
    hand_display = ""
    for idx, card in enumerate(hand):
        if hide_first_card and idx == 0:
            hand_display += "[Hidden card]"
        else:
            hand_display += f" {card[0]} of {card[1]},"
    return hand_display


def main():
    balance = 100  # Starting balance for betting
    print("========== WELCOME TO BLACKJACK ==========")
    print("Dealer stands on soft 18")
    print("Your starting balance is £100\n")

    while True:
        if balance <= 0:
            print("You ran out of money. Game over!")
            break

        print(f"Current balance: £{balance}")
        try:
            bet = int(input("Place your bet: £"))
            if bet > balance or bet <= 0:
                print("Invalid bet. Please bet within your balance.")
                continue
        except ValueError:
            print("Invalid input! Bet must be a number.")
            continue

        # Generate initial hands for user and dealer
        user_hand = [generate_card(), generate_card()]
        dealer_hand = [generate_card(), generate_card()]

        # Calculate the initial values of both hands
        user_value = calculate_hand_value(user_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        print(f"\nYour hand:{display_hand(user_hand)}, with a total value of {calculate_hand_value(user_hand)}")
        print(f"Dealer's hand:{display_hand(dealer_hand, hide_first_card=True)}")

        while calculate_hand_value(user_hand) <= 21:
            print("\nWhat do you want to do? (Enter the number)")
            print("\t1. Hit")
            print("\t2. Stay")
            print("\t3. Split (only if initial cards match)")

            try:
                option = int(input("Choice: "))
                if option == 1:  # Hit
                    hit(user_hand)
                    user_value = calculate_hand_value(user_hand)
                    print(f"\nYour hand now:{display_hand(user_hand)} (Value: {user_value})")

                    if user_value > 21:
                        print("You busted! Dealer wins.")
                        balance -= bet
                        break

                elif option == 2:  # Stay
                    user_value = calculate_hand_value(user_hand)
                    dealer_value = calculate_hand_value(dealer_hand)

                    print(f"\nYou stay with a hand value of {user_value}")
                    print(f"Dealer reveals their hand:{display_hand(dealer_hand)} (Value: {dealer_value})")

                    while dealer_value < 18:
                        hit(dealer_hand)
                        dealer_value = calculate_hand_value(dealer_hand)
                        print(f"Dealer draws a card. Dealer's hand:{display_hand(dealer_hand)} (Value: {dealer_value})")

                    if dealer_value > 21:
                        print("Dealer busts! You win.")
                        balance += bet
                    elif user_value > dealer_value:
                        print("You win!")
                        balance += bet
                    elif user_value < dealer_value:
                        print("Dealer wins!")
                        balance -= bet
                    else:
                        print("It's a tie! Bet returned.")

                    break

                elif option == 3:  # Split
                    if user_hand[0][0] == user_hand[1][0]:
                        split_hand1 = [user_hand[0], generate_card()]
                        split_hand2 = [user_hand[1], generate_card()]

                        # Process split hands separately
                        for i, split_hand in enumerate([split_hand1, split_hand2], start=1):
                            print(f"\n--- Playing hand {i} ---")
                            while calculate_hand_value(split_hand) <= 21:
                                print(f"Hand {i}: {display_hand(split_hand)} (Value: {calculate_hand_value(split_hand)})")
                                print("1. Hit\n2. Stay")

                                split_option = int(input("Choice: "))
                                if split_option == 1:
                                    hit(split_hand)
                                    if calculate_hand_value(split_hand) > 21:
                                        print(f"Hand {i} busted!")
                                        balance -= bet // 2
                                        break
                                elif split_option == 2:
                                    break

                        # Evaluate split hands against dealer
                        for i, split_hand in enumerate([split_hand1, split_hand2], start=1):
                            split_value = calculate_hand_value(split_hand)
                            if split_value <= 21:
                                print(f"\nEvaluating hand {i} against dealer")
                                if split_value > dealer_value or dealer_value > 21:
                                    print(f"Hand {i} wins!")
                                    balance += bet // 2
                                else:
                                    print(f"Hand {i} loses!")
                                    balance -= bet // 2
                    else:
                        print("You cannot split these cards.")

                else:
                    print("Invalid option.")

            except ValueError:
                print("Invalid input. Please choose a valid option.")

        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print(f"You leave the casino with £{balance}. Thanks for playing!")
            break


if __name__ == "__main__":
    main()
