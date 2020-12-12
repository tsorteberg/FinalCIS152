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
import re
from constants import constants as c


def validate(entries):
    """
    Function that validates user input for ticket registration.
    """
    # Local variable definition and initialization:
    return_statement = None

    # Define character sets for validation.
    character_set = set("0123456789GSPR ")
    number_set = set("0123456789")
    email_set = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # Variables used for iteration.
    validated = []
    min_age = False
    max_age = False
    email = False
    state = False
    checked = []
    duplicate = False

    # Input validation.
    if isinstance(entries, list):

        # If at least one value has not been entered into a ticket field,
        # then prompt user with error message.
        if len(entries) == 0:
            # Return error message.
            return_statement = False,\
                               "ERROR: You must enter at least one ticket number."
        # Else begin for loop for input validation.
        else:
            # Index defined for user output.
            index = 1

            # For loop to iterate through list of input values.
            for entry in entries:

                # Loop variable declaration and initialization.
                valid_ticket = False
                valid_age = False
                valid_height = False
                valid_email = False

                # Selection logic to determine if ticket numbers are valid.
                # If the length of the ticket number is not 7
                # and the field is not blank.
                if len(entry[0]) != 7 and entry[0] != "":
                    # Return error message.
                    return_statement = False, \
                                       "ERROR: Ticket " \
                                       + str(index) \
                                       + " must be at least 7 characters in length."
                # If any input characters don't match the allowed set.
                elif not character_set.issuperset(entry[0]) and entry[0] != "":
                    # Return error message.
                    return_statement = False, \
                                       "ERROR: Invalid ticket number entered, " \
                                       "please re-enter ticket " \
                                       + str(index) + "."
                # If ticket number does not match list of active tickets.
                elif entry[0] != "" and not check_ticket(entry[0]):
                    # Return error message.
                    return_statement = False,\
                                       "ERROR: Invalid ticket number entered, " \
                                       "please re-enter ticket " \
                                       + str(index) \
                                       + "."
                # Else set valid ticket loop variable to true.
                else:
                    valid_ticket = True

                # Selection logic to determine if ages are valid.
                # If ticket validation succeeds.
                if valid_ticket:
                    # If ticket field is not blank and age field is blank.
                    if entry[0] != "" and entry[1] == "":
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider's age is required " \
                                           "for ticket " \
                                           + str(index) \
                                           + "."
                    # If ticket field is not blank and age field is not an integer.
                    elif entry[0] != "" and not number_set.issuperset(entry[1]):
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider's age for ticket " \
                                           + str(index) \
                                           + " must be a number."
                    # If ticket field is not blank and age field is less than 3.
                    elif entry[0] != "" and int(entry[1]) < 3:
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider for ticket " \
                                           + str(index) \
                                           + " must at least 3 years old."
                    # Else set valid age loop variable to true.
                    else:
                        valid_age = True

                # Selection logic to determine if heights are valid.
                # If age validation succeeds.
                if valid_age:
                    # If ticket field is not blank and height field is blank.
                    if entry[0] != "" and entry[2] == "":
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider's height " \
                                           "is required for ticket " \
                                           + str(index) + "."
                    # If ticket field is not blank and height field is not
                    # an integer.
                    elif entry[0] != "" and not number_set.issuperset(entry[2]):
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider's height for ticket " \
                                           + str(index) + " must be a number."
                    # If ticket field is not blank and height field is less than 48.
                    elif entry[0] != "" and int(entry[2]) < 48:
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Rider for ticket " \
                                           + str(index) \
                                           + " must at least 48 inches tall."
                    # Else set valid height loop variable to true.
                    else:
                        valid_height = True
                # Selection logic to determine if email addresses are valid.
                # If height validation succeeds.
                if valid_height:
                    # If ticket field is not blank and email field is not blank any
                    # input characters don't match the allowed set.
                    if entry[0] != "" \
                            and entry[3] != "" \
                            and not re.search(email_set, entry[3]):
                        # Return error message.
                        return_statement = False, \
                                           "ERROR: Invalid email address for" \
                                           " ticket " \
                                           + str(index) + "."
                    # Else set valid email loop variable to true.
                    else:
                        valid_email = True

                # Selection logic to determine if validation passed for all inputs.
                # If all fields for entry pass validation,
                # then append true to validated list.
                if valid_ticket and valid_age and valid_height and valid_email:
                    validated.append(True)
                # Else append false to validated list.
                else:
                    validated.append(False)

                # Selection logic to track age and email categories.
                # If email field is not empty,
                # set email iteration variable to true.
                if entry[3] != "":
                    email = True

                # If age field is not empty and is an integer.
                if entry[1] != "" and number_set.issuperset(entry[1]):
                    # If the age field is less than or equal to 7,
                    # set min_age iteration variable to true.
                    if int(entry[1]) <= c.MIN_ACCP:
                        min_age = True
                    # If the age field is greater than than or equal to 14,
                    # set max_age iteration variable to true.
                    if int(entry[1]) >= c.MAX_ACCP:
                        max_age = True
                # Increment index.
                index += 1
        # Check for duplicates
        for entry in entries:
            if entry[0] != "" and entry[0] in checked:
                duplicate = True
            checked.append(entry[0])
        # Selection logic to determine if at least one email address has been
        # entered and age requirements are met.
        if len(validated) != 0 and state not in validated:
            # If minor is unaccompanied.
            if min_age is True and max_age is not True:
                # Return error message.
                return_statement = False, \
                                   "ERROR: Children under the age of 7 must be " \
                                   "accompanied by someone\n 14 years or older."
            # If no email address was entered.
            elif not email:
                # Return error message.
                return_statement = False, \
                                   "ERROR: At least one email address must be " \
                                   "provided for confirmation."
            # If duplicates are found.
            elif duplicate:
                # Prompt user with error message.
                return_statement = False, \
                                   "ERROR: Duplicate ticket numbers exist."
            else:
                # Set return statement to true.
                return_statement = True, ""
    else:
        # Raise exception.
        raise ValueError("Parameter must be of type list.")

    # Return statement.
    return return_statement


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
