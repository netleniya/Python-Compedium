"""
Using the DriveBot class, generate N drones scattered across randomly generated coordinates centered around the Greater Toronto Area.

The don't do much apart from reporting their starting conditions (speed, direction, range, coordinates).
Changed the coordinates from class variables to instance variables
"""


from drivebot import DriveBot
import random


def main() -> None:
    num_bots = random.randint(1, 50)

    coords = [
        (round(random.uniform(43.17, 44.0), 3), round(random.uniform(-80.0, -78.78), 3))
        for _ in range(num_bots)
    ]

    bots = []
    for coord in coords:
        speed, direction, dist = (
            random.randint(1, 25),
            random.randint(0, 360),
            random.randint(10, 15),
        )
        bot = DriveBot(speed, direction, dist)

        bot.latitude = coord[0]
        bot.longitude = coord[1]
        bots.append(bot)

    for drone in bots:
        print(drone)


if __name__ == "__main__":
    main()
