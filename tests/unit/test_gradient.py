from numpy.testing import assert_array_equal
import pytest
from gradientascent.gradient import calculate_2d_gradient

import test_data as data


class TestGradient:
    
    @pytest.mark.parametrize(*data.test_calculate_2d_gradient_success())
    def test_calculate_2d_gradient_success(self, array, expected_result):
        # Arrange
        # Act
        gradient = calculate_2d_gradient(array)

        # Assert
        assert_array_equal(gradient, expected_result)
