from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'x, y')
Gradient = namedtuple('Gradient', 'cardinal, magnitude')


class Grid:

    def __init__(self, array):
        self.array = array
        self.current_position = None

    def _get_height_of_coordinate(self, coordinate: Coordinate):
        return self.array[coordinate.y][coordinate.x]

    def _get_bordering_coordinates(self, current_coordinate: Coordinate):
        h, w = self.array.shape
        bordering_coordinates = []
        if current_coordinate.y - 1 >= 0:
            bordering_coordinates.append(Coordinate(current_coordinate.y - 1, current_coordinate.x))
        if current_coordinate.y + 1 < h:
            bordering_coordinates.append(Coordinate(current_coordinate.y + 1, current_coordinate.x))
        if current_coordinate.x - 1 >= 0:
            bordering_coordinates.append(Coordinate(current_coordinate.y, current_coordinate.x - 1))
        if current_coordinate.x + 1 < w:
            bordering_coordinates.append(Coordinate(current_coordinate.y, current_coordinate.x + 1))
        return bordering_coordinates

    def _calculate_steepest_ascent_coordinate(self, current_coordinate: Coordinate):
        current_height = self._get_height_of_coordinate(current_coordinate)
        bordering_coordinates = self._get_bordering_coordinates(current_coordinate)
        max_height = current_height
        steepest_ascent_coordinate = current_coordinate
        for coord in bordering_coordinates:
            coord_height = self._get_height_of_coordinate(coord)
            if coord_height > max_height:
                max_height = coord_height
                steepest_ascent_coordinate = coord
        return steepest_ascent_coordinate



