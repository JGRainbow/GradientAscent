from pytest import param
import numpy as np


def test_calculate_2d_gradient_success():
    test_variables = "array, expected_result"
    test_data = [
        param(
            np.zeros((3,3)),
            np.zeros((3,3)),
            id='zero_3x3'
            )
    ]
    return test_variables, test_data