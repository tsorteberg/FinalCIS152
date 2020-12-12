"""
/**************************************************************
* Name        : test_group.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : The purpose of this file is to perform
                unit testing for the Group class.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
import unittest
from definitions import definitions


class MyTestCase(unittest.TestCase):

    def test_object_creation_success(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        priority = "A"
        group_num = 1
        expected = 1
        # ACT
        group = definitions.Group(entry, priority, group_num)
        actual = group.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_object_creation_fail_list(self):
        # ARRANGE
        entry = "[['GP00001', '42', '72', 'noyb@noyb.com']]"
        priority = "A"
        group_num = 1
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            definitions.Group(entry, priority, group_num)

    def test_object_creation_fail_string(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        priority = 1
        group_num = 1
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            definitions.Group(entry, priority, group_num)

    def test_object_creation_fail_integer(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        priority = "A"
        group_num = "A"
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            definitions.Group(entry, priority, group_num)

    def test_object_creation_fail_size(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"],
                 ["GP00002", "42", "72", "noyb@noyb.com"],
                 ["GP00003", "42", "72", "noyb@noyb.com"],
                 ["GP00004", "42", "72", "noyb@noyb.com"],
                 ["GP00005", "42", "72", "noyb@noyb.com"]]
        priority = "A"
        group_num = 1
        # ACT
        with self.assertRaises(ValueError):
            definitions.Group(entry, priority, group_num)

    def test_update_success(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info = ["GP00002", "42", "72", "noyb@noyb.com"]
        priority = "A"
        group_num = 1
        expected = 2
        # ACT
        group = definitions.Group(entry, priority, group_num)
        group.update(test_info)
        actual = group.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_update_fail(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info = "['GP00002', '42', '72', 'noyb@noyb.com']"
        priority = "A"
        group_num = 1
        # ACT
        group = definitions.Group(entry, priority, group_num)
        # ASSERT
        with self.assertRaises(ValueError):
            group.update(test_info)

    def test_update_fail_size(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info_1 = ["GP00002", "42", "72", "noyb@noyb.com"]
        test_info_2 = ["GP00003", "42", "72", "noyb@noyb.com"]
        test_info_3 = ["GP00004", "42", "72", "noyb@noyb.com"]
        test_info_4 = ["GP00005", "42", "72", "noyb@noyb.com"]
        priority = "A"
        group_num = 1
        # ACT
        group = definitions.Group(entry, priority, group_num)
        group.update(test_info_1)
        group.update(test_info_2)
        group.update(test_info_3)
        # ASSERT
        with self.assertRaises(ValueError):
            group.update(test_info_4)

    def test_size_success(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info_1 = ["GP00002", "42", "72", "noyb@noyb.com"]
        test_info_2 = ["GP00003", "42", "72", "noyb@noyb.com"]
        test_info_3 = ["GP00004", "42", "72", "noyb@noyb.com"]
        priority = "A"
        group_num = 1
        expected = 4
        # ACT
        group = definitions.Group(entry, priority, group_num)
        group.update(test_info_1)
        group.update(test_info_2)
        group.update(test_info_3)
        actual = group.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_get_priority(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info_1 = ["GP00002", "42", "72", "noyb@noyb.com"]
        test_info_2 = ["GP00003", "42", "72", "noyb@noyb.com"]
        test_info_3 = ["GP00004", "42", "72", "noyb@noyb.com"]
        priority = "A"
        group_num = 1
        expected = "A"
        # ACT
        group = definitions.Group(entry, priority, group_num)
        group.update(test_info_1)
        group.update(test_info_2)
        group.update(test_info_3)
        actual = group.get_priority()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_get_members(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        priority = "A"
        group_num = 1
        expected = [["GP00001", "42", "72", "noyb@noyb.com"]]
        # ACT
        group = definitions.Group(entry, priority, group_num)
        actual = group.get_members()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_get_group_num(self):
        # ARRANGE
        entry = [["GP00001", "42", "72", "noyb@noyb.com"]]
        test_info_1 = ["GP00002", "42", "72", "noyb@noyb.com"]
        test_info_2 = ["GP00003", "42", "72", "noyb@noyb.com"]
        test_info_3 = ["GP00004", "42", "72", "noyb@noyb.com"]
        priority = "A"
        group_num = 1
        expected = 1
        # ACT
        group = definitions.Group(entry, priority, group_num)
        group.update(test_info_1)
        group.update(test_info_2)
        group.update(test_info_3)
        actual = group.get_group_num()
        # ASSERT
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #

