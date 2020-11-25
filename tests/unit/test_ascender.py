from numpy.testing import assert_array_equal
import pytest
from gradientascent.ascender import Ascender
                                     
import test_data as data


class TestAscender:
    
    @pytest.mark.parametrize(*data.test_get_bordering_coordinates_success())
    def test_get_bordering_coordinates_success(self, array, current_coordinate, expected_result):
        # Arrange
        ascender = Ascender(array, current_coordinate)

        # Act
        bordering_coordinates = ascender._get_bordering_coordinates(current_coordinate)

        # Assert
        assert set(bordering_coordinates) == set(expected_result)

    @pytest.mark.parametrize(*data.test_calculate_steepest_ascent_coordinate_success())
    def test_calculate_steepest_ascent_coordinate_success(self, array, current_coordinate, expected_result):
        # Arrange
        ascender = Ascender(array, current_coordinate)

        # Act
        steepest_ascent_coordinate = ascender._calculate_steepest_ascent_coordinate(current_coordinate)

        # Assert
        assert steepest_ascent_coordinate == expected_result

    @pytest.mark.parametrize(*data.test_generate_ascent_route_success())
    def test_generate_ascent_route_success(self, array, start_coordinate, expected_result):
        # Arrange
        ascender = Ascender(array, start_coordinate)

        # Act
        ascent_route = list(coord for coord in ascender)

        # Assert
        assert ascent_route == expected_result
