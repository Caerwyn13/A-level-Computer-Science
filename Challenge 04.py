def calculate(unknown):
    match unknown:
        case "distance":
            try:
                speed = float(input("Enter the speed in m/s: "))
                time = float(input("Enter the time in seconds: "))
            except ValueError:
                print(
                    "Unexpected or misspelled input. Please try again. Ensure "
                    + "your input is a strictly numerical value")
                return 1

            if speed < 0 or time < 0:
                print(
                    "Speed and time must both be positive. Double check your numbers"
                )
                return 1
            else:
                print(f"Answer: {speed * time}m")
                return 0

        case "speed":
            try:
                distance = float(input("Enter the distance in metres: "))
                time = float(input("Enter the time in seconds: "))
            except ValueError:
                print(
                    "Unexpected or misspelled input. Please try again. Ensure "
                    + "your input is a strictly numerical value")
                return 1

            if time < 0:
                print("Time must be positive. Double check your numbers")
                return 1
            else:
                print(f"Answer: {distance / time}m/s")
                return 0

        case "time":
            try:
                speed = float(input("Enter the speed in m/s: "))
                distance = float(input("Enter the distance in metres: "))
            except ValueError:
                print(
                    "Unexpected or misspelled input. Please try again. Ensure "
                    + "your input is a strictly numerical value")
                return 1

            if speed == 0:
                print("Speed cannot be 0. Double check your numbers")
            elif speed < 0:
                print("Speed must be positive. Double check your numbers")
                return 1
            else:
                print(f"Answer: {abs(distance / speed)}s")
                return 0

        case _:
            print("Unexpected or misspelled input. Please try again.")
            return 1


def main():
    result = 1

    while result == 1:
        unknown = input("Enter the unknown: ").lower().strip()
        result = calculate(unknown)


if __name__ == "__main__":
    main()
