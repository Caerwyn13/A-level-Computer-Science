import csv
import time


def create_results() -> None:
    print("\n===== Add a Result =====")
    repeat = 1  # Allows for multiple results to be added in a row

    while repeat == 1:
        # Get match data
        home = input("Enter the name of the home team: ").lower()
        home_score = int(input("Enter their score: "))
        away = input("Enter the name of the away team: ").lower()
        away_score = int(input("Enter their score: "))

        # Opens the file using "scores_file" as reference variable
        with open("Challenge 24/scores.csv", 'a', newline='') as scores_file:
            # Defines where and what to write, as well as how to separate items
            writer = csv.writer(scores_file, delimiter=',')
            writer.writerow([home, home_score, away, away_score])

        # Ask if another result is to be added
        temp_option = input(
            "Would you like to add another result? (y/n): ").lower()
        if temp_option == "y":
            repeat = 1
            print("\n")
        elif temp_option == "n":
            repeat = 0
        else:
            print(f"Unexpected input '{temp_option}', terminating program.")
            repeat = 0


def search_results() -> None:
    print("\n===== Search Results =====")
    home = input(
        "Enter the name of the home team: ").lower()  # Gets home team name

    # Opens file
    with open(r"Challenge 24/scores.csv", 'r') as scores_file:
        print("\n")
        reader = csv.reader(scores_file)  # Reads from source file
        count = 0  # Number of matches
        for row in reader:  # Loops through rows in CSV file
            if row[0] == home:  # If home matches home in file Print data
                count += 1  # And increment count
                print(f"Game number {count}: ")
                print(f"\tHome team: {row[0].title()}")
                print(f"\tAway team: {row[2].title()}")
                print(f"\tScore: {row[1]}-{row[3]}\n")

        # If no matches found
        if count == 0:
            print(
                f"No games found where {home} is the home team. Please try again"
            )


def main():
    option = 0
    print(
        "==================== Welcome to the Results Table ===================="
    )
    print("What would you like to do?")
    time.sleep(0.5)
    print("\tOption 1. Add a result")
    time.sleep(0.5)
    print("\tOption 2. Search for a result\n")
    time.sleep(0.5)

    try:
        option = int(input("Number of the option you want: "))
    except ValueError:
        print(
            "Please enter a number. In this case either '1' or '2'. Exiting Program..."
        )

    if option == 1:
        create_results()
    elif option == 2:
        search_results()
    else:
        print("Unexpected input. Ensure your input is either '1' or '2'. " +
              "Exiting Program...")


if __name__ == "__main__":
    main()
