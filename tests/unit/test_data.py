import numpy as np
from gradientascent.ascender import Ascender, Coordinate
from pytest import param

from test_helpers import create_ascender


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
        ),
        param(
            np.zeros((3, 3)),
            Coordinate(1, 0),
            [Coordinate(0, 0), Coordinate(2, 0), Coordinate(1, 1)],
            id='central_top'
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
        ),
        param(
            np.array([[0, 0, 0],
                      [1, 2, 3],
                      [0, 0, 0]]),
            Coordinate(1, 1),
            Coordinate(2, 1),
            id='move_west_from_centre'
        )
    ]
    return test_variables, test_data


def test_generate_ascent_route_success():
    test_variables = "array, start_coordinate, expected_result"
    test_data = [
        param(
            np.array([[0, 1, 0],
                      [0, 0, 0],
                      [0, 0, 0]]),
            Coordinate(0, 0),
            [Coordinate(0, 0), Coordinate(1, 0)],
            id='single_step'
        ),
        param(
            np.array([[1, 2, 3],
                      [0, 0, 4],
                      [0, 0, 5]]),
            Coordinate(0, 0),
            [Coordinate(0, 0), Coordinate(1, 0), Coordinate(2, 0),
             Coordinate(2, 1), Coordinate(2, 2)],
             id='north_east_pass'
        )
        # param(
        #     np.array([[1, 2, 3],
        #               [2, 2, 4],
        #               [1, 1, 5]]),
        #     Coordinate(0, 0),
        #     [Coordinate(0, 0), Coordinate(1, 0), Coordinate(2, 0),
        #      Coordinate(2, 1), Coordinate(2, 2)],
        #      id='north_east_pass'
        # ),
    ]
    return test_variables, test_data


def test_create_summit_heatmap_success():
    test_variables = "ascender, expected_result"
    test_data = [
        param(
            create_ascender(np.array([[1, 2, 3],
                                      [2, 2, 4],
                                      [1, 1, 5]])),
            np.array([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]]),
            id='all_reach_top_3x3'
            )
    ]
    return test_variables, test_data

