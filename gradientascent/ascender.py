from collections import namedtuple, abc

Coordinate = namedtuple('Coordinate', 'x, y')

# TODO: Make this DirectAscender and create abstract base class for Ascender
class Ascender(abc.Iterator):

    def __init__(self, array, start_coordinate):
        self.array = array
        self._shape = self.array.shape
        self._current_coordinate = start_coordinate
        self.index = 0

    @property
    def current_coordinate(self):
        return self._current_coordinate

    @current_coordinate.setter
    def current_coordinate(self, new_coordinate):
        assert isinstance(new_coordinate, Coordinate), f'New Coordinate {new_coordinate} is not a Coordinate type.'
        h, w = self._shape
        assert 0 <= new_coordinate.x and new_coordinate.x < w, f'New coordinate x position ({new_coordinate.x}) not in grid.'
        assert 0 <= new_coordinate.y and new_coordinate.y < h, f'New coordinate y position ({new_coordinate.y}) not in grid.'
        self._current_coordinate = new_coordinate

    def reset_start_coordinate(self, new_start_coordinate):
        self.index = 0
        self.current_coordinate = new_start_coordinate

    def __str__(self):
        return f'Ascender(grid_shape={self.array.shape}, current_position={self.current_coordinate})'

    def _get_height_of_coordinate(self, coordinate: Coordinate):
        return self.array[coordinate.y][coordinate.x]

    def _get_bordering_coordinates(self, current_coordinate: Coordinate):
        h, w = self.array.shape
        bordering_coordinates = []
        if current_coordinate.y - 1 >= 0:
            bordering_coordinates.append(Coordinate(current_coordinate.x, current_coordinate.y - 1))
        if current_coordinate.y + 1 < h:
            bordering_coordinates.append(Coordinate(current_coordinate.x, current_coordinate.y + 1))
        if current_coordinate.x - 1 >= 0:
            bordering_coordinates.append(Coordinate(current_coordinate.x - 1, current_coordinate.y))
        if current_coordinate.x + 1 < w:
            bordering_coordinates.append(Coordinate(current_coordinate.x + 1, current_coordinate.y))
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

    def __iter__(self):
        return self

    def __next__(self):
        if not self.index:
            # Make sure initial coordinate is yielded once
            self.index += 1
            return self.current_coordinate
        next_coord = self._calculate_steepest_ascent_coordinate(self.current_coordinate)
        if self.current_coordinate != next_coord:
            self.current_coordinate = next_coord
            self.index += 1
            return next_coord
        else:
            raise StopIteration


if __name__ == '__main__':
    import numpy as np 
    from gradientascent.utils import generate_gaussian_array

    a = generate_gaussian_array(20, 20, 0.05)
    g = Ascender(a, Coordinate(0, 0))
    g.reset_start_coordinate(Coordinate(18,15))

    for c in g:
        print(c)

    g.reset_start_coordinate(Coordinate(0,0))

    for c in g:
        print(c)





