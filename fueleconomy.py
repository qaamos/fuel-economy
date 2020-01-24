# This program can be used to calculate various useful statistics about a car's
# fuel economy.

# TO DO: support for different units, error handling

# calculate volume of fuel used
def calculateVolume():

    print("\nPlease input your car's average fuel consumption"
    " (l/100km):")
    consumption = input("> ")

    print("\nPlease input the distance traveled (km): ")
    distance = input("> ")

    volume = int(consumption) / 100 * int(distance)
    print("\nThe estimated volume of fuel consumed:", volume, "liters.")
    return

# calculate maximum range possible to drive
def calculateRange():

    print("\nPlease input your car's average fuel consumption"
    " (l/100km):")
    consumption = input("> ")

    print("\nPlease input the volume of fuel available (l)")
    volume = input("> ")

    distance = int(volume) / (int(consumption) / 100)
    print("\nThe estimated maximum range:", distance, "kilometers.")

# calculate average fuel consumption
# TO DO
def calculateConsumption():
    print("consumption")

def main():

    print("\nWelcome! To begin, please choose the statistic you would like",
    "to calculate:")

    while True:

        print("\n[1] Calculate volume of fuel used\n[2] Calculate",
        "range\n[3] Calculate average fuel consumption",
        "\n[Q] Quit\n")
        mode = input(">")

        if mode == "1":
            calculateVolume()
        elif mode == "2":
            calculateRange()
        elif mode == "3":
            calculateConsumption()
        elif mode == "q" or mode == "Q":
            break
        else:
            print("\nError! Please enter a number from 1 to 3, or Q to quit.")

    return 0

main()
