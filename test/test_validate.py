"""
/**************************************************************
* Name        : test_validate.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : The purpose of this file is to perform
                unit testing for the validate.py module.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
import unittest
from modules import validate
import shutil
import csv
import os

# Copy fresh validation file into active folder.
shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")


class MyTestCase(unittest.TestCase):

    def test_validate_no_input(self):
        # ARRANGE
        test_info = []
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_ticket_length(self):
        # ARRANGE
        test_info = [["GP0001", "", "", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_ticket_format(self):
        # ARRANGE
        test_info = [["GA00001", "", "", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_age_blank(self):
        # ARRANGE
        test_info = [["GP00001", "", "", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_age_range(self):
        # ARRANGE
        test_info = [["GP00001", "2", "", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_age_format(self):
        # ARRANGE
        test_info = [["GP00001", "ABC", "", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_height_range(self):
        # ARRANGE
        test_info = [["GP00001", "42", "36", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_height_format(self):
        # ARRANGE
        test_info = [["GP00001", "42", "ABC", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_email_exists(self):
        # ARRANGE
        test_info = [["GP00001", "42", "72", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_email_format(self):
        # ARRANGE
        test_info = [["GP00001", "42", "72", "noyb.noyb.com"]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_insert_accompany_invalid(self):
        # ARRANGE
        test_info = [["PR00001", "5", "48", "noyb@noyb.com"],
                     ["PR00001", "13", "60", "noyb@noyb.com"]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_insert_duplicates(self):
        # ARRANGE
        test_info = [["GP00001", "42", "72", "noyb@noyb.com"],
                     ["GP00001", "42", "72", "noyb@noyb.com"]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_insert_email_no_input(self):
        # ARRANGE
        test_info = [["GP00001", "42", "72", ""]]
        expected = False
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_validate_success(self):
        # ARRANGE
        test_info = [["GP00002", "42", "72", "noyb@noyb.com"]]
        expected = True
        # ACT
        actual_1, actual_2 = validate.validate(test_info)
        # ASSERT
        self.assertEqual(actual_1, expected)

    def test_check_ticket_fail(self):
        # ARRANGE
        test_info = "GP00005"
        expected = False
        # ACT
        actual = validate.check_ticket(test_info)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_check_ticket_success(self):
        # ARRANGE
        test_info = "GP00001"
        expected = True
        # ACT
        actual = validate.check_ticket(test_info)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_update_csv_success(self):
        # ARRANGE
        test_info = [["GP00001", "42", "72", "noyb@noyb.com"]]
        temp = []
        actual = False
        expected = False
        for entry in test_info:
            temp.append(entry)
        # ACT
        validate.update_csv(test_info)
        with open("../import/valid.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] in temp:
                    actual = True
        # ASSERT
        self.assertEqual(actual, expected)

    def test_update_csv_fail(self):
        # ARRANGE
        if os.path.exists("../import/valid.csv"):
            os.remove("../import/valid.csv")
        # ACT
        # ASSERT
        with self.assertRaises(FileNotFoundError):
            open("../import/valid.csv", mode='r')

        # Copy fresh validation file into active folder.
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")

    def test_update_csv_input(self):
        # ARRANGE
        test_info = "[['GP00001', '42', '72', 'noyb@noyb.com']]"
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            validate.update_csv(test_info)

    def test_validation_parameter(self):
        # ARRANGE
        test_info = "[['GP00001', '42', '72', 'noyb@noyb.com']]"
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            validate.update_csv(test_info)

    def test_check_ticket_parameter(self):
        # ARRANGE
        test_info = [['GP00001', '42', '72', 'noyb@noyb.com']]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            validate.check_ticket(test_info)


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                           #
#          Input             Expected Output            Actual Output          #
#      check_ticket() "GP00004"  False                       False             #
#      check_ticket() "GP00001"  True                        True              #
#      update_csv                False                       False             #
#      update_csv                Exception                   Exception         #
#      update_csv                Exception                   Exception         #
#      Parameter                 Exception                   Exception         #
#      Parameter                 Exception                   Exception         #
#      Ticket#: blank            False                       False             #
#      Ticket#: "GP0001"         False                       False             #
#      Ticket#: "GA00001"        False                       False             #
#      Age: blank                False                       False             #
#      Age: "2"                  False                       False             #
#      Age: "ABC"                False                       False             #
#      Height: "36"              False                       False             #
#      Height: "ABC"             False                       False             #
#      Email: blank              False                       False             #
#      Email: "noyb.noyb.com     False                       False             #
#      Accompany condition       False                       False             #
#      Duplicate condition       False                       False             #
#      All: Valid Entry          True                        True              #
