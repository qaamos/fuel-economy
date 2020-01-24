# This program can be used to calculate various useful statistics about a car's
# fuel economy.

# TO DO: support for different units, error handling

# calculate volume of fuel used
def calculateVolume():

    print("\nPlease input your car's average fuel consumption"
    " (l/100km):")
    consumption = input(">")

    print("\nPlease input the distance traveled (km): ")
    distance = input(">")

    volume = int(consumption) / 100 * int(distance)
    print("\nEstimated volume of fuel consumed: " + str(volume) + "l")
    return

# calculate maximum range possible to drive
def calculateRange():

    print("\nPlease input your car's average fuel consumption"
    " (l/100km):")
    consumption = input(">")

    print("\nPlease input the volume of fuel available (l)")
    volume = input(">")

    distance = int(volume) / (int(consumption) / 100)
    print("\nEstimated maximum range: " + str(distance) + "km")

# calculate average fuel consumption
# TO DO
def calculateConsumption():
    print("\nPlease input the volume of fuel consumed (l): ")
    volume = input(">")

    print("\nPlease input the distance driven (km): ")
    distance = input(">")

    consumption = int(volume) / int(distance) * 100
    print("\nEstimated fuel consumption: " + str(consumption) + "l/100km")

def main():

    print("\nWelcome! To begin, please choose the statistic you would like",
    "to calculate:")

    while True:

        print("\n[1] Calculate average fuel consumption\n[2] Calculate",
        "range\n[3] Calculate volume of fuel used",
        "\n[Q] Quit\n")
        mode = input(">")

        if mode == "1":
            calculateConsumption()
        elif mode == "2":
            calculateRange()
        elif mode == "3":
            calculateVolume()
        elif mode == "q" or mode == "Q":
            break
        else:
            print("\nError! Please enter a number from 1 to 3, or Q to quit.")

    return 0

main()
