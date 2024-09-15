import random

suits = ["Ace", "Spades", "Hearts", "Clubs"]
dealt_cards = []  # Holds dealt cards so cards aren't dealt twice


def GenerateCard() -> list:
  """
  Returns a list in the form[VALUE, "SUIT"]
  """
  temp = []  # Temporary to check if card has been dealt already
  card = []
  
  value = random.randint(1, 11)
  suit = random.randint(0, 3)
  temp.append(value)
  temp.append(suits[suit])

  if temp not in dealt_cards:
    card.append(value)
    dealt_cards.append(value)
    card.append(suits[suit])
    dealt_cards.append(suits[suit])
    return card

  GenerateCard()

def Hit(user_cards):
  print("Hit")

def Stay(user_cards):
  print("Stay")

def Split(user_cards):
  print("Split")
  
def main():
  user_cards = []    # Cards of the user
  dealer_cards = []  # Cards of the dealer
  print("========== BLACKJACK ==========")

  user_cards.append(GenerateCard())    # Gives the user two cards
  user_cards.append(GenerateCard())
  user_value = user_cards[0][0] + user_cards[1][0]  # Value of user's hand
  
  dealer_cards.append(GenerateCard())  # Gives the dealer two cards
  dealer_cards.append(GenerateCard())
  dealer_value = dealer_cards[0][0] + dealer_cards[1][0]  # Value of dealer's hand

  while user_value <= 21 and dealer_value <= 21:
    print(f"Your cards are {user_cards}, with a value of {user_value}")
    print(f"The dealer has {dealer_cards}, with a value of {dealer_value}")
  
    print("What do you want to do? (Enter the number)")
    print("\t1. Hit")
    print("\t2. Stay")
    print("\t3. Split")

    try:
      option = int(input("Choice: "))
      match option:
        case 1:
          Hit(user_cards)
        case 2:
          Stay(user_cards)
        case 3:
          if user_cards[0][0] == user_cards[1][0]:
            Split(user_cards)
          else: 
            print("You cannot split with these cards")
        case _:
          print("Get outta my casino!")
          return 1
    except ValueError:
      print("Get outta my casino!")
      return 1


main()