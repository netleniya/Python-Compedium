"""
Using the DriveBot class, generate N drones scattered across randomly generated coordinates centered around the Greater Toronto Area.

The don't do much apart from reporting their starting conditions (speed, direction, range, coordinates).
Changed the coordinates from class variables to instance variables 
"""

from drivebot import DriveBot
import random

num_bots = random.randint(1, 50)

coords = [(round(random.uniform(43.17, 44.0), 3), round(random.uniform(-80.0, -78.78), 3))
          for _ in range(num_bots)]

bots = []
for i in range(len(coords)):
    spped, direction, range = (random.randint(
        1, 25), random.randint(0, 360), random.randint(10, 15))
    bot = DriveBot(spped, direction, range)

    bot.latitude = coords[i][0]
    bot.longitude = coords[i][1]
    bots.append(bot)


for drone in bots:
    print(drone)
