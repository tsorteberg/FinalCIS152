"""
/**************************************************************
* Name        : main.py
* Author      : Tom Sorteberg
* Created     : 12/08/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10 Professional 1909
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This file represents the main driver code
                that will start the GUI.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
***************************************************************/
"""
from definitions import gui_definitions

if __name__ == "__main__":

    # Run GUI.
    app = gui_definitions.SchedulingApp()
    app.mainloop()
