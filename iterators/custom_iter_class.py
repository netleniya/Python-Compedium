"""
By default, custom classes are not iterable. We can’t just go around plugging our custom classes into for loops and expecting any results! This presents a problem if the class we are working with needs the ability to iterate.

To fully implement the iterator protocol, and be able to iterate over a custom class, we must define the __iter__() and __next__() methods. In most cases the two methods can do the following:

-+ The __iter__() method can include some class member initializing, but must always return the iterator object itself. Typically, this is accomplished by returning self.
-+ The __next__() method can include any number of operations but must either return the next value available or raise the StopIteration exception.
"""


class FishInventory:
    def __init__(self, fish_list):
        self.available_fish = fish_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.available_fish):
            fish_status = f"{self.available_fish[self.index]} is available"
            self.index += 1
            return fish_status
        else:
            raise StopIteration


# Create an instance of the FishInventory class and iterate over it using a for-loop
fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

for fish in fish_inventory_cls:
    print(fish)
