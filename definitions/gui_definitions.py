"""
/**************************************************************
* Name        : gui_definitions.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This class file defines the GUI classes
                used in the Scheduling Application.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
import tkinter as tk
from tkinter import *
from modules.validate import validate
import time
from definitions.definitions import Schedule
import os
import shutil

# Global object instantiation and initialization.
schedule = Schedule()
registered = []

# Data restoration support.
# Select logic to determine if previous backup exists.
if os.path.exists("../backup/backup.csv"):
    # If file exists, import the file.
    schedule.import_csv()
else:
    # Copy fresh validation file into active folder if backup does not exist.
    shutil.copyfile("../test_files/valid.csv", "../import/valid.csv")


""" Class SchedulingApp"""


class SchedulingApp(tk.Tk):
    """
    Base Tkinter class; instantiates Tkinter window object.
    """
    def __init__(self):
        """
        Default constructor.
        """
        # Instantiate Tkinter window object.
        tk.Tk.__init__(self)
        # Set private frame member as None.
        self._frame = None
        # Function call to switch to StartPage frame.
        self.switch_frame(StartPage)
        # Set window title.
        self.title("Space Adventure Ride Scheduler")

    def switch_frame(self, frame_class):
        """
        Function that switches between frame objects.
        :param frame_class: Required frame object.
        :return: No return.
        """
        # Render new frame.
        new_frame = frame_class(self)
        # If another frame exists.
        if self._frame is not None:
            # Destroy frame.
            self._frame.destroy()
        # Set base class frame as the new frame.
        self._frame = new_frame
        # Pack the frame using default layout.
        self._frame.pack()

    def exit_app(self):
        """
        Function for application exit.
        :return: Return not possible.
        """
        # Destroy Window.
        self.destroy()
        # Force termination of application.
        sys.exit()


""" Class StartPage"""


class StartPage(tk.Frame):
    """
    StartPage class; the first menu in the app.
    """
    def __init__(self, master):
        """
        Default constructor.
        :param master: Required Tkinter frame object.
        """
        # Instantiate new frame from base class.
        tk.Frame.__init__(self, master)
        # Set application label and render with default layout.
        tk.Label(self, text="Space Adventure Ride Scheduler",
                 font=('Helvetica', 18, "bold")).pack(side="top",
                                                      fill="x",
                                                      pady=5)
        # Render buttons using default layout.
        tk.Button(self, text="Register", width=10, pady=5,
                  command=lambda:
                  master.switch_frame(RegistrationPage)).pack()
        tk.Button(self, text="Admin", width=10, pady=5,
                  command=lambda: master.switch_frame(AdminPage)).pack()
        tk.Button(self, text="Exit", width=10, pady=5,
                  command=lambda: master.exit_app()).pack()


"""Class RegistrationPage """


class RegistrationPage(tk.Frame):
    """
    Registrations class; the registration page in the app.
    """
    def __init__(self, master):
        """
        Default constructor.
        :param master: Required Tkinter frame object.
        """
        tk.Frame.__init__(self, master)
        # Initialize status label.
        label_status = tk.Label(self,
                                text="",
                                anchor="w", width=60)
        # Render status label.
        label_status.grid(row=10, column=3, padx=10, pady=5, sticky="nw")
        # Configure initial status label message.
        label_status.config(text="Please enter your information to register.",
                            fg="black")

        # Define input boxes.
        # Ticket 1
        label_ticket_1 = tk.Label(self, text="Ticket 1:")
        input_ticket_1 = tk.Entry(self, width=10)
        label_age_1 = tk.Label(self, text="Age:")
        input_age_1 = tk.Entry(self, width=10)
        label_height_1 = tk.Label(self, text="Height (in):")
        input_height_1 = tk.Entry(self, width=10)
        label_email_1 = tk.Label(self, text="email:")
        input_email_1 = tk.Entry(self, width=40)

        # Ticket 2
        label_ticket_2 = tk.Label(self, text="Ticket 2:")
        input_ticket_2 = tk.Entry(self, width=10)
        label_age_2 = tk.Label(self, text="Age:")
        input_age_2 = tk.Entry(self, width=10)
        label_height_2 = tk.Label(self, text="Height (in):")
        input_height_2 = tk.Entry(self, width=10)
        label_email_2 = tk.Label(self, text="email:")
        input_email_2 = tk.Entry(self, width=40)

        # Ticket 3
        label_ticket_3 = tk.Label(self, text="Ticket 3:")
        input_ticket_3 = tk.Entry(self, width=10)
        label_age_3 = tk.Label(self, text="Age:")
        input_age_3 = tk.Entry(self, width=10)
        label_height_3 = tk.Label(self, text="Height (in):")
        input_height_3 = tk.Entry(self, width=10)
        label_email_3 = tk.Label(self, text="email:")
        input_email_3 = tk.Entry(self, width=40)

        # Ticket 4
        label_ticket_4 = tk.Label(self, text="Ticket 4:")
        input_ticket_4 = tk.Entry(self, width=10)
        label_age_4 = tk.Label(self, text="Age:")
        input_age_4 = tk.Entry(self, width=10)
        label_height_4 = tk.Label(self, text="Height (in):")
        input_height_4 = tk.Entry(self, width=10)
        label_email_4 = tk.Label(self, text="email:")
        input_email_4 = tk.Entry(self, width=40)

        # Initialize input boxes.
        # Ticket #1
        label_ticket_1.grid(row=2, column=0, padx=10, sticky="nw")
        input_ticket_1.grid(row=3, column=0, padx=10, sticky="nw")
        label_age_1.grid(row=2, column=1, padx=10, sticky="nw")
        input_age_1.grid(row=3, column=1, padx=10, sticky="nw")
        label_height_1.grid(row=2, column=2, padx=10, sticky="nw")
        input_height_1.grid(row=3, column=2, padx=10, sticky="nw")
        label_email_1.grid(row=2, column=3, padx=10, sticky="nw")
        input_email_1.grid(row=3, column=3, padx=10, sticky="nw")
        label_ticket_2.grid(row=4, column=0, padx=10, sticky="nw")
        input_ticket_2.grid(row=5, column=0, padx=10, sticky="nw")
        label_age_2.grid(row=4, column=1, padx=10, sticky="nw")
        input_age_2.grid(row=5, column=1, padx=10, sticky="nw")
        label_height_2.grid(row=4, column=2, padx=10, sticky="nw")
        input_height_2.grid(row=5, column=2, padx=10, sticky="nw")
        label_email_2.grid(row=4, column=3, padx=10, sticky="nw")
        input_email_2.grid(row=5, column=3, padx=10, sticky="nw")
        label_ticket_3.grid(row=6, column=0, padx=10, sticky="nw")
        input_ticket_3.grid(row=7, column=0, padx=10, sticky="nw")
        label_age_3.grid(row=6, column=1, padx=10, sticky="nw")
        input_age_3.grid(row=7, column=1, padx=10, sticky="nw")
        label_height_3.grid(row=6, column=2, padx=10, sticky="nw")
        input_height_3.grid(row=7, column=2, padx=10, sticky="nw")
        label_email_3.grid(row=6, column=3, padx=10, sticky="nw")
        input_email_3.grid(row=7, column=3, padx=10, sticky="nw")
        label_ticket_4.grid(row=8, column=0, padx=10, sticky="nw")
        input_ticket_4.grid(row=9, column=0, padx=10, sticky="nw")
        label_age_4.grid(row=8, column=1, padx=10, sticky="nw")
        input_age_4.grid(row=9, column=1, padx=10, sticky="nw")
        label_height_4.grid(row=8, column=2, padx=10, sticky="nw")
        input_height_4.grid(row=9, column=2, padx=10, sticky="nw")
        label_email_4.grid(row=8, column=3, padx=10, sticky="nw")
        input_email_4.grid(row=9, column=3, padx=10, sticky="nw")

        # Confirm button.
        confirm_button = \
            tk.Button(self,
                      text="Confirm",
                      command=lambda: validation_helper(input_ticket_1,
                                                        input_ticket_2,
                                                        input_ticket_3,
                                                        input_ticket_4,
                                                        input_age_1,
                                                        input_age_2,
                                                        input_age_3,
                                                        input_age_4,
                                                        input_height_1,
                                                        input_height_2,
                                                        input_height_3,
                                                        input_height_4,
                                                        input_email_1,
                                                        input_email_2,
                                                        input_email_3,
                                                        input_email_4,
                                                        ), width=10)
        confirm_button.grid(row=10, column=0, sticky="nw", padx=10, pady=5)

        # Clear button.
        clear_button = \
            tk.Button(self,
                      text="Clear",
                      command=lambda: master.switch_frame(RegistrationPage),
                      width=10)
        clear_button.grid(row=10, column=1, sticky="nw", padx=10, pady=5)

        # Home button.
        home_button = tk.Button(self, text="Home",
                                command=lambda: master.switch_frame(StartPage),
                                width=10)
        home_button.grid(row=10, column=2, sticky="nw", padx=10, pady=5)

        def validation_helper(ticket_1, ticket_2, ticket_3, ticket_4,
                              age_1, age_2, age_3, age_4, height_1,
                              height_2, height_3, height_4,
                              email_1, email_2, email_3, email_4):
            """
            Helper function to call module for input validation.
            :param ticket_1: Required: tkinter Entry object type.
            :param ticket_2: Required: tkinter Entry object type.
            :param ticket_3: Required: tkinter Entry object type.
            :param ticket_4: Required: tkinter Entry object type.
            :param age_1: Required: tkinter Entry object type.
            :param age_2: Required: tkinter Entry object type.
            :param age_3: Required: tkinter Entry object type.
            :param age_4: Required: tkinter Entry object type.
            :param height_1: Required: tkinter Entry object type.
            :param height_2: Required: tkinter Entry object type.
            :param height_3: Required: tkinter Entry object type.
            :param height_4: Required: tkinter Entry object type.
            :param email_1: Required: tkinter Entry object type.
            :param email_2: Required: tkinter Entry object type.
            :param email_3: Required: tkinter Entry object type.
            :param email_4: Required: tkinter Entry object type.
            :return: No return; function executes another function if
            validation passes.
            """

            # Local variable declaration and initialization.
            # Create a list of entry list objects.
            entries = []
            # Get values from entry objects and assign to a list for
            # each entry.
            if ticket_1.get() != "":
                entry_1 = [ticket_1.get(),
                           age_1.get(), height_1.get(), email_1.get()]
                entries.append(entry_1)
            if ticket_2.get() != "":
                entry_2 = [ticket_2.get(),
                           age_2.get(), height_2.get(), email_2.get()]
                entries.append(entry_2)
            if ticket_3.get() != "":
                entry_3 = [ticket_3.get(),
                           age_3.get(), height_3.get(), email_3.get()]
                entries.append(entry_3)
            if ticket_4.get() != "":
                entry_4 = [ticket_4.get(),
                           age_4.get(), height_4.get(), email_4.get()]
                entries.append(entry_4)

            validated, message = validate(entries)

            if not validated:
                label_status.config(text=message, fg="red")
            else:
                # Function call to confirm.
                confirm(entries)

        def confirm(entries):
            """
            Function that updates registration frame for confirmation.
            :param entries: Required list.
            :return: No return.
            """

            # Set Entry object state to disabled to prevent editing.
            input_ticket_1.config(state="disabled")
            input_ticket_2.config(state="disabled")
            input_ticket_3.config(state="disabled")
            input_ticket_4.config(state="disabled")
            input_age_1.config(state="disabled")
            input_age_2.config(state="disabled")
            input_age_3.config(state="disabled")
            input_age_4.config(state="disabled")
            input_height_1.config(state="disabled")
            input_height_2.config(state="disabled")
            input_height_3.config(state="disabled")
            input_height_4.config(state="disabled")
            input_email_1.config(state="disabled")
            input_email_2.config(state="disabled")
            input_email_3.config(state="disabled")
            input_email_4.config(state="disabled")

            # Update status label.
            label_status.config(text="Please review your information and "
                                     "select 'Yes' to confirm reservation.",
                                fg="black")

            # Yes button.
            yes_button = tk.Button(self, text="Yes",
                                   command=lambda: populate(entries), width=10)
            yes_button.grid(row=10, column=0, sticky="nw", padx=10, pady=5)

            # Cancel button.
            cancel_button = tk.Button(self, text="Cancel",
                                      command=lambda:
                                      master.switch_frame(AdminPage),
                                      width=10)
            cancel_button.grid(row=10, column=1, sticky="nw", padx=10, pady=5)

        def populate(entries):
            """
            Function that calls Schedule class insert function.
            :param entries: Required list.
            :return: No return.
            """

            # Function call to insert data into queue.
            schedule.insert(entries)

            # Update label for confirmation.
            label_status.config(text="Processed successfully.", fg="black")
            self.update()
            time.sleep(2)

            # Function call for additional registration.
            master.switch_frame(RegistrationPage)


""" Class Admin """


class AdminPage(tk.Frame):
    """
    Admin class; the registration page in the app.
    """
    def __init__(self, master):
        """
        Default constructor.
        :param master: Required Tkinter frame object.
        """
        # Render frame.
        tk.Frame.__init__(self, master)

        label_status = tk.Label(self,
                                text="",
                                anchor="w", width=60)
        # Render status label.
        label_status.grid(row=0, column=3, padx=10, pady=5, sticky="nw")
        label_status.config(text="Please select an option.")

        # Home button.
        home = tk.Button(self, text="Home",
                         command=lambda: master.switch_frame(StartPage),
                         width=10)
        home.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

        # Export button.
        export = tk.Button(self, text="Export",
                           command=lambda: confirm(), width=10)
        export.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        # If backup file does not exist, disable export button.
        if not os.path.exists("../backup/backup.csv"):
            export.config(state="disabled")

        def confirm():
            """
            Helper function to confirm export validation.
            :return: No return.
            """

            label_status.config(text="Are you sure?", fg='red')

            # Yes button.
            yes_button = tk.Button(self, text="Yes",
                                   command=lambda: process(), width=10)
            yes_button.grid(row=0, column=0, sticky="nw", padx=10, pady=5)

            # Cancel button.
            cancel_button = tk.Button(self, text="Cancel",
                                      command=lambda:
                                      master.switch_frame(AdminPage),
                                      width=10)
            cancel_button.grid(row=0, column=1, sticky="nw", padx=10, pady=5)

        def process():
            """
            Helper function that performs function call and updates
            status label.
            :return: No return.
            """
            # Function call to process export.
            schedule.export_csv()

            # Update label for confirmation.
            label_status.config(text="Processed successfully.", fg="black")
            self.update()
            time.sleep(2)

            # Function call for additional registration.
            master.switch_frame(AdminPage)
