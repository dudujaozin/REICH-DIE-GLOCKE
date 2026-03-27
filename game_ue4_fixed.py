import math

class Location:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def set_location(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_location(self):
        return (self.x, self.y, self.z)

    def distance(self, other_location):
        return math.sqrt((self.x - other_location.x) ** 2 + 
                         (self.y - other_location.y) ** 2 + 
                         (self.z - other_location.z) ** 2)


class Antigravity:
    def __init__(self, max_float_height):
        self.max_float_height = max_float_height
        self.is_float = False

    def activate_float(self):
        self.is_float = True

    def deactivate_float(self):
        self.is_float = False

    def is_floating(self):
        return self.is_float


class GameObject:
    def __init__(self, name, location):
        self.name = name
        self.location = Location(*location)
        self.antigravity = Antigravity(max_float_height=10)  # You can change max height if needed

    def move_to(self, new_location):
        self.location.set_location(*new_location)

    def update(self):
        if self.antigravity.is_floating():
            print(f"{self.name} is floating at height {self.location.z}")
        else:
            print(f"{self.name} is at location {self.location.get_location()}")


if __name__ == '__main__':
    player = GameObject("Player1", (0, 0, 0))
    player.antigravity.activate_float()  # Activate antigravity effect
    player.move_to((10, 5, 8))  # Move player to a new location
    player.update()  # Update and display current state of Player1
