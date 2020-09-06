import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):

    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("ชายยย"))

    def test_validate_name_with_valid_input_string_of_int(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_valid_input_contained_string_of_int(self):
        self.assertEqual(False, validate_name("ชายปอzaa007"))

    def test_validate_name_with_valid_input_contained_spcaice_of_spcaice(self):
        self.assertEqual(False, validate_name("!?@#$%^&*()_+"))

    def test_validate_name_with_valid_input_contained_none_of_None(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_valid_input_contained_none_of_spaceing(self):
        self.assertEqual(False, validate_name("ชาย ปอ"))

    def test_validate_id_with_valid_input_id_none_of_id(self):
        self.assertEqual(False, validate_id("1231243"))

    def test_validate_id_with_valid_input_id_none_of_none(self):
        self.assertEqual(False, validate_id(""))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
