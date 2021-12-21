class CannonUnity:
    def __init__(self, cordinates):
        coord_x = cordinates[0]
        coord_y = cordinates[1]

        self.coordinates = [coord_x, coord_y]
        self.bridge = coord_x
        self.rivers_in_range = []

        if coord_y == 0:
            self.rivers_in_range = [1]
        elif coord_y in [1, 2, 3]:
            self.rivers_in_range = [coord_y, coord_y + 1]
        else:
            self.rivers_in_range = [4]

    def get_bridge(self):
        return self.bridge

    def get_rivers_in_range(self):
        return self.rivers_in_range

    def get_coordinates(self):
        return self.coordinates
