import numpy as np
from gradientascent.grid import Coordinate
from pytest import param


def test_get_bordering_coordinates_success():
    test_variables = "array, current_coordinate, expected_result"
    test_data = [
        param(
            np.zeros((3, 3)),
            Coordinate(0, 0),
            [Coordinate(1, 0), Coordinate(0, 1)],
            id='top_left'
        ),
        param(
            np.zeros((3, 3)),
            Coordinate(1, 1),
            [Coordinate(0, 1), Coordinate(2, 1), Coordinate(1, 2), Coordinate(1, 0)],
            id='centre'
        ),
        param(
            np.zeros((3, 3)),
            Coordinate(2, 2),
            [Coordinate(1, 2), Coordinate(2, 1)],
            id='bottom_right'
        )
    ]
    return test_variables, test_data


def test_calculate_steepest_ascent_coordinate_success():
    test_variables = "array, current_coordinate, expected_result"
    test_data = [
        param(
            np.array([[1, 2, 3],
                      [4, 5, 6],
                      [6, 8, 9]]),
            Coordinate(1, 1),
            Coordinate(1, 2),
            id='move_south'
        ),
        param(
            np.array([[1, 2, 3],
                      [4, 9, 6],
                      [6, 8, 5]]),
            Coordinate(2, 2),
            Coordinate(1, 2),
            id='move_west'
        ),
        param(
            np.array([[1, 2, 3],
                      [4, 5, 6],
                      [6, 8, 9]]),
            Coordinate(2, 2),
            Coordinate(2, 2),
            id='stay_stationary'
        )
    ]
    return test_variables, test_data


def test_ascend_one_step_success():
    test_variables = "array, current_coordinate, expected_result"
    test_data = [
        param(
            np.array([[0, 1, 0],
                    [0, 0, 0],
                    [0, 0, 0]]),
            Coordinate(0, 0),
            Coordinate(1, 0),
            id='3x3_top_left'
        )
    ]
    return test_variables, test_data
