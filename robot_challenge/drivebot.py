"""
Codecademy Python Coding challenge. Create a robot and define its behaviour using a combination of class variables, instance variables, and class methods.
-- Class variables take the form ClassName.variable_name, and can be changed for every instance (object) of the class
-- Instance variables take the form self.variable_name, and can only be accessed by the object itself
-- Class methods can manipulate and change values of variables 

Task: Create a bunch of robots using Classes
"""


class DriveBot:

    all_disabled = False
    # latitude = longitude = -9999
    robot_count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def __repr__(self):
        return f"Bot{self.id:>2}. Speed:{self.motor_speed:0>2}, Direction:{self.direction:>03}, Range: {self.sensor_range:>1}, Coords: ({self.latitude:>6}, {self.longitude})"

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def set_coords(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
