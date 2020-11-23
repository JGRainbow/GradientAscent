from pytest import param


def test_assess_error_data():
    test_variables = "user_times_list, metronome_times_list, expected_result"
    test_data = [
        param(
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            0,
            id='perfect score over 4 beats'
        ),
        param(
            [0.1, 1.1, 2.1, 3.1],
            [0, 1, 2, 3],
            0.1,
            id=r'all user times 0.1 out of sync|'
        ),
        param(
            [0, 1, 2, 3],
            [0, 1, 2],
            0, # maybe add a penalty?
            id='perfect score, one missing'
        )
    ]
    return test_variables, test_data