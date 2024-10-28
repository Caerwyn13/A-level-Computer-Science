import math
import os
import sys


def get_word() -> list:
  word = []
  temp = input("Player 1, enter your word: ").upper()

  for i in range(0, len(temp)):
    if temp[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      print("Please enter alphabetical letters next time. Exiting...")
      sys.exit()
    word.append(temp[i])

  os.system('clear')  # Clears terminal so player 2 doesn't see the word

  return word


def calculate_lives(difficulty: str, length: int) -> int:
  """
  Calculates a suitable number of lives according to difficulty
  and length of the word
  """
  match difficulty:
    case "easy":
      return math.floor(1.25 * (length + math.log(length + 1)))
    case "normal":
      return math.floor(length + math.log(length + 1))
    case "hard":
      return math.floor(0.75 * (length + math.log(length + 1)))
    case _:
      return math.floor(length + math.log(length + 1))


def update_word(guess: str, word: list, user_word: list) -> None:
  for i in range(0, len(word)):
    if guess == word[i]:
      user_word[i] = guess


def main():
  print("========== HANGMAN ==========")
  difficulty = input("Easy, Normal, or Hard?: ").lower()
  word = get_word()  # Word
  lives = calculate_lives(difficulty, len(word))  # Number of lives
  user_word = ['*' for _ in range(0, len(word))]  # Letters guessed by player 2
  guess = ""  # Current guess

  print("========== HANGMAN ==========")
  while user_word != word and lives != 0:
    temp = ""
    for i in range(0, len(word)):
      temp += user_word[i]

    print(f"WORD: {temp}\t\tGUESSES REMAINING {lives}")
    guess = input("\nGuess a letter: ").upper()
    if len(guess) == len(word):
      if list(guess) == word:
        print("\n========== Congratulations ==========")
        print(
            f"\033[1;33mYou beat the game with {lives} guesses remaining!\033[0;0m"
        )
        return 0
    elif guess in user_word:
      print("That letter has already been guessed.")
    elif guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      print("Please enter a letter.")
    else:
      update_word(guess, word, user_word)
      lives -= 1

  if user_word == word:
    print("\n========== Congratulations ==========")
    print(
        f"\033[1;33mYou beat the game with {lives} guesses remaining!\033[0;0m"
    )
    return 0

  if lives == 0:
    print("\n========== GAME OVER ==========")
    print("\033[1;31mYou failed to beat the game. Try again!\033[0;0m" +
          f"\nThe word was \033[1;36m{str(word)}\033[0;0m")
    return 1

  print("\033[1;32mHow did we get here?\033[0;0m")
  return 1


if __name__ == "__main__":
  main()
