from numpy.testing import assert_array_equal
import pytest
from gradientascent.ascender import Ascender
from gradientascent.summiter import Summitter
                                     
import test_data as data


class TestSummitter:
    
    @pytest.mark.parametrize(*data.test_create_summit_heatmap_success())
    def test_create_summit_heatmap_success(self, ascender, expected_result):
        # Arrange
        smt = Summitter(ascender)

        # Act
        summit_heatmap = smt.create_summit_heatmap()

        # Assert
        assert_array_equal(summit_heatmap, expected_result)

    @pytest.mark.parametrize(*data.test_is_visited_success())
    def test_is_visited_success(self, ascender, summit_heatmap, coordinate, expected_result):
        # Arrange
        smt = Summitter(ascender)
        smt.summit_heatmap = summit_heatmap

        # Act
        is_visited = smt._is_visited(coordinate)

        # Assert
        assert is_visited == expected_result

    @pytest.mark.parametrize(*data.test_get_summit_coord_success())
    def test_get_summit_coord_success(self, ascender, expected_result):
        # Arrange
        smt = Summitter(ascender)

        # Act
        smt_coord = smt._get_summit_coord(smt.ascender.array)

        # Assert
        assert smt_coord == expected_result
