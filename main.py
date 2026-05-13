# 10-masala:
class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    def set_rooms(self, new_rooms):
        self.__rooms = new_rooms


h1 = Hospital('Shifo', 50)
print(h1.name)
print(h1.get_rooms())
h1.set_rooms(70)
print(h1.get_rooms())
