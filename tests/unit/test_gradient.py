from numpy.testing import assert_array_equal
import pytest
from gradientascent.grid import Grid
                                     
import test_data as data


class TestGradient:
    
    @pytest.mark.parametrize(*data.test_get_bordering_coordinates_success())
    def test_get_bordering_coordinates_success(self, array, current_coordinate, expected_result):
        # Arrange
        grid = Grid(array)

        # Act
        bordering_coordinates = grid._get_bordering_coordinates(current_coordinate)

        # Assert
        assert set(bordering_coordinates) == set(expected_result)

    @pytest.mark.parametrize(*data.test_calculate_steepest_ascent_coordinate_success())
    def test_calculate_steepest_ascent_coordinate_success(self, array, current_coordinate, expected_result):
        # Arrange
        grid = Grid(array)

        # Act
        steepest_ascent_coordinate = grid._calculate_steepest_ascent_coordinate(current_coordinate)

        # Assert
        assert steepest_ascent_coordinate == expected_result

