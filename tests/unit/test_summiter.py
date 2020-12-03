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