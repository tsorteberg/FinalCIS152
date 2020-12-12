"""
/**************************************************************
* Name        : test_schedule.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : The purpose of this file is to perform
                unit testing for the Schedule class.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
import unittest
from definitions import definitions
import shutil
import os
import csv

# Copy fresh validation file into active folder.
shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")


class MyTestCase(unittest.TestCase):

    def test_insert_ticket_no_input(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["", "42", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_ticket_length(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP0001", "42", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_ticket_format(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GA00001", "42", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_ticket_invalid(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00005", "42", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_age_no_input(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_age_range(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "2", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_age_format(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "ABC", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_height_no_input(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "42", "", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_height_range(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "42", "36", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_height_format(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00003", "42", "ABC", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_email_no_input(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00001", "42", "72", ""]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_email_invalid(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00001", "42", "72", "noyb.noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_duplicates(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GP00001", "42", "72", "noyb@noyb.com"],
                     ["GP00001", "42", "72", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_accompany_invalid(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["PR00001", "5", "48", "noyb@noyb.com"],
                     ["PR00001", "13", "60", "noyb@noyb.com"]]
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.insert(test_info)

    def test_insert_valid(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        test_info = [["GP00001", "42", "72", "noyb@noyb.com"]]
        expected = 1
        # ACT
        schedule.insert(test_info)
        actual = schedule.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_remove(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        schedule.insert([['GR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00003', '42', '72', 'noyb@noyb.com']])
        expected = 3
        # ACT
        schedule.remove()
        actual = schedule.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_size_join(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        test_info_1 = [["GP00002", "42", "72", "noyb@noyb.com"]]
        test_info_2 = [["GP00003", "42", "72", "noyb@noyb.com"]]
        expected = 1
        # ACT
        schedule.insert(test_info_1)
        schedule.insert(test_info_2)
        actual = schedule.size()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_size_new(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        test_info_1 = [["GS00001", "42", "72", "noyb@noyb.com"]]
        test_info_2 = [["GR00002", "42", "72", "noyb@noyb.com"]]
        expected = 2
        # ACT
        schedule.insert(test_info_1)
        schedule.insert(test_info_2)
        actual = schedule.size()
        # ASSERT
        self.assertEqual(actual, expected)

        # Delete backup file.
        os.remove("../backup/backup.csv")

    def test_is_empty(self):
        # ARRANGE
        schedule = definitions.Schedule()
        expected = True
        # ACT
        actual = schedule.is_empty()
        # ASSERT
        self.assertEqual(actual, expected)

    def test_search_error(self):
        # ARRANGE
        schedule = definitions.Schedule()
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.search("ABC")

    def test_search_invalid(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        test_info_1 = [["PR00002", "42", "72", "noyb@noyb.com"]]
        test_info_2 = [["PR00003", "42", "72", "noyb@noyb.com"]]
        expected = False
        # ACT
        schedule.insert(test_info_1)
        schedule.insert(test_info_2)
        actual = schedule.search(2)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_search_valid(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info_11 = [["GS00002", "42", "72", "noyb@noyb.com"]]
        test_info_22 = [["GS00003", "42", "72", "noyb@noyb.com"]]
        expected = True
        # ACT
        schedule.insert(test_info_11)
        schedule.insert(test_info_22)
        actual = schedule.search(1)

        # ASSERT
        self.assertEqual(actual, expected)

    def test_display_group_exception(self):
        # ARRANGE
        schedule = definitions.Schedule()
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            schedule.display_group("ABC")

    def test_display_group_valid(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["PR00001", "42", "72", "noyb@noyb.com"]]
        expected = "Group#: 1, Priority: C, \nMembers: \n\n" \
                   "Ticket#: PR00001\n" \
                   "Age: 42\n" \
                   "Height: 72\n" \
                   "email: noyb@noyb.com\n"
        # ACT
        schedule.insert(test_info)
        actual = schedule.display_group(1)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_backup_csv_success(self):
        # ARRANGE
        schedule = definitions.Schedule()
        test_info = [["GR00001", "42", "72", "noyb@noyb.com"]]
        temp_list = []
        expected = [['1', 'D', "[['GR00001', '42', '72', 'noyb@noyb.com']]"]]
        # ACT
        schedule.insert(test_info)
        schedule.backup_csv()
        with open('../backup/backup.csv', mode='r', newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                temp_list.append(line)
        csv_file.close()
        actual = temp_list
        # ASSERT
        self.assertEqual(actual, expected)

    def test_export_csv(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        schedule.insert([['GR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00003', '42', '72', 'noyb@noyb.com']])
        expected = True
        # ACT
        schedule.selection_sort()
        schedule.export_csv()
        actual = os.path.exists("../export/export.csv")
        # ASSERT
        self.assertEqual(expected, actual)

    def test_import_csv_success(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        expected = "Group#: 1, Priority: D, \nMembers: \n\n" \
                   "Ticket#: GR00001\n" \
                   "Age: 42\n" \
                   "Height: 72\n" \
                   "email: noyb@noyb.com\n\n" \
                   "Ticket#: GR00002\n" \
                   "Age: 42\n" \
                   "Height: 72\n" \
                   "email: noyb@noyb.com\n\n" \
                   "Ticket#: GR00003\n" \
                   "Age: 42\n" \
                   "Height: 72\n" \
                   "email: noyb@noyb.com\n" \
        # ACT
        schedule.insert([['GR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00003', '42', '72', 'noyb@noyb.com']])
        schedule = definitions.Schedule()
        schedule.import_csv()
        actual = schedule.display_group(1)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_priority_fail(self):
        # ARRANGE
        test_info = "[['GR00001', '42', '72', 'noyb@noyb.com']]"
        # ACT
        # ASSERT
        with self.assertRaises(ValueError):
            definitions.Schedule.priority(test_info)

    def test_priority_success(self):
        # ARRANGE
        test_info = [['GR00001', '42', '72', 'noyb@noyb.com']]
        expected = "D"
        # ACT
        actual = definitions.Schedule.priority(test_info)
        # ASSERT
        self.assertEqual(actual, expected)

    def test_selection_sort(self):
        # ARRANGE
        shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")
        schedule = definitions.Schedule()
        schedule.insert([['GR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GS00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['PR00003', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00001', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00002', '42', '72', 'noyb@noyb.com']])
        schedule.insert([['GP00003', '42', '72', 'noyb@noyb.com']])
        expected = "A"
        # ACT
        schedule.selection_sort()
        actual = schedule.remove().get_priority()
        # ASSERT
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #
#   insert() ticket: blank      Exception                   Exception         #
#   insert() ticket: "GP0001"   Exception                   Exception         #
#   insert() ticket: "GA00001"  Exception                   Exception         #
#   insert() ticket: "GP00004"  Exception                   Exception         #
#   insert() age: blank         Exception                   Exception         #
#   insert() age: "2"           Exception                   Exception         #
#   insert() age: "ABC"         Exception                   Exception         #
#   insert() height: blank      Exception                   Exception         #
#   insert() height: "2"        Exception                   Exception         #
#   insert() height: "ABC"      Exception                   Exception         #
#   insert() email: blank       Exception                   Exception         #
#   insert() email: invalid     Exception                   Exception         #
#   insert() ticket: duplicate  Exception                   Exception         #
#   insert() age: invalid       Exception                   Exception         #
#        is_empty()             True                        True              #
#       priority()              Exception                   Exception         #
#       priority()              Success                     Success           #
#   insert() all: Valid         Success                     Success           #
#       backup_csv()            Success                     Success           #
#   size() 2 Same Priority         1                           1              #
#  size() 2 Different Priority     2                           2              #

