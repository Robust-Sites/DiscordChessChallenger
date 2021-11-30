class Piece:
    def __init__(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
Knight = Piece("Knight", (1,6))
print(Knight.coordinate)