"""
/**************************************************************
* Name        : definitions.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This class file defines both the Schedule
                and Group wrapper data types for the
                Scheduling Application.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
from constants import constants
from modules.validate import check_ticket
import re
from modules.validate import update_csv
import csv

""" Class Schedule"""


class Schedule(object):
    """
    This class represents a queue data structure with
    associated class and static functions.  The Schedule
    queue is then populated with Group class nodes.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self._queue = []
        self._group_number = 1

    def insert(self, entries):
        """
        Inserts a group object
        :param entries: Required list.
        :return: No return.
        """

        # Local variable declaration and initialization.
        character_set = set("0123456789GSPR ")
        number_set = set("0123456789")
        email_set = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        length = len(entries)
        priority = self.priority(entries)
        inserted = False
        no_email = False
        min_age = False
        max_age = False
        checked = []
        duplicate = False

        # Input validation.
        for entry in entries:
            # Validate ticket numbers.
            if len(entry[0]) != constants.TICKET_LEN \
                    or not character_set.issuperset(entry[0]) \
                    or not check_ticket(entry[0]):
                # Raise exception.
                raise ValueError("Invalid value for ticket number parameter.")
            # Validate age.
            elif not number_set.issuperset((entry[1])) or int(entry[1]) < constants.MIN_AGE:
                # Raise exception.
                raise ValueError("Invalid value for age parameter.")
            elif not number_set.issuperset((entry[2])) or int(entry[2]) < constants.MIN_HEIGHT:
                # Raise exception.
                raise ValueError("Invalid value for height parameter.")
            # Validate email.
            elif entry[3] != "" and not re.search(email_set, entry[3]):
                # Raise exception.
                raise ValueError("Invalid value for email parameter.")
            # If there are no email addresses, then set no_email variable to True.
            elif entry[3] != "":
                no_email = True

        # Check for duplicates and age verification.
        for entry in entries:
            if entry[0] is not None and entry[0] in checked:
                duplicate = True
            checked.append(entry[0])
            # If age field is not empty and is an integer.
            if entry[1] != "" and number_set.issuperset(entry[1]):
                # If the age field is less than or equal to 7,
                # set min_age iteration variable to true.
                if int(entry[1]) <= constants.MIN_ACCP:
                    min_age = True
                # If the age field is greater than than or equal to 14,
                # set max_age iteration variable to true.
                if int(entry[1]) >= constants.MAX_ACCP:
                    max_age = True

        # If no email address is provided.
        if not no_email:
            # Raise exception.
            raise ValueError("No value provided for email.")
        # If accompany requirements are not met.
        elif min_age is True and max_age is not True:
            raise ValueError("Accompany requirements not met.")
        # If there are duplicates.
        elif duplicate:
            # Raise exception.
            raise ValueError("Duplicate ticket exists")

        # If the group is full or the queue is empty.
        if length == constants.MAX_GROUP or self.is_empty():
            # Append group object to queue.
            self._queue.append(Group(entries, priority, self._group_number))
            # Increment group number.
            self._group_number += 1
            # Set inserted to True.
            inserted = True
        # Else if group is less than 4, find a group with same priority
        # with room for additional members and if available, insert member
        # information.
        else:
            for group in self._queue:
                if (constants.MAX_GROUP - group.size()) >= length \
                        and priority == group.get_priority():
                    inserted = True
                    for entry in entries:
                        group.update(entry)
        # If queue is not empty and no suitable group is found, create
        # a new group.
        if not inserted:
            self._queue.append(Group(entries, priority, self._group_number))
            # Increment group number.
            self._group_number += 1
        # Remove ticket entries from valid.csv to prevent additional
        # registration.
        update_csv(entries)
        # Write entry to backup.csv file in case of recovery.
        self.backup_csv()

    def size(self):
        """
        Function that returns the size of the queue.
        :return: Returns an integer.
        """
        # Return statement.
        return len(self._queue)

    def is_empty(self):
        """
        Function that returns True if the queue is empty.
        :return: Returns a boolean.
        """
        # Return statement.
        return len(self._queue) == 0

    def search(self, value):
        """
        Function that performs a search based on group number.
        Returns true if found.
        :param value: Required integer.
        :return: Returns a boolean.
        """
        # Local variable declaration and initialization.
        return_statement = False
        # Input Validation.
        if isinstance(value, int):
            # For loop to iterate through queue.
            # If value is found, return True.
            for group in self._queue:
                if group.get_group_num() == value:
                    return_statement = True
        else:
            raise ValueError("Parameter value must be an integer.")

        # Return statement.
        return return_statement

    def backup_csv(self):
        """
        Function that exports data to a .csv for backup.
        :return: No return.
        """

        # Overwrite export.csv if it exists.
        with open('../backup/backup.csv', mode='w', newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for group in self._queue:
                csv_writer.writerow([group.get_group_num(), group.get_priority(), group.get_members()])
        # Close open object.
        csv_file.close()

    @ staticmethod
    def priority(entries):
        """
        Static function that determines group priority.
        :param entries: Required list.
        :return: Returns a string.
        """
        # Local variable declaration and initialization.
        priority = None
        # Input validation.
        if isinstance(entries, list):
            # For loop and selection logic to determine group priority.
            for entry in entries:
                if entry[0] != "" and entry[0][0:2] == "GP":
                    priority = "A"
                elif entry[0] != "" and entry[0][0:2] == "GS":
                    priority = "B"
                elif entry[0] != "" and entry[0][0:2] == "PR":
                    priority = "C"
                elif entry[0] != "" and entry[0][0:2] == "GR":
                    priority = "D"
        else:
            # Raise exception.
            raise ValueError("Parameter must be type list.")

        # Return statement.
        return priority


""" Class Group """


class Group(object):

    def __init__(self, entries, priority, group_num):
        """
        Default constructor.
        :param entries: Required list.
        :param priority: Required String.
        :param group_num: Required integer.
        """
        # Input validation.
        if isinstance(entries, list) \
                and isinstance(priority, str) \
                and isinstance(group_num, int) \
                and len(entries) <= 4:
            self._group_num = group_num

            # Member variable declaration and initialization.
            self._members = entries
            self._priority = priority
        else:
            raise ValueError("Invalid parameter.")

    def size(self):
        """
        Function that returns the size of group.
        :return: Returns an integer.
        """
        # Return statement.
        return len(self._members)

    def update(self, visitor):
        """
        Function that appends members to groups.
        :param visitor: Required list.
        :return: No return.
        """
        # Input validation.
        if isinstance(visitor, list) and self.size() != constants.MAX_GROUP:
            self._members.append(visitor)
        else:
            raise ValueError("Parameter must be of type list.")

    def get_priority(self):
        """
        Function that returns group priority.
        :return: Returns a string.
        """
        # Return statement.
        return self._priority

    def get_members(self):
        """
        Function that returns group member information.
        :return: Returns a list.
        """
        # Return statement.
        return self._members

    def get_group_num(self):
        """
        Function that returns the group number.
        :return: Returns an int.
        """
        # Return statement.
        return self._group_num
