import math
import random


def get_code(n: int) -> list:
  """
  Generates an n digit code
  """
  code = []
  for _ in range(0, n):
    code.append(str(random.randint(0, 9)))

  return code


def record_guess(new_guess, length) -> str:
  """
  Records guess by user
  """
  guess_list = []

  for i in range(0, length):
    guess_list.append(new_guess[i])

  return new_guess


def update_guess(user_code, guess, code, length) -> None:
  """
  Updates guess
  """
  for i in range(0, length):
    if guess[i] == code[i]:
      user_code[i] = guess[i]


def main() -> int:
  code = []  # Code for user to guess
  current_guess = []  # User's current guess

  code_length = int(input("How many digits do you want to guess? "))
  code = get_code(code_length)  # Generate n-digit code
  user_code = ['*' for _ in range(0, code_length)]  # Code guessed by user

  # Number of guesses
  count = math.ceil(code_length * math.log10(code_length + 1))

  while user_code != code and count != 0:
    temp = ""
    for i in range(0, code_length):
      temp += user_code[i]

    print(f"GUESS: {temp}\nGUESSES REMAINING: {count}\n\n")
    new_guess = input("Enter your guess: ")
    if len(new_guess) == code_length:
      current_guess = record_guess(new_guess, code_length)
      count -= 1
      update_guess(user_code, current_guess, code, code_length)
    else:
      print("Error. Please type your guess in full. In this case, " +
            f"type {code_length} digits.")

  if user_code == code:
    temp = ""
    for i in range(0, code_length):
      temp += code[i]
    print("\n========== Congratulations ==========")
    print(
        f"\033[1;33mYou beat the game with {count} guesses remaining!\033[0;0m"
        + f"\nThe code was \033[1;36m{temp}\033[0;0m")
    return 0

  if count == 0:
    print("\n========== GAME OVER ==========")
    print("\033[1;31mYou failed to beat the game. Try again!\033[0;0m \n")
    return 1

  print("\033[1;32mHow did we get here?\033[0;0m")
  return 1


if __name__ == "__main__":
  main()
