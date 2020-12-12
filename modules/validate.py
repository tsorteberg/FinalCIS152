"""
/**************************************************************
* Name        : validate.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : The purpose of this modules is to provide
                input validation for the GUI application.
                A list is passed to the validate function,
                which returns a boolean value to indicate
                if the validation passed, and an applicable
                message for the user.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
import csv


def check_ticket(ticket_num):
    """
    Helper function that verifies that ticket is valid by checking
    a .csv file.
    :param ticket_num: Required string.
    :return: Returns a boolean.
    """

    # Local variable declaration and initialization.
    return_statement = False

    # Input validation.
    if isinstance(ticket_num, str):
        # Try except clause to check if file is available.
        try:
            # Open valid.csv file and read line by line.
            with open('../import/valid.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    # If match is found, set return statement to True.
                    if ticket_num == row[0]:
                        return_statement = True
        except FileNotFoundError:
            # Raise exception.
            raise FileNotFoundError("ERROR: valid.csv file cannot be found.")
        # Close open object.
        csv_file.close()
    else:
        # Raise exception.
        raise ValueError("Parameter must be of type string.")

    # Return statement.
    return return_statement


def update_csv(entries):
    """
    Static method that removes ticket numbers to prevent
    additional registrations.
    :param entries: Required list.
    :return: No return.
    """
    # Local variable declaration and initialization.
    temp = []
    # Input validation.
    if isinstance(entries, list):
        # Try except clause to check if file is available.
        try:
            with open("../import/valid.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    temp.append(row[0])
        except FileNotFoundError:
            # Raise exception.
            raise FileNotFoundError("ERROR: valid.csv file cannot be found.")
        # Close open object.
        csv_file.close()
        # Remove all ticket numbers from temporary list.
        for entry in entries:
            temp.remove(entry[0])
        # Overwrite valid.csv file to reflect available ticket numbers.
        with open("../import/valid.csv", mode='w', newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in temp:
                csv_writer.writerow([row])
        # Close open object.
        csv_file.close()
    else:
        # Raise exception.
        raise ValueError("Parameter must be of type list.")
