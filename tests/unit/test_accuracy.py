import pytest

from InThePocket.rhythmic_accuracy import assess_error
import accuracy_test_data as data


class TestAccuracy:
    
    @pytest.mark.parametrize(*data.test_assess_error_data())
    def test_assess_error(self, user_times_list, metronome_times_list, expected_result):
        # Arrange
        # Act
        test_error = assess_error(user_times_list, metronome_times_list)

        # Assert
        assert expected_result == pytest.approx(test_error)