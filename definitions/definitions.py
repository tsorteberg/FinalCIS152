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
